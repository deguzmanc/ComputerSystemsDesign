## Final report guidelines

1. Introduction and problem statement
   Describe in your own words what your project accomplishes, and motivate the decisions made

In this project, we modifyied a filesystem that works with client server over xmlrpc to support more servers. Learning to scale horizontally with more servers instead of vertically with more powerful is important as it is a current industry trend with applications in cloud computing and distributed systems.

2. Design and implementation
   Include a detailed description of your design and how you decided to implement everything from the corruption of data, virtual-to-physical block translation, and handling failures. Use subsections for highlighting the major changes for each of the python programs.

1) implement checksum handling on the server-side, and return error when checksums don't match (-cblk)
2) implement abstraction layer for Get(), Put(), RSM() on client side (see above) and detect/print CORRUPTED_BLOCK
3) implement support to connect to multiple servers on the client side (hint: you can use a dict for block_server)
4) implement RAID-0, where data is Put() to all servers, RSM() to server 0, and Get() from any server
5) expand it to support detection when a server is disconnected and failover to another server (use at-most-once, see below)
6) expand it to support detection of a checksum error and failover to another server
7) expand to RAID-4, where one server is the parity server
8) expand to RAID-5, where the parity is distributed
9) implement the repair procedure

3. Evaluation
   Describe how you tested your program and, for EEL-5737 students, how you evaluated the load distribution.

4. Reproducibility
   Describe step by step instructions for how to use and run your file system and if possible, include how to run the tests you used to verify your code.

5. Conclusions

Hello
