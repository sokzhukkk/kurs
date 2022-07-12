import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    
    def new_folder(self):
        headers = self.get_headers()
        params = {'path': '/photo'}
        path_new_folder = requests.put('https://cloud-api.yandex.net/v1/disk/resources',params = params, headers = headers)
        return '/photo'

    def _get_upload_link(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        new_path = f'{self.new_folder()+path}'
        params = {'path': new_path, 'overwrite': True}
        response = requests.get(url, params = params, headers = headers)
        return response.json().get('href')

    def upload(self, path, path_to_file):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        resp = requests.put(upload_link, path_to_file, headers = headers)
        resp.raise_for_status() # ???
        if resp.status_code == 201: 
            print('Success')