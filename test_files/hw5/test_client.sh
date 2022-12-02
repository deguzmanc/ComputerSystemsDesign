#!/bin/sh
echo "test$1.in";
echo "test$1.out";

python3 ../../HW4_memoryfs/memoryfs_shell_rpc.py -nb 1536 -bs 256 -ns 4 -startport 8000 -cid 0 -is 32 < "test$1.in" > "test$1.out"

sh ../clean_output.sh "test$1.out"
