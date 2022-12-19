from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import requests
import json
import time
import tqdm


def full_path(folder_name, file_name):
    fpath = os.path.join(os.getcwd(), folder_name, file_name)
    return fpath


def get_token(file_name):
    # Сначала токены нужно положить в соответствующие файлы
    path = full_path('work_files', file_name)
    with open(path, encoding='utf-8') as file:
        token = file.readline()
    return token


def safe_enter(text):
    enter = input(text)
    if enter.isnumeric():
        enter = int(enter)
    else:
        print('Введена неверная команда!')
        enter = -1
    return enter


def json_data_file(transfer_list):
    data = transfer_list
    path = full_path('json', 'transferred.json')
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.photo_data = {}
        self.albums_data = {}
        self.photo_count = 5
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {
            'access_token': self.token,
            'owner_id': self.id,
            'v': self.version}

    def get_albums_data(self):
        url = 'https://api.vk.com/method/photos.getAlbums'
        self.params.update({
            'need_system': 1
        })
        api = requests.get(url=url, params=self.params)
        data = json.loads(api.text)
        count = data['response']['count']
        print(f'Найдено альбомов: {count}')
        i = 1
        for album in data['response']['items']:
            print(f'{i}. {album["title"]} - {album["size"]} фото в альбоме.')
            self.albums_data[i] = {'album_id': album['id'], 'album_size': album['size']}
            i += 1

    def get_foto_data(self, album_id='profile', offset=0, count=50):
        url = 'https://api.vk.com/method/photos.get'
        self.params.update({
            'album_id': album_id,
            'offset': offset,
            'count': count,
            'photo_sizes': 1,
            'extended': 1,  # Тут могли быть ваши лайки, но их нет :'(
        })
        api = requests.get(url=url, params=self.params)
        data = json.loads(api.text)
        for photo in data['response']['items']:
            max_height = 0
            for size in photo['sizes']:
                if size['height'] > max_height:
                    max_height = size['height']
                    self.photo_data[photo['id']] = {'photo_url': size['url'], 'photo_size': size['type']}


class Transfer:

    def __init__(self, assess_token, transfer_method):
        self.ya_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.files_transfer = []
        self.files_done = {}
        self.token = assess_token
        self.transfer_method = transfer_method
        self.headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def files_names(self, names_container):
        self.files_done = {'file_name': f'{names_container}.jpg',  # Нету лайков у меня...
                           'size': f'{vk.photo_data[names_container]["photo_size"]}'}
        self.files_transfer.append(self.files_done)
        time.sleep(0.1)

    def transfer_logic(self, dir_name):
        if vk.album_num == 0:
            for num in vk.albums_data.keys():
                vk.get_foto_data(vk.albums_data[num]['album_id'])
            pbar = tqdm.tqdm(desc='Progress', total=len(vk.photo_data), ncols=100, ascii=False, colour='green')
            for i in vk.photo_data.keys():
                self.files_names(i)
                self.transfer_method_select(dir_name, i)
                pbar.update(n=1)
        else:
            vk.get_foto_data(vk.albums_data[vk.album_num]['album_id'])
            if vk.photo_count == 0:
                vk.photo_count = vk.albums_data[vk.album_num]['album_size']
            counter = 1
            pbar = tqdm.tqdm(desc='Progress', total=vk.photo_count, ncols=100, ascii=False, colour='green')
            for i in vk.photo_data.keys():
                if counter <= vk.photo_count:
                    self.files_names(i)
                    self.transfer_method_select(dir_name, i)
                    counter += 1
                    pbar.update(n=1)
                else:
                    break

    def transfer_method_select(self, directory, names):
        if self.transfer_method == 1:
            return self.ya_transfer(directory, names)
        if self.transfer_method == 2:
            return self.gl_transfer(directory, names)
        if self.transfer_method == 3:
            return self.ld_transfer(directory, names)

    def ya_transfer(self, ya_dir, names_container):
        file_path = f'{ya_dir}/{names_container}.jpg'
        res = requests.get(f'{self.ya_url}/upload?path={file_path}&overwrite=True',
                           headers=self.headers).json()
        file = requests.get(vk.photo_data[names_container]["photo_url"])
        try:
            requests.put(res['href'], files={'file': file.content})
        except KeyError:
            print(res)

    @staticmethod
    def gl_transfer(gl_dir, names_container):
        api = requests.get(vk.photo_data[names_container]["photo_url"])
        with open(f'{names_container}.jpg', "wb") as file:
            file.write(api.content)
        folders = drive.ListFile(
            {
                'q': "title='" + gl_dir + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"
            }).GetList()
        for gl_folder in folders:
            if folder['title'] == gl_dir:
                file_gl = drive.CreateFile({'parents': [{'id': gl_folder['id']}]})
                file_gl.SetContentFile(f'{names_container}.jpg')
                file_gl.Upload()
        os.remove(f'{names_container}.jpg')

    @staticmethod
    def ld_transfer(ld_dir, names_container):
        api = requests.get(vk.photo_data[names_container]["photo_url"])
        with open(full_path(ld_dir, f'{[names_container]}.jpg'), "wb") as file:
            file.write(api.content)


# vk_id = int(input('Введите ваш VK id: '))
vk_id = get_token('id.txt')
vk_access_token = get_token('vk_token.txt')
vk = VK(vk_access_token, vk_id)
vk.get_albums_data()
vk.get_foto_data()
while True:
    vk.album_num = safe_enter('Введите номер альбома для трансфера (введите "0" если хотите выбрать все альбомы): ')
    if vk.album_num < 0:
        break
    elif vk.album_num in vk.albums_data.keys():
        vk.photo_count = safe_enter('Введите количество фото для скачивания ("0" - для выбора всех фото): ')
        if vk.photo_count < 0:
            print('Установленно значение по умолчанию - 5 фото.')
    elif vk.album_num == 0:
        print('Будут скачаны все фото!')
        vk.photo_count = 0
    print('1. Сохранить на Я.Диск')
    print('2. Сохранить на Google.Диск (в следующих обновлениях!)')
    print('3. Локальное сохранение')
    disc_select = safe_enter('Выберите куда направить фото: ')
    if disc_select == 1:
        # ya_token = str(input('Введите ваш токен ЯндексДиск: '))
        ya_token = get_token('ya_token.txt')
        ya_disc = Transfer(ya_token, transfer_method=1)
        img_dir = input('Введите название папки для сохранения фото: ')
        requests.put(f'{ya_disc.ya_url}?path={img_dir}', headers=ya_disc.headers)
        ya_disc.transfer_logic(img_dir)
        json_data_file(ya_disc.files_transfer)
    elif disc_select == 2:
        # gl_token = str(input('Введите ваш токен Google.Disc: '))
        drive = GoogleDrive(GoogleAuth())
        gl_disc = Transfer(None, transfer_method=2)
        img_dir = input('Введите название папки для сохранения фото: ')
        folder = drive.CreateFile({'title': img_dir, 'mimeType': 'application/vnd.google-apps.folder'})
        folder.Upload()
        gl_disc.transfer_logic(img_dir)
        json_data_file(gl_disc.files_transfer)
    elif disc_select == 3:
        ld_token = None
        local_disc = Transfer(ld_token, transfer_method=3)
        img_dir = input('Введите название папки для сохранения фото: ')
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)
        local_disc.transfer_logic(img_dir)
        json_data_file(local_disc.files_transfer)
    else:
        break
    break
