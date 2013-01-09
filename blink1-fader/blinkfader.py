import zmq

class BlinkFader:
    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.PAIR)
        socket.bind("tcp://127.0.0.1:6969")

        while True:
            msg = socket.recv()
            print "> " + msg
            self.parseMsg(msg)

    def __init__(self):
        pass


def main():
    x = BlinkFader()
    x.run()

if __name__ == '__main__':
    main()
