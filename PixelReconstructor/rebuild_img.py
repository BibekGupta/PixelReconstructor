from PIL import Image, ImageDraw
import psutil
import time

# The Timer starts when the script runs
start_time = time.time()

def process_power():
        process = psutil.Process()
        memory_usage = round(process.memory_info().rss / (1024 * 1024), 2)

        current_time = time.time()

        uptime_seconds = current_time - start_time
        uptime_minutes, uptime_seconds = divmod(uptime_seconds, 60)
        uptime_hours, uptime_minutes = divmod(uptime_minutes, 60)
        uptime_seconds = f'{uptime_seconds:.2f}'
        uptime = f'{uptime_hours:.0f}h {uptime_minutes:.0f}m {uptime_seconds}s'

        # Write to the file instead of printing to the terminal
        print(f"-> Memory Usage: {memory_usage} MB")
        print(f"-> Time Takens: {uptime}")


def create_image_from_pixels(input_file, output_image_path):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Extracting pixel values from each line
    pixels = []
    for line in lines:
        try:
            # Extracting x, y, and RGB values 
            x, y, r, g, b = map(int, line.strip().split())

            #for debugging
            print(f"[🟢] X: {x}, Y: {y}, R: {r}, G: {g}, B: {b}")

            pixels.append((x, y, (r, g, b)))
        except Exception as e:
            print(f"[🔴] Exception: {e}")
            print(f"[🔴] Error processing line: {line}")

    if not pixels:
        print("[🔴] No valid pixel data found.")
        return

    # Determine the dimensions of the image based on the maximum x and y values
    max_x, max_y = max(data[0] for data in pixels), max(data[1] for data in pixels)

    # Create a blank canvas
    image = Image.new("RGB", (max_x + 1, max_y + 1), color="white")

    # Use ImageDraw to draw rectangles with specified colors
    draw = ImageDraw.Draw(image) 
    for x, y, color in pixels:
        try:
            draw.rectangle([x, y, x + 1, y + 1], fill=color)
        except Exception as e:
            print(f"[🔴] Exception: {e}")
            print(f"[🔴] Error processing line: {x} {y} {color[0]} {color[1]} {color[2]}")

    # Save the image
    image.save(output_image_path)

    # Add print statement to check the size of the image
    print(f"Image size: {image.size}")

    # Add a final check to see if there are any non-white pixels in the image
    non_white_pixels = [(x, y, image.getpixel((x, y))) for x in range(image.width) for y in range(image.height) if image.getpixel((x, y)) != (255, 255, 255)]

# Specify the path to your output file and the desired output image path
input_file_path = 'output.txt'
output_image_path = 'rebuild_img.png'

# Call the function to create the image
create_image_from_pixels(input_file_path, output_image_path)

process_power()
print("[✔] Image creation completed successfully.")   