# *** this is my main file.***

APP_ACCESS_TOKEN = ' 2121110795.f566e63.45b3d45844144983bd2217db985ca244'
BASE_URL = 'https://api.instagram.com/v1/'
import requests
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

#*** here we import the functions and call them where required..***

from self_info import self_info
from get_user_info import get_user_info
from get_user_id import get_user_id
from get_post_id import  get_post_id
from like_a_post import  like_a_post
from get_user_post import get_user_post
from post_a_comment import  post_a_comment
from delete_neg_comment import  delete_negative_comment
from  get_own_post import get_own_post


# *** here we define the fuction stat_bot in which we have provided the choices.***

def start_bot():
    while True:

        print '\n'
        # *** here this will print the welcome message. ***
        print 'Hey! Welcome to instaBot!'
        # *** thus will provide the menu options for the user.***
        print 'Here are your menu options:'
        # *** this will give the user his own post.***
        print "1.Get your own details\n"
        # *** this will provide the user details with username.***
        print "2.Get details of a user by username\n"
        # ***this will give you your own post.***
        print "3.Get your own recent post\n"
        # *** this will provide the recent post of the user by username.***
        print "4.Get the recent post of a user by username\n"
        # *** this will give you the list of the user who had liked your post.***
        print "5.Get a list of people who have liked the recent post of a user\n"
        # ***
        print "6.Like the recent post of a user\n"
        # *** this will give you the list of comments of the user on the recent post.***
        print "7.Get a list of comments on the recent post of a user\n"
        # here we will make our comment on the recent post of the user.***
        print "8.Make a comment on the recent post of a user\n"
        #this will delete the negative comments from the recent post of the user.***
        print "9.Delete negative comments from the recent post of a user\n"
        # *** here we exit the program. ***
        print "10.Exit"

        choice = raw_input("Enter you choice: ")
        if choice == "1":
            self_info()
        elif choice == "2":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice=="5":
           insta_username = raw_input("Enter the username of the user: ")
           get_like_list(insta_username)
        elif choice=="6":
           insta_username = raw_input("Enter the username of the user: ")
           like_a_post(insta_username)
        elif choice=="7":
           insta_username = raw_input("Enter the username of the user: ")
           get_comment_list(insta_username)
        elif choice=="8":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="9":
           insta_username = raw_input("Enter the username of the user: ")
           delete_negative_comment(insta_username)
        elif choice == "10":
            exit()
        else:
            print "wrong choice"

start_bot()

