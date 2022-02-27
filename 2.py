from pprint import pprint

import requests 

token = ""

class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def upload(self, file_path: str):
         upload_url = 'https://dev.yandex.net/disk-polygon/?lang=ru&tld=ru#!/v147disk47resources/GetResourceUploadLink'
         headers = self.get_headers()
         params = {"path": 'disk_file_path', "overwrite": "true"}
         response = requests.get(upload_url, headers=headers, params=params)
         href = self._get_upload_link(disk_file_path='disk_file_path').get("href", "")
         response = requests.put(href, data=open('filename', 'rb'))
         response.raise_for_status()
         if response.status_code == 201:
             print("Success")
         pprint(response.json())
         return response.json()

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'https://dev.yandex.net/disk-polygon/?lang=ru&tld=ru#!/v147disk47resources/GetResourceUploadLink'
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)