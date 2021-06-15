import socket
import pymsgbox
import time

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

while True:
    time.sleep(10)
    check = is_connected()
    if check != True:
        pymsgbox.alert('Disconnected', 'Internet_status', button='ok', timeout=5000)
        while True:
            check = is_connected()
            time.sleep(2)

            if check == True:
                pymsgbox.alert('Connected', 'Internet_status', button='ok',timeout=10000)
                break
