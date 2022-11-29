import matplotlib.pyplot as plt
import numpy as np

global NS
NS = 4

def vbn_to_ps_sn_pbn(virutal_block_number):
    """
    input:
    virtual_block_number
    output:
    parity_server(ps)
    server_number(sn)
    physical_block_number:
    """
    physical_block_number = virutal_block_number // (NS - 1)
    server_number = virutal_block_number % (NS - 1)

    parity_server = (NS - 1 - physical_block_number) % NS
    if server_number >= parity_server:

      server_number += 1

    return parity_server, server_number, physical_block_number


A = -1 * np.ones((NS*2,NS))
B = -1 * np.ones((NS*2,NS))


for i in range(2*NS*(NS-1)):
    ps, sn, pbn = vbn_to_ps_sn_pbn(i)
    A[pbn, sn] = i
    B[pbn, sn] = 1 if i >= 0 else -1
    
  

fig, ax = plt.subplots()
# Using matshow here just because it sets the ticks up nicely. imshow is faster.
ax.matshow(B, cmap='gray', vmin=-5,vmax=1)
plt.xlabel('Server Number')
plt.ylabel('Physical block number')

for (i, j), z in np.ndenumerate(A):
    if z == -1:
      ax.text(j, i, 'pb', ha='center', va='center')
    else:
      ax.text(j, i, int(z), ha='center', va='center')

plt.savefig('RAID5_4.png')
plt.show()
    


