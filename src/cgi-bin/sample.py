#!/usr/bin/python3
#-*- coding: utf-8 -*-

import cgi
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import client as cl

storage = cgi.FieldStorage()
print('Status: 200 OK')
print('Content-Type: text/html\n')

ip = storage.getvalue('ip')
text = storage.getvalue('text')
speed = float(storage.getvalue('speed'))
emotion = storage.getvalue('emotion')


if '\n' in text:
    text = text.replace('\r\n', '').replace('\n', '')

print(ip, text, speed, emotion)
t = cl.say_text(ip, 22222, text, speed, emotion)
m = cl.make_speech_motion(t, speed)
cl.play_motion(ip, 22222, m)
