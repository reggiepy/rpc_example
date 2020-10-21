# *_*coding:utf-8 *_*
from xmlrpc import client


class Calcultor(client.ServerProxy):
    def __init__(self, host: str = "localhost", port: int = 9000):
        super(Calcultor, self).__init__(f"http://{host}:{port}")


if __name__ == '__main__':
    calcultor = Calcultor()
    out = calcultor.add(1, 2)
    print(out)
    out = calcultor.Calcultor.add(1, 2)
    print(out)
