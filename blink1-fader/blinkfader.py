from Blink import Blink
import Queue
from time import sleep
import threading

class BlinkFader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.blink = Blink()
        self.blink.off()
        self.daemon = True
        self.queue = Queue.Queue()
        self.history = []
        self.killed = False

    def run(self):
        while not self.killed:
            while not self.queue.empty():
                (r,g,b) = self.queue.get()

                self.blink.rgb(r,g,b, 1500)
                self.history.append((r,g,b))
                sleep(3.5)

                self.blink.rgb(0, 0, 0, 1000)
                sleep(2.5)

            self.addHistoryToQueue()

    def addHistoryToQueue(self):
        for (r,g,b) in self.history:
            self.add(r,g,b)
        sleep(.1)

    def add(self, r, g, b):
        self.queue.put((r,g,b))

    def clear(self):
        while not self.queue.empty():
            self.queue.get()

    def kill(self):
        self.killed = True


def main():
    x = BlinkFader()
    x.start()
    x.add(255,0,0)
    x.add(0,0,255)
    sleep(20)
    print 'adding green'
    x.add(0, 255, 0)
    while True:
        sleep(10)

if __name__ == '__main__':
    main()
