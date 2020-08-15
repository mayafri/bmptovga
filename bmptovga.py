#!/usr/bin/env python3

import binascii
import re

filename = input("Nom du fichier BMP : ")

if filename[-4:].lower() == '.bmp':
    prettyname = filename[:-4]
else:
    prettyname = filename

f = open(filename, "rb")
bindata = f.read()
f.close()

textdata = binascii.hexlify(bindata).decode()

ld = re.findall('..', textdata)
width  = int(str(ld[21]+ld[20]+ld[19]+ld[18]),16)
height = int(str(ld[25]+ld[24]+ld[23]+ld[22]),16)

padding_ligne = 0
imagesize  = int(str(ld[37]+ld[36]+ld[35]+ld[34]),16)
pixels = width*height
if pixels < imagesize:
    padding_ligne = int((imagesize-pixels)/height)

print("Taille détectée : "+str(width)+" x "+str(height)+" pixels.")

ldimg = ld[1078:] # 54 octets header + 1024 octets palette

ldordered = []
pas = 0
for i in range(1, width+1):
    ldordered += [ldimg[pas:pas+width]]
    pas = pas+width+padding_ligne

foutput = prettyname+": \n"

for i in reversed(range(height)):
    foutput += "db 0x"+',0x'.join(ldordered[i])+'\n'

filenameout = prettyname+'.asm'
f = open(filenameout, 'w');
f.write(foutput)
f.close()

print("Fichier converti sous le nom : "+filenameout);
