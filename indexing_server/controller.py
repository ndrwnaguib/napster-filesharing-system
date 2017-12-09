# coding=utf-8
"""
-----------------------------------------------------------------------------------------------------------
| This project is GPL v3 licensed. Refer to https://www.gnu.org/licenses/gpl-3.0.en.html for more details |
| Author: Andrew Nagyeb                                                                                   |
| Repository: https://github.com/andrewnagyeb                                                             |
-----------------------------------------------------------------------------------------------------------
"""
import pickle
from socket import _socketobject

from constants import *


def search(filename, list_of_files):
    # type: (str, dict) -> (bool,int,str)
    """
    :type list_of_files: dict
    """
    found = False
    return_data = {}
    for key in list_of_files:
        print list_of_files.get(key)['shared_files']
        if filename in list_of_files.get(key)['shared_files']:
            if not found:
                found = True
            return_data[key] = list_of_files.get(key)
    return found, return_data


def register(conn, set_of_lists, peer_data_object=None):
    # type: (_socketobject, dict,dict) -> None
    """
    :param conn:
    :param set_of_lists: dict
    :param peer_data_object: dict
    :return: None
    """
    if peer_data_object is None:
        peer_data_object = {}
    list_id = len(set_of_lists) + 1  # allocate list_id
    set_of_lists[list_id] = peer_data_object  # initialize to empty
    conn.send(pickle.dumps([list_id, True]))  # return ID


def append(conn, request, set_of_lists):
    # type: (_socketobject, list, dict) -> None
    list_id = request[2]  # fetch list_id
    data = request[1]  # fetch data to append
    set_of_lists[list_id] = data  # append it to the list
    conn.send(pickle.dumps(OK))  # return an OK
