import os

class OfflineMedia:
    def __init__(self, download_folder="downloads"):
        self.download_folder = download_folder
        os.makedirs(self.download_folder, exist_ok=True)
