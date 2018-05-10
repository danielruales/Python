#!/usr/bin/python
import sys

fname        = sys.argv[1] #holds barcode sequences
barcodefname = sys.argv[2] #holds list of barcodes

barcodefile = open(barcodefname, "r") #defines barcodefile
for barcode in barcodefile:
        barcode = barcode.strip() #makes barcode an item
        outfname = "%s.%s" % (fname,barcode) #names output file for each barcode
        print "barcode: %s" % barcode #prints every barcodes to the screen
        outf = open(outfname, "w") #opens file that is being written to
        handle = open(fname, "r") #reads file with barcode sequences
        for line in handle: #for all of the seqeunces in fname
                temp = line.split() #line split (seq# and sequence)
                potential_barcode = temp[1][:len(barcode)] #second item is potential barcode, and is the length of the barcode to the beginning
                if potential_barcode == barcode:
                        outseq = temp[1][len(barcode):] #outseq is rest of matched sequence without barcode
                        print(temp[0] + " " + outseq) #prints the seq# and the outseq
                        outf.write(temp[0] + " " + outseq + "\n") #writes to the file
        handle.close()
        outf.close()
barcodefile.close()
