# coding=utf-8
"""
-----------------------------------------------------------------------------------------------------------
| This project is GPL v3 licensed. Refer to https://www.gnu.org/licenses/gpl-3.0.en.html for more details |
| Author: Andrew Nagyeb                                                                                   |
| Repository: https://github.com/andrewnagyeb                                                             |
-----------------------------------------------------------------------------------------------------------
"""
from data_object import *
from helper import *


class Peer:
    def __init__(self, port, host, server_port, server_host):
        # type: (int, str) -> None
        self.host = host  # this machine
        self.port = port  # port it will listen to
        self.sock = socket()  # socket for incoming calls
        self.sock.bind((self.host, self.port))  # bind socket to an address
        self.sock.listen(2)  # max num connections
        self.data_object = DataObject(server_host, server_port)

    def search(self, filename, host, port):
        result = self.send_receive([SEARCH, filename], host, port)
        return result

    def download_file(self, message, host, port):
        s = socket()
        s.connect((host, port))  # connect to server
        s.send(pickle.dumps(message))  # send some data
        downloads_dir_path = os.path.join(os.getcwd(),
                                          'peer')  # If you want to change it. Change the folder actual name
        filename = message[2]  # requested filename from the server
        with open(os.path.join(os.path.join(downloads_dir_path, 'downloads'), "downloaded_" + filename),
                  'wb') as file_to_write:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                file_to_write.write(data)
            file_to_write.close()
        s.close()
        print('Successfully get the file')
        print('connection closed')

    @staticmethod
    def send_receive(message, host, port):
        # type: (list) -> str or int
        sock = socket()  # create a socket
        sock.connect((host, port))  # connect to server
        sock.send(pickle.dumps(message))  # send some data
        result = pickle.loads(sock.recv(1048))  # receive the response
        sock.close()  # close the connection
        return result

    @staticmethod
    def send_to(host, port, data):
        # type: (str, str, list) -> None
        """
        :rtype: None
        """
        sock = socket()
        sock.connect((host, port))  # connect to server (blocking call)
        sock.send(pickle.dumps(data))  # send some data
        sock.close()

    def listen(self):
        while True:
            (conn, addr) = self.sock.accept()
            print "[*] Got a connection from ", addr[0], ":", addr[1]
            data = conn.recv(1024)
            request = pickle.loads(data)  # unwrap the request
            if request[0] == DOWNLOAD:
                send_file(conn, request)
