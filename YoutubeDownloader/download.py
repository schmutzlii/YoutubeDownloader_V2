import os
import concurrent.futures
from pytube import YouTube

class Downloader:
    def __init__(self, download_path, extension):
        self.download_path = download_path
        self.extension = extension

    def download_video(self, url):
        yt = YouTube(url)
        stream = yt.streams.get_by_itag(251)
        downloaded_file_path = stream.download(self.download_path)
        return downloaded_file_path

    def rename_file(self, file_path):
        file_name, _ = os.path.splitext(file_path)
        new_file_path = os.path.join(self.download_path, file_name + self.extension)
        os.rename(file_path, new_file_path)
        return new_file_path

    def file_exists(self, file_path):
        return os.path.exists(file_path)

    def download_and_rename(self, url):
        try:
            video_id = YouTube(url).title
            file_path = os.path.join(self.download_path, video_id + self.extension)

            if self.file_exists(file_path):
                print(f"Track from {file_path} already exists, skipping...")
            else:
                downloaded_path = self.download_video(url)
                if self.file_exists(downloaded_path):
                    #new_file_path = self.rename_file(downloaded_path)
                    #print(f"Downloaded and renamed: {new_file_path}")
                    pass
                else:
                    print(f"Download failed for {url} or file does not exist.")
        except Exception as e:
            print(f"Error processing {url}: {e}")

    def download_all_parallel(self, urls):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.download_and_rename, urls)
