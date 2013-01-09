import zmq
import re

""" This manages the sockets """
class BlinkFadeManager:
    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.PAIR)
        socket.bind("tcp://127.0.0.1:6969")

        while True:
            msg = socket.recv()
            print "> " + msg
            self.parseMsg(msg)


    def parseMsg(self, msg):
        match = re.search(r'(\w+)\|(\w*)', msg)
        if match:
            cmd = match.group(1)
            args = match.group(2)

            if cmd == '':
                pass
        else:
            print "Invalid Command: " + msg

    def __init__(self):
        self.fader = BlinkFader()
        self.addStartupSequence()



def main():
    x = BlinkFadeManager()
    x.run()

if __name__ == '__main__':
    main()
