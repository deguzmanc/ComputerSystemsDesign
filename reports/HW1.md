**Q1)** What is the maximum file size possible with this file system configuration?

2 \* 128B = 256B max of block storage.
Because the inode size is 16B and 4, 2, and 2 B are taken for size, type, and refcnt, there are 8B that can store 2, 4B block numbers.

**Q2)** How many inodes are in use in this file system? (not the maximum number of inodes, but how many inodes are in use for this dump file)

This uses inodes 0-9. This was found by showing the inode table (block 4, 5) as well as showinode for [0:16].

**Q3)** Which raw blocks are allocated and in use in this file system?

Blocks 6-17 are allocated. This was found by counting the bytes with flipped bits in the bitmap in blocks 2 and 3 (bitmap). `showblockslice 2 6 17` shows the bytes that have non-zero value.

**Q4)** Describe what is stored in inode 0

Inode 0 stores the root folder.

**Q5)** Describe what is stored in block 6

It stores the file table (name to inode) for the root directory.

**Q6)** Describe what is represented in the output of command showblockslice 6 0 15 (hint: look up ASCII encoding in hexadecimal format, and refer to the file system code slides discussed in class)

The first 12 Bytes are the name '.' for the root directory (reference to itself). The last 4 Bytes signify that it is stored at inode 0.

**Q7)** Describe what is represented in the output of command showblockslice 6 16 31

The first 12 Bytes are the name 'file1.txt'. The last 4 Bytes signify that it is stored at inode 1.

**Q8)** What is the inode number of file file1.txt?

The inode number is 1. (see above)

**Q9)** What is the inode number of directory dir1?

The inode number is 2. This was found by `showblockslice 6 32 47`.

**Q10)** Which raw block stored the inode of file file1.txt?

The inode of file1.txt is stored in the inode table at block 4.

**Q11)** Describe what is stored in block 7

It is the first 128B of file1.txt. This was found because 7 is the first block num in inode 1.

**Q12)** What is the inode number of directory dir3?

The inode number is 7. This was found using `showblockslice 6 80 95`.

**Q13)** What is the inode number of directory dir4?

The inode number is 8. This was found by `showinode 7` and seeing block_num 15. Then `showblockslice 15 32 47` to read the table entry for dir4.

**Q14)** What is the inode number of file file4.txt?

The inode number is 9. This was found by `showinode 8` and seeing block_num 16. Then `showblockslice 16 32 47` to read the table entry for file4.txt.

**Q15)** What block number(s) make up the contents of file4.txt (found in /dir3/dir4)?

Block number 17 is used for file4.txt. This was found using showinode 9. Although block 0 is listed, the size is 66 > 128, so all of file4.txt's data is stored in block 17.
