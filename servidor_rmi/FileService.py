import os
import Pyro5.api

@Pyro5.api.expose
class FileService:
    def list_files(self, directory_path):
        try:
            return os.listdir(directory_path)
        except Exception as e:
            return str(e)
    
    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            return str(e)
    
    def get_file_size(self, file_path):
        try:
            return os.path.getsize(file_path)
        except Exception as e:
            return str(e)
    
    def download_file(self, file_path, start, length):
        try:
            with open(file_path, 'rb') as file:
                file.seek(start)
                return file.read(length)
        except Exception as e:
            return str(e)
