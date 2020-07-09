╻┏┓╻┏━┓╺┳╸┏━┓┏┓ ┏━┓╺┳╸
┃┃┗┫┗━┓ ┃ ┣━┫┣┻┓┃ ┃ ┃
╹╹ ╹┗━┛ ╹ ╹ ╹┗━┛┗━┛ ╹ 
By r0m305

The original project was a python script, which i thereafter converted to a C script with cython as follows:
  cython -3 --embedd -o instabot.c Instabot.py
I then compiled the instabot.c script using gcc on kali linux 2020.1 as follows:
  gcc -Os -I /usr/include/python3.8/ -o instabot instabot.c -lpython3.8 -lpthread -lm -lutil -ldl
The executable is already compiled for you, so you just have to run it
Run the instabot executable as follows:
  sudo chmod +x instabot
  sudo ./instabot
