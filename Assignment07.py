
#!/usr/bin/python
import sys

barcode = sys.argv[1]
filename = sys.argv[2]
bclen = len(barcode)
for line in open(filename, "r"):
	bc  = line[:bclen]
	seq = line[bclen:]

	if(bc == barcode):
		print(seq.strip())
