#import the  requests  library
import requests

#getting user id from user_id file
from get_user_id import get_user_id

#import the app_access_token and base_url from constant file
from constant import APP_ACCESS_TOKEN,BASE_URL

#Here is create a function to get the user post id
def get_post_id(insta_username):

    #Here is the code logic
    user_id = get_user_id(insta_username)
    if user_id == None:
        print( 'User does not exist!')
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print ('GET request url : %s' % (request_url))
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print ('There is no recent post of the user!')
            exit()
    else:
        print ('Status code other than 200 received!')
        exit()