import pyarrow.parquet as pq
import requests
import os
import psutil
import time
from PIL import Image

def download_images(parquet_file, output_directory, max_images=10000):
    table = pq.read_table(parquet_file)
    urls = table.column('URL ').to_pylist()
    os.makedirs(output_directory, exist_ok=True)

    downloaded_count = 0
    start_time = time.time()
    last_check_time = start_time
    check_interval = 5  # Adjust accordingly 
    for url in urls:
        if downloaded_count >= max_images:
            break
        try:
            response = requests.get(url)
            if response.status_code == 200:
                filename = url.split('/')[-1]
                with open(os.path.join(output_directory, filename), 'wb') as f:
                    f.write(response.content)
                downloaded_count += 1

                current_time = time.time()
                if current_time - last_check_time >= check_interval:
                    cpu_usage = psutil.cpu_percent()
                    network_usage = psutil.net_io_counters()
                    print(f"Time: {current_time - start_time} sec | CPU Usage: {cpu_usage}% | Network Usage: {network_usage.bytes_sent} bytes sent, {network_usage.bytes_recv} bytes received")
                    last_check_time = current_time
        except Exception as e:
            print(f"Error downloading image from {url}: {str(e)}")
    
    elapsed_time = time.time() - start_time
    cpu_usage = psutil.cpu_percent()
    network_usage = psutil.net_io_counters()

    print(f"Total Elapsed Time: {elapsed_time} seconds")
    print(f"Final CPU Usage: {cpu_usage}%")
    print(f"Final Network Usage: {network_usage.bytes_sent} bytes sent, {network_usage.bytes_recv} bytes received")

    display_images(output_directory)


def display_images(directory):
   
    files = os.listdir(directory)
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    for image_file in image_files:
        file_path = os.path.join(directory, image_file)
        try:
            image = Image.open(file_path)
            image.show()
        except Exception as e:
            print(f"Error displaying image {file_path}: {str(e)}")

parquet_file = "C:/Users/cusat/Desktop/links.parquet"
output_directory = "C:/Users/cusat/Desktop/Output"
download_images(parquet_file, output_directory)
