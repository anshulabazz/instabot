import requests
from constant import BASE_URL, APP_ACCESS_TOKEN
from get_user_post import get_users_post
def like_a_post(insta_username):
  post_id = get_users_post(insta_username)
  # print media_id
  request_url = (BASE_URL + ''
                            'media/%s/likes') % (post_id)
  payload = {"access_token": APP_ACCESS_TOKEN}
  print( 'POST request url : %s' % (request_url))
  post_a_like = requests.post(request_url, payload).json()

  if post_a_like['meta']['code'] == 200:
    print ("Post Liked Successfully")
  else:
    print ("Unable to like post")