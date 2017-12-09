# Napster file-sharing system

Brief about this project

Peer-to-Peer(P2P) Technologies are being widely used for sharing the data between the servers and the clients. One of the major technology for file sharing that is implemented nowadays is the Napster-Style Peer-to-Peer File Sharing System. The older versions of the systems used to have a single server which stores the files in its directory that are received from the clients. The major drawback of these systems was that if a new file has been created in one of the peers, it must be transferred to the server before another peer can access it, which delays the process of transfer from one peer to another. This can be conquered using the Napster system which allows the peer to peer file transfer.


### System Architecture ( Which this project was developed over)
* Processor type: Intel &reg; Core&trade; i5-2410 CPU @ 2.30Ghz x 4
* Memory: 7.7 GiB

### System Requirements:
* Python 2.7 environment installed

### Design
Entire project is designed using Python 2.7 where I used some network programming concepts such as sockets, multi-threading for establishing connections between peers. Major components of this project are:
* Indexing Server
* Peer _( Which acts as client and a server )_

#### Indexing server
Indexing server indexes the content of all peers _(Which have registered with it)_ using dictionary with a _peer id_ attached to each peer. It provides two funcitons which are **register** and **search** .

### Peer
Major function of the peer: Register and Listen to clients that wants to download (_As a server_). Search for a filename and ask to download it _(As a client)_. Firstly, as a client, user can request a file name to the indexing server. The indexing server returns a peer data whcih shares this file with all of its details. The user then connects to this peer and downloads the file. Secondly, as a server,the peer waits for requests from other peers and sends the requested file when receiving a request. So peers here, act as both the client and the server. This server is different from the central index server which only indexes the files. But, the server functionality of the peer can be used to download the files from its directory. The peer acts a client to download the files from other peers into its directory.

### How-to
* Run _main.py_ . Output should look like this:
`````
1 - Run Server
2 - Run Peer
Please select whichever you want.
`````
##### indexing server - How-to
You must run the indexing server first. So you choose "_1_"
```
1
```
```
Please enter the IP of the server in this format XXX.XXX.XXX.XXX. Enter 0 to run as localhost
0
Please enter the port number of which the server is going to listen to.
45000
[*] Started listening on localhost : 45000
```
In the above running example, we choose "_0_" to run as _localhost_ (You can enter your machine IP), and for the listening port we choose _45000_. Now server is waiting(listening) for incoming peers' requests.
 We run _main.py_ one more time to run peer. This time we choose "_2_"
 ##### Peer - How-to
```
1 - Run Server
2 - Run Peer
Please select whichever you want.
2
```
```
Please enter server's port number
45000
```
You have to enter server's port number which it is currently listening to, which is _45000_(check indexing server configurations) in our case.
```
Please enter servers IP number in the following format XXX.XXX.XXX.XXX and 0 for localhost
0
```
We choose "_0_" since we are running on local machine. Next output is:
```
1 - Search for a filename and download it.
2 - Register to the indexing server.
2
```
We chose "_2_" in order to register files to the indexing server(choose "_1_" if you have registered files already).
```
Please enter your port number
25000
Please enter your IP number in the following format XXX.XXX.XXX.XXX and 0 for localhost
0
``` 
We chose a random port (_25000_) as a peer to listen to for incoming requests to download specific files, and "_0_" for localhost
```
Please enter the directory path of which you want to share its files.
/path/to/this/project/peer/testing_files
Congratulations you have been registered successfully.
[*] You will now be put to the listening state.
[*] Started listening on localhost : 25000
```
You are now blocked and waiting for another peers to request files to download. Now let's search for a file.
We run _main.py_ one more time as a peer and we enter same configurations for the server and we get to the following output again. 
_(Case that only one peer has the file)_
```
1 - Search for a filename and download it.
2 - Register to the indexing server.
1
Please enter filename you want to search for.
1.txt
File 1.txt was found in the following one or more peers. Peer/s details are::

Peer port: 25000 

Peer host: localhost 

Shared file path: /path/to/this/project/peer/testing_files 

File shared at: 2017-10-31 20:27:41 

Do you want to download it (Y/N): y
Successfully get the file
connection closed
```
_(Case that one or more peer has the file)_
```
File 6.txt was found in the following one or more peers. Peer/s details are:

Peer ID: 1 

Peer port: 25000 

Peer host: localhost 

File shared at: 2017-12-09 21:11:42 

-------------------------------------
Peer ID: 2 

Peer port: 35000 

Peer host: localhost 

File shared at: 2017-12-09 21:11:53 

-------------------------------------
Do you want to download it (Y/N):
y
Please specify Peer ID
1
Successfully get the file
connection closed
```
Downloaded file should be found in: _/path/to/this/project/peer/downloads/downloaded_1.txt_

For the peer that is running waiting for requests the output is(Which has the actual file):
```
[*] You will now be put to the listening state.
[*] Started listening on localhost : 25000
[*] Got a connection from  127.0.0.1 : 51702
Done sending
```
Hopefully that illustrated how this project runs and overall idea of _Napster File-Sharing System_

### Enhancements
Possible enhancements to this project are:
* Allow editing files for the registered peer.
* Ping the requesting peer to calculate latency.
* Assign the network bandwidth to each peer.
### Issues
Please for any code issues feel free to submit an issue to this repository and I will answer shortly
