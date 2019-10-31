import pytest
import requests

API_BASE_URL = "https://jsonplaceholder.typicode.com"
SEP = "/"
POSTS = "posts"


def list(type):
    URL = API_BASE_URL + SEP + type

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    return r.json()


def item(type, id):
    URL = API_BASE_URL + SEP + type + SEP + str(id)

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    return r.json()


def delete(type, id):
    URL = API_BASE_URL + SEP + type + str(id)

    # sending get request and saving the response as response object
    r = requests.delete(url=URL)

    # extracting data in json format
    return r.json()


def post_list():
    return list(POSTS)


def post_get(id):
    return item(POSTS, id)


def post_delete(id):
    return delete(POSTS, id)

def test_crud():
    list_posts = post_list()

    print(len(list_posts))

    print(type(list_posts[1]))

    item_id = list_posts[1]['id']

    print(item_id)

    item_post = post_get(item_id)

    print(item_post)

    post_delete_result = post_delete(item_id)

    print(post_delete_result)

    item_post = post_get(item_id)

    print(item_post)


# print([{ id: vv['id'], ['userId']) for v in list(POSTS)])

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def prod(a, b):
#     return a * b

# def test_answer():
#     assert add(2, 4) == 6
#     assert sub(2, 4) == -2
#     assert prod(2, 4) == 8
