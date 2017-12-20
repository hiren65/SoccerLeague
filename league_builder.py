import csv

with  open("soccer_players.csv",'r') as csvfile:
    for line in csvfile:
        print(line)
    pass
print("\n \n")
with open("soccer_players.csv" , newline='') as csvfile:
    artreader = csv.reader(csvfile, delimiter=',')
    rows = list(artreader)
    for row in rows[0:]:
        print(',   '.join(row))


with open('soccer_players.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
        print(mydict)



d = {}
d1 = {}
list1 = []
with open('soccer_players.csv') as f:
    readers = csv.DictReader(f)
    for row in readers:
        d.setdefault(row['Name'], {}).update({row['Height (inches)']: row['Soccer Experience']})

        d1.update( {row['Name']:row.pop('Guardian Name(s)')})
        

#print(d)
#print(d1)

result = {}
for key in (d.keys() | d1.keys()):
    if key in d: result.setdefault(key, []).append(d[key])
    if key in d1: result.setdefault(key, []).append(d1[key])

print (result)
#df = []
#print(type(df))


