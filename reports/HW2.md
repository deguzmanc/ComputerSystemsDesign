## Design/implementation

1. Warmup: extend the design of memoryfs_shell.py to support the following shell commands:

`mkdir dirname`
creates a directory named "dirname" (a string without spaces) in the current working directory

`create filename`
creates a file named "filename" (a string without spaces) in the current working directory

`append filename string`
appends a string (without spaces) to the end of "filename", if it exists (and if there is sufficient room in the file)

Hint: follow the pattern for the other commands in the shell to implement these. Familiarize yourself with the Create() and Write() methods of the FileName() class given to you in memoryfs.py

2. Main challenge: extend your design to support unlinking (removing). In particular, you will extend the FileName() class in memoryfs.py with the Unlink() method, and extend the shell with the rm command (which calls Unlink()):

memoryfs_shell.py:
rm filename
Remove the file by calling Unlink(), if the file exists in the cwd and is a regular file (not a directory)

memoryfs.py
def Unlink(self, dir, name):

Here, "dir" is the _inode number_ of the current directory and "name" is the _file name_ to be unlinked

Similar to the book's description, this function should provide the following functionality:

- NOTE: please ensure you return the error message EXACTLY AS SHOWN BELOW for smooth grading. Your aasignment _will_ have points deducted for not following the naming convention\*

a) Ensure "dir" corresponds to a valid directory; if not, return an error ERROR_UNLINK_INVALID_DIR
b) Ensure "name" exists in the directory; if not, return an error ERROR_UNLINK_DOESNOT_EXIST
c) Ensure "name" refers to a file of type INODE_TYPE_FILE; if not, return error ERROR_UNLINK_NOT_FILE
d) Decrement the refcnt of the file that is being unlinked
e) Remove the (name,inode) binding for this file in dir
f) Decrement the refcnt for the directory dir
g) If the file's refcnt drops to zero:
g.1) Free up the file's blocks (setting the proper byte(s) to 0 in the free block bitmap)
g.2) Free up the inode (setting the inode to be INODE_TYPE_INVALID)
