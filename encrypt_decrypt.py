import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES



import os, random, struct
from Crypto.Cipher import AES

#
# def encryptf(key, filename):
#     chunk_size = 64*1024
#     output_file = filename+".enc"
#     file_size = str(os.path.getsize(filename)).zfill(16)
#     IV = ''
#     for i in range(16):
#         IV += chr(random.randint(0, 0xFF))
#     encryptor = AES.new(key, AES.MODE_CBC, IV)
#     with open(filename, 'rb') as inputfile:
#         with open(output_file, 'wb') as outf:
#             outf.write(file_size)
#             outf.write(IV)
#             while True:
#                 chunk = inputfile.read(chunk_size)
#                 if len(chunk) == 0:
#                     break
#                 elif len(chunk) % 16 != 0:
#                    chunk += ' '*(16 - len(chunk)%16)
#                 outf.write(encryptor.encrypt(chunk))
#
#
# def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
#     """ Encrypts a file using AES (CBC mode) with the
#         given key.
#
#         key:
#             The encryption key - a string that must be
#             either 16, 24 or 32 bytes long. Longer keys
#             are more secure.
#
#         in_filename:
#             Name of the input file
#
#         out_filename:
#             If None, '<in_filename>.enc' will be used.
#
#         chunksize:
#             Sets the size of the chunk which the function
#             uses to read and encrypt the file. Larger chunk
#             sizes can be faster for some files and machines.
#             chunksize must be divisible by 16.
#     """
#     if not out_filename:
#         out_filename = in_filename + '.enc'
#
#     key = Random.get_random_bytes(16)
#     iv = os.urandom(16)
#     # aes_mode = AES.MODE_CBC
#     # obj = AES.new(key, aes_mode, iv)
#     # ciphertext = obj.encrypt(plaintext)
#
#     # iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
#     encryptor = AES.new(key, AES.MODE_CBC, iv)
#     filesize = os.path.getsize(in_filename)
#
#     with open(in_filename, 'rb') as infile:
#         with open(out_filename, 'wb') as outfile:
#             outfile.write(struct.pack('<Q', filesize))
#             outfile.write(iv)
#
#             while True:
#                 chunk = infile.read(chunksize)
#                 if len(chunk) == 0:
#                     break
#                 elif len(chunk) % 16 != 0:
#                     chunk += ' ' * (16 - len(chunk) % 16)
#
#                 outfile.write(encryptor.encrypt(chunk))
#
#


class main(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, data):
        data = self._pad(data)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(data))

    def decrypt(self, data):
        data = base64.b64decode(data)
        iv = data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(data[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


# main =main("keyhere")
#
# #------------encrypt---------------#
#
# result = main.encrypt("saleh")
# print(result)
#
# #------------dencrypt---------------#
#
# result = main.decrypt(result)
# print(result)

