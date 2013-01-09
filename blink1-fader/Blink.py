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


    def rgb(self, r, g, b, time=300):
        r = getInt(r)
        g = getInt(g)
        b = getInt(b)

        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            self.cmd('--rgb %d,%d,%d -m %d' % (r, g, b, time))

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
    """ Will try to return an int from a string or int """
    if not isinstance(i, int):
        return int(i)
    return i
