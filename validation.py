# coding=utf-8
"""
-----------------------------------------------------------------------------------------------------------
| This project is GPL v3 licensed. Refer to https://www.gnu.org/licenses/gpl-3.0.en.html for more details |
| Author: Andrew Nagyeb                                                                                   |
| Repository: https://github.com/andrewnagyeb                                                             |
-----------------------------------------------------------------------------------------------------------
"""


def validate_ip(ip):
    # type: (str) -> bool
    for i in ip:
        try:
            int(i)
        except ValueError:
            return False
    return True


def validate_port(port):
    # type: (str) -> bool
    try:
        int(port)
    except ValueError:
        return False
    return True


def validate_ip_port(PORT, HOST):
    RETURN_HOST = HOST
    RETURN_PORT = PORT
    IP_VALIDATION = False
    PORT_VALIDATION = False
    if HOST == "0":
        IP_VALIDATION = True
        RETURN_HOST = "localhost"
    else:
        IP_VALIDATION = validate_ip(HOST)
    PORT_VALIDATION = validate_port(PORT)
    if IP_VALIDATION and PORT_VALIDATION:
        return True, RETURN_HOST, RETURN_PORT
    else:
        return False, None, None
