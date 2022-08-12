# Client Chat

A simple Python program to demonstrate client-server interaction. 

By default the server is started on 127.0.0.1 (localhost) on port 9001.

## How to Run

1. Open 2 instances of your OS terminal. One instance will run server.py and the other will run client.py

2. Make sure you have Python installed on your system. If not, go here: https://www.python.org/downloads/

3. First run server.py to get it connected to localhost and port 9001.
![startserver](https://user-images.githubusercontent.com/62896013/184407307-2ae6ba68-e9e0-477b-8e8e-fa5782f1a329.png)

4. Then run client.py to connect to the server. 
![startclient](https://user-images.githubusercontent.com/62896013/184407416-105bc72c-5538-4cb0-b441-91d7a75d59b4.png)

5. The server will indicate the client's connection by displaying the corresponding IP address and port number. 

6. The programs "take turns" communicating with each other. The ">" character indicates the respective instance's own text (i.e. any text following a ">" is stuff that was typed on that particular terminal instance). 

7. Type "/q" into any instance to close both the client and server. 

![chatexample](https://user-images.githubusercontent.com/62896013/184409066-94e762bd-e56e-4f62-8f74-a558007ee6c1.png)
