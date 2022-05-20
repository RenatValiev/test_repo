import os
from threading import Thread
import shutil
import requests

USERS_URL = 'https://randomuser.me/api'
CATS_URL = 'https://catfact.ninja/fact'


def process_3_users(first_user_index: int, users: list):
    for user_index in range(first_user_index, first_user_index + 3):
        user = users[user_index]
        os.mkdir(f'user_data/{user_index}')

        user_data = f'gender: {user["gender"]}\ntitle: {user["name"]["title"]}\n' \
                    f'first name: {user["name"]["first"]}\nlast name: {user["name"]["last"]}'
        with open(f'user_data/{user_index}/user_info.txt', 'w', encoding='utf8') as file:
            file.write(user_data)

        cat_fact_json = requests.get(CATS_URL).json()
        cat_fact = f'cat fact: {cat_fact_json["fact"]}\nlength: {cat_fact_json["length"]}'
        with open(f'user_data/{user_index}/cat_fact.txt', 'w', encoding='utf8') as file:
            file.write(cat_fact)

        user_pic_url = user['picture']['large']
        user_pic = requests.get(user_pic_url).content
        with open(f'user_data/{user_index}/user_photo.jpg', 'wb') as file:
            file.write(user_pic)


def make_threads():
    try:
        os.mkdir('user_data')
    except FileExistsError:
        shutil.rmtree('user_data')
        os.mkdir('user_data')
    users = requests.get(USERS_URL, params={'results': 12}).json()['results']
    threads = [Thread(target=process_3_users, args=(i, users)) for i in range(0, 10, 3)]
    for thread in threads:
        thread.start()


def main():
    make_threads()


if __name__ == '__main__':
    main()