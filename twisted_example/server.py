# *_*coding:utf-8 *_*
import os
import sys

from twisted.internet import reactor
from twisted.web import server
from twisted.web import xmlrpc

# Thread pool size, default is 10
reactor.suggestThreadPoolSize(10)


class RPCFunctions(xmlrpc.XMLRPC):
    def xmlrpc_add(self, a, b):
        return a + b


class CalcultorResource(xmlrpc.XMLRPC):
    def xmlrpc_add(self, a, b):
        return a + b



def main():
    rpc_function = RPCFunctions(allowNone=True, useDateTime=True)
    rpc_function.putSubHandler("Calcultor", CalcultorResource())
    reactor.listenTCP(9000, server.Site(rpc_function))
    reactor.run()


if __name__ == "__main__":
    main()
