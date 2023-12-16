# Reverse Shell

A reverse shell is a shell that is running on one computer but accepts requests and relays the responses to another computer.
So it acts on behalf of another computer remotely.

![image](https://github.com/MichaelBenIsrael/Python-Networking-Reverse-Shell/assets/73841983/ec7887c4-474d-44bf-b7c8-04f0699e937c)



### Dependencies

* [Python](https://www.python.org/) - Programming Language

### Understand Sockets
![image](https://github.com/MichaelBenIsrael/Python-Networking-Reverse-Shell/assets/73841983/a408748c-2080-4d83-b290-d92608263aaf)


### Project's Architecture

![image](https://github.com/MichaelBenIsrael/Python-Networking-Reverse-Shell/assets/73841983/c005d619-0a93-420e-a60b-0cc1ae31b732)


### Run

The server.py file is ready to run. The pc that would run this file will create a socket that will listen to clients at port 9999.
When the server is running an interactive prompt would be avaliable, this prompts supports the following commands:
- list: Prints all the current clients data <br><br>
![image](https://github.com/MichaelBenIsrael/Python-Networking-Multithreaded-Reverse-Shell/assets/73841983/adc465c9-ee53-443c-a0a3-5bf5cb38b02e)
<br><br>
- select: enables to select the client to send commands to<br><br>
![image](https://github.com/MichaelBenIsrael/Python-Networking-Multithreaded-Reverse-Shell/assets/73841983/20b2a620-64b1-40b2-812d-5d2125381a36)

<br><br>
Once the client has been selected, commands can be sent from the server
to execute in the client's computer.
The client can connect to the server by running the client.py from his/her computer.
The only modification that the client.py file needs is the client current IP address
which can be recieved by typing: "ipconfig" in the command prompt. 

