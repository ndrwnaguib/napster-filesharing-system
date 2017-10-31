# coding=utf-8
"""
-----------------------------------------------------------------------------------------------------------
| This project is GPL v3 licensed. Refer to https://www.gnu.org/licenses/gpl-3.0.en.html for more details |
| Author: Andrew Nagyeb                                                                                   |
| Repository: https://github.com/andrewnagyeb                                                             |
-----------------------------------------------------------------------------------------------------------
"""
import os


def show_result(result, filename):
    # type: (list, str) -> bool
    if result[0]:
        print "File", filename, "was found. Peer details are:\n"
        print "Peer port:", result[1]['peer_port'], "\n"
        print "Peer host:", result[1]['peer_host'], "\n"
        print "Shared file path:", result[1]['shared_files_path'], "\n"
        print "File shared at:", result[1]['shared_at'], "\n"
        download_it = raw_input("Do you want to download it (Y/N):")
        download_it.lower()
        if download_it == "y":
            return True
        elif download_it == 'n':
            return False
        else:
            print "Invalid Choice"
    else:
        print "File", filename, "was not found!"


def send_file(conn, data):
    file_path = data[1]
    filename = data[2]
    path_to_file = os.path.join(file_path, filename)
    with open(path_to_file, 'rb') as file_to_send:
        for data in file_to_send:
            conn.sendall(data)
    print('Done sending')
    conn.close()
