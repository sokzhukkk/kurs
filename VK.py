import requests
from pprint import pprint
import datetime
class VK_id:
    def __init__(self, token_vk):
        self.token_vk = token_vk

    def get_photo(self, id):
        URL = 'https://api.vk.com/method/photos.get'
        # token_vk = self.token_vk
        params = {
            'owner_id': id,
            'album_id': 'profile',
            'extended' : 1,
            'access_token': self.token_vk,
            'v': '5.131'
        }
        res = requests.get(URL, params = params)
        return res

    def upload_photo(self, id):
        res = self.get_photo(id)
        list_photo = res.json()['response']['items']
        list_photo_info = []
        dict_url = {}
        for photo in list_photo:
            for sizes in photo['sizes']:
                size = sizes['type']
                url = sizes['url']

            inf = {"file_name": f"{photo['likes']['count']}_{datetime.date.today()}.jpg", "size": size}
            dict_url[inf["file_name"]] = url
            list_photo_info.append(inf)
        # pprint(dict_url)
        pprint(list_photo_info)
        return dict_url
            