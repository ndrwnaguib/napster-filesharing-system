# coding=utf-8
"""
-----------------------------------------------------------------------------------------------------------
| This project is GPL v3 licensed. Refer to https://www.gnu.org/licenses/gpl-3.0.en.html for more details |
| Author: Andrew Nagyeb                                                                                   |
| Repository: https://github.com/andrewnagyeb                                                             |
-----------------------------------------------------------------------------------------------------------
"""
from socket import *
from threading import *

from indexing_server.controller import *


class Server:
    def __init__(self, port=PORT, host=HOST, max_num_connections=5):
        self.host = host  # this machine
        self.semaphore = Semaphore(max_num_connections)  # Handling threads synchronization for critical sections.
        self.port = int(port)  # the port it will listen to
        self.sock = socket()  # socket for incoming calls
        self.sock.bind((self.host, self.port))  # bind socket to an address
        self.sock.listen(max_num_connections)  # max num of connections
        self.setOfLists = {}  # init: no lists to manage
        print "[*] Started listening on", self.host, ":", self.port

    def run(self):
        while True:
            (conn, addr) = self.sock.accept()  # accept incoming call
            print "[*] Got a connection from ", addr[0], ":", addr[1]
            data = conn.recv(1024)  # fetch data from peer
            request = pickle.loads(data)  # unwrap the request
            print "[*] Request after unwrap", request
            if request[0] == REGISTER:  # create a list
                self.semaphore.acquire()
                register(conn, self.setOfLists)
                self.semaphore.release()

            elif request[0] == APPEND:  # append request
                self.semaphore.acquire()
                append(conn, request, self.setOfLists)
                self.semaphore.release()

            elif request[0] == GETVALUE:  # read request
                list_id = request[1]  # fetch list_id
                result = self.setOfLists[list_id]  # get the elements
                conn.send(pickle.dumps(result))  # return the list
            # -
            elif request[0] == STOP:  # request to stop
                print self.setOfLists
                conn.close()  # close the connection  #-
                break  # -
            elif request[0] == SEARCH:
                self.semaphore.acquire()
                found_boolean, file_object = search(request[1], self.setOfLists)
                if found_boolean:
                    conn.send(pickle.dumps([found_boolean, file_object]))
                else:
                    conn.send(pickle.dumps([found_boolean]))
                self.semaphore.release()
