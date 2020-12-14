# *_*coding:utf-8 *_*

from xmlrpc.client import ServerProxy

if __name__ == '__main__':
    server = ServerProxy("http://localhost:9999")  # 初始化服务器
    print(server.get_string("cloudox"))  # 调用函数1并传参
    print(server.add(8, 8))  # 调用函数2并传参
    print(server.print("fasfd"))  # 调用函数2并传参
