import requests
from constant import APP_ACCESS_TOKEN,BASE_URL
from get_post_id import get_post_id

def get_like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + ''
                              'media/%s/comment') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print('POST request url : %s' % (request_url))
    like_list = requests.get(request_url).json()
    if like_list['meta']['code'] == 200:
        print("like_list")
    else:
        print("not found")