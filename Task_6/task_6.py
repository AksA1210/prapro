import os
import time
import psutil
import requests
from concurrent.futures import ThreadPoolExecutor
from PIL import Image


class Downloader:
    def __init__(self, parquet_file, output_directory, max_images=100, max_threads=10):
        self.parquet_file = parquet_file
        self.output_directory = output_directory
        self.max_images = max_images
        self.max_threads = max_threads

    def download_image(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                fname = url.split("/")[-1]
                with open(os.path.join(self.output_directory, fname), "wb") as f:
                    f.write(response.content)
                return fname
        except Exception as e:
            print(f"Error downloading image from {url}: {str(e)}")
        return None

    def download_images(self):
        os.makedirs(self.output_directory, exist_ok=True)

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            table = pq.read_table(self.parquet_file)
            urls = table.column("URL ").to_pylist()[: self.max_images]

            start_time = time.time()
            futures = []
            for url in urls:
                future = executor.submit(self.download_image, url)
                futures.append(future)

            downloaded_count = 0
            for future in futures:
                if future.result():
                    downloaded_count += 1

            self.display_images()

    def display_images(self):
        files = os.listdir(self.output_directory)
        image_files = [
            file for file in files if file.endswith((".jpg", ".jpeg", ".png", ".gif"))
        ]
        for image_file in image_files:
            file_path = os.path.join(self.output_directory, image_file)
            try:
                image = Image.open(file_path)
                image.show()
            except Exception as e:
                print(f"Error displaying image {file_path}: {str(e)}")


parquet_file = "C:/Users/cusat/Desktop/links.parquet"
output_directory = "C:/Users/cusat/Desktop/Output"
downloader = Downloader(parquet_file, output_directory)
downloader.download_images()
