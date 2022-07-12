import requests
from VK import VK_id
from YAD import YaUploader
from pprint import pprint
from PIL import Image  # Для обработки изображения

# from urllib.request import urlopen  # Для открытия изображения по ссылке
token = '...'
token_vk = '...'
id = '...'

if __name__ == '__main__':
    vk = VK_id(token_vk)
    uploader = YaUploader(token)
    dict_url = vk.upload_photo(id)
    count = 0
    for name, url in dict_url.items():
        # print(name,url)
        count += 1
        resp = requests.get(url, stream=True).raw
        img = Image.open(resp)
        img.save(f'{name}.jpg', 'jpeg')
        with open (f'{name}.jpg', 'rb') as f:
            uploader.upload(f'/{name}',f)
        print(f'Фото {count} загружено')
    
   


    