#!/usr/bin/env python
import subprocess

def main():
    subprocess.call(['screen -dmS blink /home/pi/blink1-api/ENV/bin/python /home/pi/blink1-api/blink1/manage.py runserver 0.0.0.0:80'], shell=True)

if __name__ == '__main__':
    main();
