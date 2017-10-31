# Napster file-sharing system

Brief about this project

Peer-to-Peer(P2P) Technologies are being widely used for sharing the data between the servers and the clients. One of the major technology for file sharing that is implemented nowadays is the Napster-Style Peer-to-Peer File Sharing System. The older versions of the systems used to have a single server which stores the files in its directory that are received from the clients. The major drawback of these systems was that if a new file has been created in one of the peers, it must be transferred to the server before another peer can access it, which delays the process of transfer from one peer to another. This can be conquered using the Napster system which allows the peer to peer file transfer.


### System Architecture
* Processor type: Intel &reg; Core&trade; i5-2410 CPU @ 2.30Ghz x 4
* Memory: 7.7 GiB

### System Requirements:
* Python 2.7 environment installed

### Design
Entire project is design using Python 2.7 where I used some network programming concepts such as sockets, multi-threading for establishing connections between peers. Major components of this project are:
* Indexing Server
* Peer _( Which acts as client and a server )_

#### Indexing server
Indexing server indexes the content of all peers _(Which have registered with it)_ using dictionary with a _peer id_ attached to each peer. It provides two funcitons which are **register** and **search** .

### Peer
Major function of the peer: Register and Listen to clients that wants to download (_As a server_). Search for a filename and ask to download it _(As a client)_. Firstly, as a client, user can request a file name to the indexing server. The indexing server returns a peer data whcih shares this file with all of its details. The user then connects to this peer and downloads the file. Secondly, as a server,the peer waits for requests from other peers and sends the requested file when receiving a request. So peers here, act as both the client and the server. This server is different from the central index server which only indexes the files. But, the server functionality of the peer can be used to download the files from its directory. The peer acts a client to download the files from other peers into its directory.

### How-to

