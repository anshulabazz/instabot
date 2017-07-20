#import requests libarary
import requests
#we import base url or app access token form constant.py file
from constant import BASE_URL,APP_ACCESS_TOKEN
#Create a function of user getting information itself
def self_info():
    #here is the logic and code to get user information itself
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print('GET request url : %s' % (request_url))
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print ('Username: %s' % (user_info['data']['username']))
            print ('No. of followers: %s' % (user_info['data']['counts']['followed_by']))
            print ('No. of people you are following: %s' % (user_info['data']['counts']['follows']))
            print( 'No. of posts: %s' % (user_info['data']['counts']['media']))
        else:
            print ('User does not exist!')
    else:
        print ('Status code other than 200 received!')