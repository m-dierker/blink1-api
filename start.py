#!/usr/bin/env python
import subprocess

def main():
    subprocess.call(['screen', '-dmS', 'blink', 'python', 'blink1/manage.py', 'runserver', '0.0.0.0:80'])

if __name__ == '__main__':
    main();
