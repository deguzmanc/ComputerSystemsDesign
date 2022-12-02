#!/bin/sh

# python3 ../../HW4_memoryfs/memoryfs_server.py -p "800$1" -nb 512 -bs 256
python3 ../../HW4_memoryfs/memoryfs_server.py -p "8000" -nb 512 -bs 256 &
python3 ../../HW4_memoryfs/memoryfs_server.py -p "8001" -nb 512 -bs 256 &
python3 ../../HW4_memoryfs/memoryfs_server.py -p "8002" -nb 512 -bs 256 &
python3 ../../HW4_memoryfs/memoryfs_server.py -p "8003" -nb 512 -bs 256