#!/usr/bin/env python
import subprocess


class Blink:

    def on(self):
        self.cmd('--on')

    def off(self):
        self.cmd('--off')

    def saveRGB(self, r, g, b, pos):
        r = getInt(r)
        g = getInt(g)
        b = getInt(b)
        pos = getInt(pos)

        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            self.cmd('--savergb %d,%d,%d,%d' % (r, g, b, pos))


    def rgb(self, r, g, b):
        r = getInt(r)
        g = getInt(g)
        b = getInt(b)

        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            self.cmd('--rgb %d,%d,%d' % (r, g, b))

    def random(self, numtimes):
        numtimes = getInt(numtimes)

        self.cmd('--random %d' % numtimes)


    def cmd(self, cmd):
        print 'Command: ' + cmd
        code = subprocess.call(['blink1-tool ' + cmd], shell=True)
        return code


    def __init__(self):
        pass

def getInt(i):
        if not isinstance(i, int):
            return int(i)
        return i

def main():
    x = Blink()
    for i in range(0, 16):
        r = 0
        g = 0
        b = 0
        if i in range (0, 2):
            r = 255
        elif i in range (4, 6):
            g = 255
        elif i in range (8, 10):
            b = 255
        elif i in range (12, 14):
            r = 255
            b = 255
        x.saveRGB(r, g, b, i)
    print 'rgb saved'


if __name__ == '__main__':
    main()
