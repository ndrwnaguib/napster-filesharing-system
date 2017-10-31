# coding=utf-8
"""
-----------------------------------------------------------------------------------------------------------
| This project is GPL v3 licensed. Refer to https://www.gnu.org/licenses/gpl-3.0.en.html for more details |
| Author: Andrew Nagyeb                                                                                   |
| Repository: https://github.com/andrewnagyeb                                                             |
-----------------------------------------------------------------------------------------------------------
"""
import datetime
import time
from os import *
from indexing_server.server import *  # -
from peer.peer import *
from validation import *

decision = raw_input("1 - Run Indexing Server\n"
                     "2 - Run Peer\n"
                     "Please select whichever you want.\n")
if decision == "1":
    HOST = raw_input("Please enter the IP of the server in this format XXX.XXX.XXX.XXX. Enter 0 to run as localhost\n")
    PORT = raw_input("Please enter the port number of which the server is going to listen to.\n")
    PORT_VALIDATION = validate_port(PORT)
    valid_boolean, valid_host, valid_port = validate_ip_port(PORT, HOST)
    if valid_boolean:
        server = Server(valid_port, valid_host)
        server.run()
    else:
        print "Invalid configurations for the server."

elif decision == "2":
    print "Welcome Client.\n"
    PORT = input("Please enter server's port number\n")
    HOST = raw_input(
        "Please enter servers IP number in the following format XXX.XXX.XXX.XXX and 0 for localhost\n")
    valid_boolean, valid_host, valid_port = validate_ip_port(PORT, HOST)
    if valid_boolean:
        choice = raw_input("1 - Search for a filename and download it.\n"
                           "2 - Register to the indexing server.\n")
        if choice == "1":
            filename = raw_input("Please enter filename you want to search for.\n")
            if len(filename) != 0:
                peer = Peer(0, "", valid_port,
                            valid_host)  # We don't have to set port or host for peer as it is not going to listen
                file_data = peer.search(filename, valid_host, valid_port)
                download_it = show_result(file_data, filename)
                if download_it:
                    peer.download_file([DOWNLOAD, file_data[1]['shared_files_path'], filename],
                                       file_data[1]['peer_host'], file_data[1]['peer_port'])
                else:
                    print "Okay thank you for using our system."
            else:
                print "You cannot search for an empty string."
        elif choice == "2":
            PEER_PORT = input("Please enter your port number\n")
            PEER_HOST = raw_input(
                "Please your IP number in the following format XXX.XXX.XXX.XXX and 0 for localhost\n")
            valid_boolean, valid_host, valid_port = validate_ip_port(PEER_PORT, PEER_HOST)
            if valid_boolean:
                peer = Peer(valid_port, valid_host, PORT, HOST)
                PATH = raw_input("Please enter the directory path of which you want to share its files.\n")
                try:
                    shared_files = [f for f in listdir(PATH) if path.isfile(path.join(PATH, f))]
                    if len(shared_files) != 0:
                        REGISTERED_SUCCESSFULLY = peer.data_object.register
                        sharing_datetime = datetime.datetime.fromtimestamp(int(time.time())).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        data_object = dict(peer_port=valid_port, peer_host=valid_host, shared_files_path=PATH,
                                           shared_files=shared_files, shared_at=sharing_datetime)
                        if REGISTERED_SUCCESSFULLY:
                            DATA_INSERTED = peer.data_object.append_data(data_object)
                            if DATA_INSERTED:
                                print "Congratulations you have been registered successfully.\n" \
                                      "[*] You will now be put to the listening state.\n" \
                                      "[*] Started listening on", valid_host, ":", valid_port
                                peer.listen()  # block until you receive request
                            else:
                                print "There was an error while inserting your data."
                    else:
                        print "You cannot share empty directory."
                except OSError:
                    print "Invalid Directory Path"
            else:
                print "Invalid configurations."
        else:
            print "Invalid configurations for the server."
    else:
        print "Invalid Choice"
else:
    print "Invalid Choice."
