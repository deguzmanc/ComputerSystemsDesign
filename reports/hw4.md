## Design/implementation ##

1) Implement artificial delay in memoryfs_server.py to model a server/network slow to respond

Modify memoryfs_server.py to support a new command-line argument -delayat COUNT, where COUNT is an integer. Then, in your server code, modify the Get() and Put() implementations such that for every Nth request (N is the COUNT), the server artificially delays by "sleeping" for 10 seconds.

2) Implement at-least-once semantics for memoryfs_client.py

Implement at-least-once semantics for the Get(), Put() and RSM() calls in the client, such that your design is able to recover both from timeouts, and when the server is disconnected/reconnected. 
*FOR FULL CREDIT* make sure your implementation prints out the following error messages (exactly these strings) when these events happen, respectively:

SERVER_TIMED_OUT
SERVER_DISCONNECTED

3) Implement an in-disk key/value store for memoryfs_server.py

In the implementations up to HW#3, the RawBlocks data is stored in main memory - hence, when the process terminates or is killed, the data is gone. In this assignment, you will implement a key/value store in disk that persists over restarts using Python's dbm module https://remusao.github.io/posts/python-dbm-module.html

To this end, modify the server to support two additional command-line arguments: 
-initdbm : an integer flag; 1 initializes the database with zero blocks, 0 does not initialize the database 
-dbmfile : a string that names the file used by dbm in disk 

If the -dbmfile argument is given, you should use the named file as storage. Then, if -initdbm is 1, initialize all blocks with zeroes; otherwise, don't initialize - simply use its contents.

4) Implement a client-side cache for file data blocks read (Get()) in the Read() function in memoryfs_client.py

Extend your memoryfs_client.py to support client-side caching of file data blocks. You should only concern with data blocks in regular files - not directories, not inodes, no free bitmap blocks, etc.

You will implement a simple caching invalidation policy as follows:
  - initialize gencnt to 0, and increment it any time the file is written to, *and* also when it is unlinked
  - when a file is Read(), check first what the gencnt in the inode is, and what the gencnt in the cache is. 
    - If the gencnt match, you may Get() blocks from the cache if they are present in the cache 
    - If the gencnt do not match, invalidate all cache entries for this file inode
    - If the block is not present in the cache, Get() from the server and store in the cache

*FOR FULL CREDIT* make sure your implementation prints out the following status messages to the screen (exactly these strings) when *each* block is found in the cache, and when the cache is invalidate, respectively:

CACHE_HIT
CACHE_INVALIDATED

## Assignment questions ##

Q1) In the code given to you, the Acquire() and Release() calls are placed around operations such as cat and append to ensure they run exclusively in one client at a time. What is one example of a race condition that can happen without the lock? Simulate a race condition in the code (comment out the lock Acquire()/Release() in the cat and append functions, and place sleep statement(s) strategically) to verify, and describe how you did it.

Q2) What happens when you don't store the data in disk using dbm on the server, and terminate/restart the server? 

Q3) What are the changes that were made to the Get() and Put() methods in the client, compared to the HW#3 version of the code?

Q4) At-least-once semantics may at some point give up and return (e.g. perhaps the server is down forever). How would you implement this in the code (you don't need to actually implement; just describe in words)