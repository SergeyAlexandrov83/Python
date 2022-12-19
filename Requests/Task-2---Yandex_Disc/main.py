import requests
import os
from env_var import TOKEN


class YandexDisc:
    def __init__(self, token: str):
        self.HOST = 'https://cloud-api.yandex.net:443'
        self.uri = '/v1/disk/resources/upload'
        self.token = token
        self.headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/json'
        }

    def local_uploader(self, file_path: str, file_name: str):
        url = self.HOST + self.uri
        full_path = os.path.join(os.getcwd(), file_path, file_name)
        params = {'path': f'/{file_name}'}
        upload_url = requests.get(url=url, headers=self.headers, params=params).json()['href']
        response = requests.put(upload_url, headers=self.headers, data=open(full_path, 'rb'))
        if response.status_code in range(200, 203):
            print('File uploading done!')
        else:
            print('Something went wrong!\nError code:', response.status_code)


def main():
    ya_disc = YandexDisc(TOKEN)
    dir_path = input('Input directory path: ')
    for file in os.listdir(dir_path):
        print(file)
    name = input('Input file name: ')
    ya_disc.local_uploader(dir_path, name)


if __name__ == '__main__':
    main()
