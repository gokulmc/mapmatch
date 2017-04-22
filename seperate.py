import csv
import sys
def inBox(nr):
	if(float(nr[0]) < 19.120210):
		return False
	if(float(nr[0]) > 19.143240):
		return False
	if(float(nr[1]) < 72.894318):
		return False
	if(float(nr[0]) > 72.933929):
		return False
	return True

filename = str(sys.argv[1])
print filename
f = open(filename,'r')
fo = open('out'+filename,'w')
w = csv.writer(fo)
rows = csv.reader(f)
label =[]
label.append('lat')
label.append('long')
label.append('TimeStamp')
w.writerow(label)
for r in rows:
	nr=r
	# nr.append(r[2])
	if(nr!=[]):
		if(inBox(nr)):
			w.writerow(nr)
		else :
			print 'Out'
