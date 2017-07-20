#now we import a requests libraray
import requests

#now we import base url and app access token
from constant import APP_ACCESS_TOKEN,BASE_URL


#here we create a function to get a user id and username
def get_user_id(insta_username):

#now we create a logic to  get  the  user id
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print( 'GET request url : %s' % (request_url))
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print( 'Status code other than 200 received!')
        exit()