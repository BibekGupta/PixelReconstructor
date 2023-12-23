from PIL import Image
import numpy as np
import psutil
import time

print('[🟢] Running...')

image_path = 'test.png'  # This is path of the image will be process

# The Timer starts when the script runs
start_time = time.time()

# Open output.txt file in write mode  [w=write ,r=read]
with open('output.txt', 'w') as output_file:

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

    def get_pixel_values(image_path):
        img = Image.open(image_path)

        img_array = np.array(img)

        height, width, channels = img_array.shape

        for y in range(height):
            for x in range(width):
                pixel_values = img_array[y, x]
                # Write to the file instead of printing to the terminal
                # Format is X Y R G B
                print(f"{x} {y} {pixel_values[0]} {pixel_values[1]} {pixel_values[2]}", file=output_file)

        process_power()  # Call Function from above

    get_pixel_values(image_path)


async def main():
        while True:
            process_power()
