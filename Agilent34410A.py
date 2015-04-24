#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket,sys

class Agilent34410A:
    BUFFER_SIZE = 1024

    def __init__(self, ip='169.254.102.195', port=5025):
        self.name= "Agilent 34410A"
        self.ip=ip
        self.port=port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

        self.response = ""

    def __del__(self):
        self.s.close()

    def connect(self):
        self.s.connect((self.ip, self.port))

    def send(self,MESSAGE):
        try:
            self.s.send(MESSAGE+'\n')
        except socket.error as e:
            print (e)
            self.connect()
            self.send(MESSAGE+'\n')