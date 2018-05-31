#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2018-05-19 22:54
# @AUTHOR : thang
import itertools
import logging
import string
import zipfile

import os

import zlib

DICTIONARY_PATH = os.path.dirname(os.path.abspath(__file__)) + '/resources/dictionary.txt'


class ZipPwdCracker:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def dictionary_attack(self, zip_file_path,DICTIONARY_PATH):
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            self.logger.debug(zf.infolist())
            with open(DICTIONARY_PATH, 'r') as f:
                for line in f.readlines():
                    password = line.strip('\n').encode()
                    # self.logger.debug("Try " + str(password))
                    try:
                        zf.setpassword(password)
                        if zf.testzip() is None:
                            return 'Password found: {}'.format(password.decode())
                            return password.decode()
                    except RuntimeError:
                        pass
                    except zlib.error as e:
                        self.logger.error(str(e))

            return

    def brute_force_attack(self, zip_file_path, max_length=4):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            self.logger.debug(zf.infolist())
            for i in range(1, max_length):
                print("Try with password length = " + str(i))
                for j in itertools.product(alphabet, repeat=i):
                    password = ''.join(j).encode()
                    # self.logger.debug("Try " + str(password))
                    try:
                        zf.setpassword(password)
                        if zf.testzip() is None:
                            return 'Password found: {}'.format(password.decode())
                            # return password.decode()
                    except RuntimeError:
                        pass
                    except zlib.error as e:
                        # self.logger.error(str(e))
                        pass
            return
