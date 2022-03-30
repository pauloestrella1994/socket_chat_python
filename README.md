# Simple Client/Server chat example 
Welcome to client/server chat room!

To run this code, make sure you're in a Linux/Unix based system and have python installed
(this project was made in a Ubuntu 20.04 with python 3.9.5). You can install python following
the tutorial on [official webapge](https://www.python.org/downloads/source/). 

If you want to some easy-to-manage tool, take a look at [Pyenv](https://github.com/pyenv/pyenv)

With a Linux system, a python installed and all this files unziped in your local machine,
we can start the project.

This is a simple chat room system, with multiple clients and a server. Server running will
listen all the new connections and will print their address, and, if someone is disconnected,
the server will broadcast a message for all the clients showing who get disconnected. Also, 
when a new client is connected, the server will broadcast a message to all the clients connected
and he's messages as well.

To run the server and start to listen clients, open a terminal and run:

```
python server.py
```

To disconnect the server, run Ctrl + C (KeyboardInterrupt), so the server will broadcast a message
for all clients showing that the server is out.

To run a new client, open a new terminal and run:

```
python client.py
```

it will request a nickname for your new client, after that, we can start sending messages. For a test,
its necessary at least two clients, just because the server don't print the messages of any clients, 
he's just fowarding the messages to all connected clients. To disconnect the client, run Ctrl + C
(KeyboardInterrupt), and the server, and the other clients will know that you are disconnected.
