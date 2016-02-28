f = open('workfile', 'w')
f = open('workfile', 'r')
f.read()
f.readline()

for line in f:
    print line

f.write('This is a test\n')

#its always good to dump data in json format to keep it structures
