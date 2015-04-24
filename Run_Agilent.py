#! /usr/bin/python
# -*- coding: utf-8 -*-
#Taper quit pour quitter
#Exemple de commande à taper : MEAS:DIOD?

import Agilent34410A

mult = Agilent34410A.Agilent34410A('192.168.38.129')

while True:

    message = raw_input("Quelle mesure voulez-vous ?")

    if message == "quit":
        break

    print (mult.send(message))