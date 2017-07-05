from delete_negative_comment import delete_negative_comment
from post_a_comment import post_a_comment
from like_user_post import like_a_post
from get_user_info import get_user_info
from self_info import self_info
from get_own_post import get_own_post
from get_user_post import get_users_post
from get_comment_list import get_comment_list
from get_like_list import get_like_list
from like_user_post import like_a_post
def start_bot():
    while True:
        print ('\n')
        print ('Hey! Welcome to instaBot!')
        print( 'Here are your menu options:')
        print ("a.Get your own details\n")
        print ("b.Get details of a user by username\n")
        print ("c.Get your own recent post\n")
        print ("d.Get the recent post of a user by username\n")
        print ("e.Get a list of people who have liked the recent post of a user\n")
        print ("f.Like the recent post of a user\n")
        print ("g.Get a list of comments on the recent post of a user\n")
        print ("h.Make a comment on the recent post of a user\n")
        print ("i.Delete negative comments from the recent post of a user\n")
        print ("j.Exit")

        choice =input("Enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = input("Enter the username of the user: ")
            get_users_post(insta_username)
        elif choice=="e":
           insta_username = input("Enter the username of the user: ")
           get_like_list(insta_username)
        elif choice=="f":
           insta_username = input("Enter the username of the user: ")
           like_a_post()(insta_username)
        elif choice=="g":
           insta_username =input("Enter the username of the user: ")
           get_comment_list(insta_username)
        elif choice=="h":
           insta_username = input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="i":
           insta_username = input("Enter the username of the user: ")
           delete_negative_comment(insta_username)
        elif choice == "j":
            exit()
        else:
            print ("wrong choice")