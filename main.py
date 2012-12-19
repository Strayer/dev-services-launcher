#!/usr/bin/python3
# coding=utf-8
import os
from services import Nginx, PHP, MongoDB
import tools
import settings

nginx = Nginx()
php = PHP(nginx.get_php_upstream())
mongodb = MongoDB()

if settings.START_PHP:
    print("PHP version: {}".format(php))
if settings.START_NGINX:
    print("Nginx version: {}".format(nginx))
if settings.START_MONGODB:
    print("MongoDB version: {}".format(mongodb))

print('')

stop_execution = False

if settings.START_PHP:
    print("Starting PHP ({} instances)".format(len(php.addresses)))
    php.start()
if settings.START_NGINX:
    print("Starting Nginx")
    nginx.start()
if settings.START_NGINX:
    print("Starting MongoDB")
    mongodb.start()

print("")
print("Menu:")
print("(STRG+c) or (q) to quit")
if settings.START_NGINX:
    print("(r) to reload nginx config")
if settings.START_PHP:
    print("(p) to restart php processes")
print("")

while True:
    char = tools.getch()

    if char == b"\x03" or char == b"q":
        break
    elif char == b"r" and settings.START_NGINX:
        print("Reloading nginx config... ",end="")
        nginx.reload_config()
        print("done")
    elif char == b"p" and settings.START_PHP:
        print("Restarting php processes... ",end="")
        php.stop()
        php.start()
        print("done")

print("Stopping processes...")
if settings.START_NGINX:
    nginx.stop()
if settings.START_PHP:
    php.stop()
if settings.START_MONGODB:
    mongodb.stop()
