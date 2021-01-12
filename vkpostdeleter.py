import vk_api
import PySimpleGUI as sg


class VkPostDeleter:
    logged_in = bool
    vk_session = ''
    vk = ''

    def __init__(self):
        self.logged_in = False

    def login(self, login, password):
        self.vk_session = vk_api.VkApi(login, password, auth_handler=handler)
        self.vk_session.auth()
        self.vk = self.vk_session.get_api()
        self.logged_in = True

    def delete_with_offset(self, offset):
        posts = self.vk.wall.get(count=100, offset=offset)['items']
        while posts:
            for post in posts:
                print(post['id'])
                self.vk.wall.delete(post_id=post['id'])
            posts = self.vk.wall.get(count=100, offset=offset)['items']


def handler():
    code = sg.popup_get_text('Please input the code from the message', '2 factor authentication')
    return code, False

