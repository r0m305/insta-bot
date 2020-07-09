cython -3 --embed -o script.c script.py
gcc -Os -I /usr/include/python3.8/ -o script script.c -lpython3.8 -lpthread -lm -lutil -ldl

