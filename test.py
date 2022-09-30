b1 = bytearray(b'0123456789abcdef')
b2 = bytearray(b'0'*16)
b = b1[12:16]
b1[12:16] = b'0000'
print(b1)

# print(b[1*4:-1*4])
# print(b[2*4:])
# print(id(b))
# b[1*4:-1*4] = b[2*4:]
# print(id(b))
# temp = b[4:-4]
# b = b2
# temp = b[2*4:]
print(b)

# s = [0, 1, 2, 3, 0, 0]

# ind_last_non_zero = -1
# while ind_last_non_zero > -1-len(s):
#   print(s[ind_last_non_zero])
#   ind_last_non_zero -= 1
# # for (int counter = myArray.length - 1; counter >= 0; counter--) {