import os
import pytest
from downloader import Downloader, download_images

def test_Downloader():
    parquet_file = "test_data/links.parquet"  
    downloader = Downloader(parquet_file)
    assert len(downloader.urls) > 0

def test_download_images():
    parquet_file = "test_data/links.parquet"  
    output_directory = "test_output"  
    max_images = 20 
    download_images(parquet_file, output_directory, max_images)
    assert os.path.isdir(output_directory)
    assert len(os.listdir(output_directory)) == max_images


if __name__ == "__main__":
    pytest.main([__file__])