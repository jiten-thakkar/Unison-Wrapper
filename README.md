Unison-Wrapper
==============

A Unison wrapper in PyQt4

This is a very simple wrapper for [Unison File Synchronizer](http://www.cis.upenn.edu/~bcpierce/unison/)
Here sockets are used for file transfer.

It has two parts:
1: servers code
Shell file to start the server

2: Client App with GUI
Background process managing the sync to the master.
UI shows the contents of the synced folder.
Client application is built with Python Qt.

Document for usage is in [doc](../master/Doc/) folder
