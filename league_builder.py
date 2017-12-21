import csv
# Read csv file raw
with  open("soccer_players.csv",'r') as csvfile:
    for line in csvfile:
        print(line)
    pass

# Create Dictionarys d and d1 both with key 'Name'
d = {}
d1 = {}
d2 = {}
list1 = []
with open('soccer_players.csv') as f:
    readers = csv.DictReader(f)
    for row in readers:
        #d.setdefault(row['Name'], {}).update({row['Height (inches)']: row['Soccer Experience']})
        d.update({row['Name']: row.pop('Height (inches)')})
        d1.update({row['Name']: row.pop('Soccer Experience')})

        d2.update( {row['Name']:row.pop('Guardian Name(s)')})


print(d)
#print(d1)
# Merge Both dictionary d and d1 having same key Name name result
print("\n \n")

result = {}
for key in (d.keys() | d1.keys() | d2.keys()):
    if key in d: result.setdefault(key, []).append(d[key])
    if key in d1: result.setdefault(key, []).append(d1[key])
    if key in d2: result.setdefault(key, []).append(d2[key])

print (result)
#df = []
#print(type(df))
i = 0
for key in  result:
    i += 1
    #print(key)
    #print(result[key])
print("Total Number of players are {} \n so In each team there would be 6 members will come!".format(i))
print(result['Ben Finkelstein'][2])
# create new csv file named reult.csv

with open('tempLeagueDict.csv', 'w') as csvfile:
    fieldNames = {'Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)'}
    fileLeagueWriter = csv.DictWriter(csvfile, fieldNames)
    fileLeagueWriter.writeheader()
    for key, value in sorted(result.items(), key=lambda item: ('Name','Height (inches)', 'Soccer Experience', 'Guardian Name(s)')):
        fileLeagueWriter.writerow({
            'Name':key,
            'Height (inches)':result[key][0],
            'Soccer Experience':result[key][1],
            'Guardian Name(s)':result[key][2]
        })


# rearranging order
with open('tempLeagueDict.csv', 'r') as infile, open('reordered.csv', 'w') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)


# small print group list function
def myList_print():
    myGroup = input('enter group name for print >')
    if myGroup == str(1):
        print(listOne)
    if myGroup == str(2):
        print(listTwo)
    if myGroup == str(3):
        print(listThree)
        


listOne = []
listTwo = []
listThree = []
my_list = []

while True:
    # if you enter 'end' or 'exit then your programe goes closed
    # if you enter ''YES' or 'NO' then you get list of experienced or non-experienced player list
    # if you enter 'print then you may gate selected group members list printed
    # if you enter 'create' then you enter in group player selection part
    word = input("enter your word >")
    ii = 0
    if word=='end' or word=='exit':
        break
    if word == 'YES' or word == 'NO':
        for key in result:

            if result[key][1] == word:
                ii += 1;
                print("{} : {}".format(key,result[key]))
        print('Total Number {} expericed {} '.format(ii,word))
    if word == 'print':
        myList_print()
    if word == 'create':
        groupName = input("Enter group name 1 or 2 or 3")
        if groupName == str(1):
            my_list = listOne
        if groupName == str(2):
            my_list = listTwo
        if groupName == str(3):
            my_list = listThree
        print("Your selected {}".format(groupName))
        for key in result:
            print("{} : {}".format(key, result[key]))
            select = input("enter selection > ")
            if select == 'Y' or select == 'y':
                if len(my_list) >= 9:
                    print('there is limit of 9 in single group')
                    if groupName == 1:
                        listOne = my_list
                    if groupName == 2:
                        listTwo = my_list
                    if groupName == 3:
                        listThree = my_list
                    my_list = []
                    break

                my_list.append(key)
                print(my_list)
            if select == 'N' or select == 'n':
                continue









