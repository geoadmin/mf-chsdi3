import os
import select
import socket
import re
from struct import pack, unpack

class SphinxClient:

    def __init__(self, host):
        """
        Create a new client object, and fill defaults.
        """
        self._host          =  host                   # searchd host (default is "localhost")
        self._port          = 9312                          # searchd port (default is 9312)
        self._path          = None                          # searchd unix-domain socket path
        self._socket        = None
        self._timeout       = 10

    def Connect(self):
        """
        INTERNAL METHOD, DO NOT CALL. Connects to searchd server.
        """
        if self._socket:
            # we have a socket, but is it still alive?
            sr, sw, _ = select.select([self._socket], [self._socket], [], 0)

            # this is how alive socket should look
            if len(sr) == 0 and len(sw) == 1:
                return self._socket

            # oops, looks like it was closed, lets reopen
            self._socket.close()
            self._socket = None

        try:
            if self._path:
                af = socket.AF_UNIX
                addr = self._path
                desc = self._path
            else:
                af = socket.AF_INET
                addr = (self._host, self._port)
                desc = '%s;%s' % addr
            sock = socket.socket(af, socket.SOCK_STREAM)
            sock.settimeout(self._timeout)
            sock.connect(addr)
        except socket.error as msg:
            if sock:
                sock.close()
            self._error = 'connection to %s failed (%s)' % (desc, msg)
            return

        v = unpack('>L', sock.recv(4))[0]
        if v < 1:
            sock.close()
            self._error = 'expected searchd protocol version, got %s' % v
            return

        # all ok, send my version
        sock.send(pack('>L', 1))
        return sock


if __name__ == '__main__':
    sphinxhost = os.environ.get('SPHINXHOST', 'localhost')
    s = SphinxClient(sphinxhost)
    resp = s.Connect()
    if isinstance(resp, socket.socket):
        print("Connected to Sphinx server {}".format(sphinxhost))
    else:
        print("Cannot connect to Sphinx server {}".format(sphinxhost))
    
