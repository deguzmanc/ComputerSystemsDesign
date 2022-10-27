import pickle, logging
import argparse
import time
import dbm
import os.path

# For locks: RSM_UNLOCKED=0 , RSM_LOCKED=1 
RSM_UNLOCKED = bytearray(b'\x00') * 1
RSM_LOCKED = bytearray(b'\x01') * 1

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
  rpc_paths = ('/RPC2',)

class DiskBlocks():
  def __init__(self, total_num_blocks, block_size):
    # This class stores the raw block array
    self.block = []                                            
    # Initialize raw blocks 
    for i in range (0, total_num_blocks):
      putdata = bytearray(block_size)
      self.block.insert(i,putdata)

if __name__ == "__main__":

  # Construct the argument parser
  ap = argparse.ArgumentParser()

  ap.add_argument('-nb', '--total_num_blocks', type=int, help='an integer value')
  ap.add_argument('-bs', '--block_size', type=int, help='an integer value')
  ap.add_argument('-port', '--port', type=int, help='an integer value')
  ap.add_argument('-delayat', '--delayat', type=int, nargs='?', help='an integer value to delay every nth request')
  ap.add_argument('-initdbm', '--initdbm', type=int, nargs='?', help='an integer flag; 1 initializes the database with zero blocks, 0 does not initialize the database')
  ap.add_argument('-dbmfile', '--dbmfile', type=str, nargs='?', help='a string that names the file used by dbm in disk')

  args = ap.parse_args()

  if args.total_num_blocks:
    TOTAL_NUM_BLOCKS = args.total_num_blocks
  else:
    print('Must specify total number of blocks') 
    quit()

  if args.block_size:
    BLOCK_SIZE = args.block_size
  else:
    print('Must specify block size')
    quit()

  if args.port:
    PORT = args.port
  else:
    print('Must specify port number')
    quit()

  DELAY_AT = -1
  if args.delayat:
    DELAY_AT = args.delayat


  # initialize blocks
  RawBlocks = DiskBlocks(TOTAL_NUM_BLOCKS, BLOCK_SIZE)
  request_count = 0

  if args.dbmfile:
    DBM_FILE = args.dbmfile
    INIT_DBM = args.initdbm
    with dbm.open(DBM_FILE, 'c') as db:
      # initialize from file
      if INIT_DBM == 0: 
        for i in range(0, TOTAL_NUM_BLOCKS):
          RawBlocks.block[i] = bytearray(db[str(i)])
      #write zeroes to file
      elif INIT_DBM == 1:
        for i in range (0, TOTAL_NUM_BLOCKS):
          db[str(i)] = bytes(RawBlocks.block[i])
      else:
        print('Must specify a valid initdbm if dbmfile is specified')
        quit()


  # Create server
  server = SimpleXMLRPCServer(("127.0.0.1", PORT), requestHandler=RequestHandler) 

  def Get(block_number):
    global request_count
    request_count += 1
    if DELAY_AT != -1 and request_count % DELAY_AT == 0:
      time.sleep(10)
    result = RawBlocks.block[block_number]
    return result

  server.register_function(Get)

  def Put(block_number, data):
    global request_count
    request_count += 1
    if DELAY_AT != -1 and request_count % DELAY_AT== 0:
      time.sleep(10)
    RawBlocks.block[block_number] = data.data

    # write to dbm as well
    if args.dbmfile:
      with dbm.open(DBM_FILE, 'c') as db:
        db[str(block_number)] = bytes(data.data)
    return 0

  server.register_function(Put)

  def RSM(block_number):
    result = RawBlocks.block[block_number]
    # RawBlocks.block[block_number] = RSM_LOCKED
    RawBlocks.block[block_number] = bytearray(RSM_LOCKED.ljust(BLOCK_SIZE,b'\x01'))

    # write to dbm as well
    if args.dbmfile:
      with dbm.open(DBM_FILE, 'c') as db:
        db[str(block_number)] = bytes(bytearray(RSM_LOCKED.ljust(BLOCK_SIZE,b'\x01')))

    return result

  server.register_function(RSM)

  # Run the server's main loop
  print ("Running block server with nb=" + str(TOTAL_NUM_BLOCKS) + ", bs=" + str(BLOCK_SIZE) + " on port " + str(PORT))
  server.serve_forever()

