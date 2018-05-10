#!/usr/bin/python

import sys
import the
import math

def ave_stderr(x): #defining function we are creating using variable x (array)
	ave = sum(x)/len(x) #sum of numbers over amount of numbers
	#print "mean: %f" % ave

	ssq = 0.0
	for y in x:
		ssq += (y-ave)*(y-ave) #sum of squares 

	#print "ssq: %f" % ssq	

	var = ssq/(len(x) -1) #calculate variance
	#print "var: %f" % var

	sdev = math.sqrt(var) #math package sqrt function
	#print "stdev: %f" % sdev

	stderr = sdev / math.sqrt(len(x)) #calculate standard error
	#print "stderr %f" %stderr

	return (ave,stderr) #after calculating, send back to where it was sent from

#match barcodes with sequences
barcodefname = sys.argv[1] #contains list of sequence barcodes
fname = sys.argv[2] #contains barcoded sequences

barcodefile = open(barcodefname, "r")
listOfBarcodeOutputFiles = []
barcodes = []
for barcode in barcodefile:
    barcode = barcode.strip()
    outfname = "%s.%s" % (fname,barcode)
    listOfBarcodeOutputFiles.append(outfname) #save the list of file created
    barcodes.append(barcode)
    outf = open(outfname, "w") #open the file we are writing to
    handle = open(fname, "r") #read the file with the barcode sequences
    for line in handle: #for each seqeunce in the fname
        temp = line.split() #split the line (seq# and sequence)
        potential_barcode = temp[1][:len(barcode)] #potential barcode is the second item and is the from the length of the barcode to the beginning
        if potential_barcode == barcode:
            outseq = temp[1][len(barcode):] #outseq is the rest of the matched sequence without the barcode
            #print(temp[0] + " " + outseq) #print the seq# and the outseq
            outf.write(temp[0] + " " + outseq + "\n") #write to the file
    handle.close()
    outf.close()
barcodefile.close()

#creating filenames
j = 0
for filename in listOfBarcodeOutputFiles:
    infname    = filename
    fastaname  = infname + ".fasta"
    mafftfname = fastaname + ".mafft"
    stockname  = mafftfname + ".stock"
    distancename = stockname + ".distance"

    #simple to fasta
    handle = open(infname, "r")
    outf   = open(fastaname, "w")
    for line in handle:
        linearr = line.split()
        seqid = linearr[0]
        seq = linearr[1]
        outf.write(">%s\n%s\n" % (seqid, seq))
    handle.close()
    outf.close()

    #align using mafft
    cmd = "mafft %s > %s" % (fastaname, mafftfname)
    sys.stderr.write("command: %s\n" % cmd)
    os.system(cmd)
    sys.stderr.write("command done")

    #convert fasta maft alignment to stockholm
    cmd = "fasta_to_stockholm %s > %s" % (mafftfname,stockname)
    sys.stderr.write("command: %s\n" % cmd)
    os.system(cmd)
    sys.stderr.write("command done\n")

    #run quicktree to get distance matrix
    cmd = "quicktree -out m %s" % stockname
    #sys.stderr.write("command: %s\n" % cmd)
    #subprocess.call(cmd, shell=True)
    #os.system(cmd)
    stream = os.popen(cmd).read()
    #sys.stderr.write("command done \n")
    fDistance = open(distancename, "w")
    fDistance.write(stream)
    fDistance.close()
    fDistance = open(distancename,"r")   

    user_numbers = []
    handle = fDistance
    i=1
    for line in handle:
	linearr = line.split()
	for s in linearr[i:]:
		user_numbers.append(float(s))
	i += 1
    # handle.close()

    #print user_numbers
    (a,s) = ave_stderr(user_numbers)
    #print(stockname)
    print "%s %f +/- %f" % (barcodes[j],a,s)
    j += 1
    #print(ave_stderr())
        
    handle.close()
