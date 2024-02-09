import pyarrow.parquet as pq
import requests
import os

class Downloader:
    def __init__(self, pq_file: str):
        self.pq_file = pq_file
        self.table = pq.read_table(pq_file)
        # Find column names in the schema and normalize them
        self.urls = self._find_column_names('URL')

    def __getitem__(self, key):
        # Handle single index or slice
        if isinstance(key, int):
            return self._download_image(key)
        elif isinstance(key, slice):
            return [self._download_image(i) for i in range(*key.indices(len(self.urls)))]

    def _find_column_names(self, column_name):
        normalized_column_name = column_name.strip().lower()
        for field in self.table.schema.names:
            if field.strip().lower() == normalized_column_name:
                return self.table.column(field).to_pylist()
        raise KeyError(f'Field "{column_name}" does not exist in schema')

    def _download_image(self, index):
        url = self.urls[index]
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Extract filename from URL
                filename = os.path.basename(url)
                output_directory = os.path.dirname(self.pq_file)
                file_path = os.path.join(output_directory, filename)
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                return file_path
            else:
                print(f"Failed to download image from {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image from {url}: {str(e)}")


parquet_file = "C:/Users/cusat/Desktop/links.parquet"
table = pq.read_table(parquet_file)
print(table.schema)


def download_images(parquet_file, output_directory, max_images=10000):
    downloader = Downloader(parquet_file)
    os.makedirs(output_directory, exist_ok=True)
    downloaded_count = 0

    for i in range(len(downloader.urls)):
        if downloaded_count >= max_images:
            break

    
        try:
            local_path = downloader[i]
            if local_path:
                downloaded_count += 1
        except Exception as e:
            print(f"Error downloading image at index {i}: {str(e)}")


if __name__ == "__main__":
    parquet_file = "C:/Users/cusat/Desktop/links.parquet"
    output_directory = "C:/Users/cusat/Desktop/Output"
    download_images(parquet_file, output_directory)

