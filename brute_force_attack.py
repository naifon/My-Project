import itertools
import logging
import os
import random
import string
import time
import zipfile
import zlib
from concurrent.futures import ThreadPoolExecutor

DICTIONARY_PATH = os.path.dirname(os.path.abspath(__file__)) + '/resources/dictionary.txt'


class ZipPwdCracker:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def dictionary_attack(self, zip_file_path, DICTIONARY_PATH, max_length=4):
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            self.logger.debug(zf.infolist())
            with open(DICTIONARY_PATH, 'r') as f:
                for line in f.readlines():
                    password = line.strip('\n').encode()
                    if len(password) == max_length:
                        print("Try with password: " + str(password.decode()))
                        try:
                            zf.setpassword(password)
                            if zf.testzip() is None:
                                return 'Password found: {}'.format(password.decode())
                                # return password.decode()
                        except RuntimeError:
                            pass
                        except zlib.error as e:
                            self.logger.error(str(e))

            return "Password not found"

    def brute_force_attack(self, zip_file_path, max_length=4, callback=None):
        alphabet = string.digits + string.ascii_letters + string.punctuation
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            # self.logger.debug(zf.infolist())
            for i in range(1, max_length + 1):
                for j in itertools.product(alphabet, repeat=i):
                    # self.scan_ports_async(itertools.product(alphabet, repeat=i), callback, max_length)
                    password = ''.join(j).encode()
                    # self.logger.debug("Try " + str(password))
                    print("Try with password: " + str(password.decode()))
                    try:
                        zf.setpassword(password)
                        if zf.testzip() is None:
                            return 'Password found: {}'.format(password.decode())
                        else:
                            callback("Try with password: {}".format(password.decode()))

                        # time.sleep(100)

                        # return password.decode()
                    except RuntimeError:
                        pass
                    except zlib.error as e:
                        # self.logger.error(str(e))
                        pass

            return "Password not found"

    # def scan_ports_async(self, list, callback=None, max_length=4):
    #     THREAD_LIMIT = 2
    #     with ThreadPoolExecutor(max_workers=THREAD_LIMIT) as executor:
    #         futures = []
    #         for port in list:
    #             future = executor.submit(self.st, port)
    #             futures.append(future)
    #
    #         for future in futures:
    #             result = future.result()
    #             # print(result)
    #             if result is not None and callback:
    #                 if random.randint(1, 3):
    #                     callback(result)
    #
    # def st(self, str1):
    #     return ''.join(str1)
