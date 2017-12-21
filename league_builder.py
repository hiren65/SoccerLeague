import csv, os, sys

# To clear content
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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

temp_result = {}
temp_result = result.copy()
print(temp_result)

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

def print_line():
    print("-"*60)

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

def print_All():
    name = 0
    cls()
    ## delete only if file exists ##
    filename = 'teams.txt'
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("Sorry, I can not remove %s file." % filename)
    print_line()
    print('Group 1 (Dragons)')
    print_line()
    # Create new text file
    with open('teams.txt', 'a') as txtFile:
        txtFile.write("-" * 50)
        txtFile.write("\n")
        txtFile.write('Group 1 Dragons')
        txtFile.write("\n")
        txtFile.write("-" * 50)
        txtFile.write("\n")
    for name in listOne:
        chiku = {}
        chiku = temp_result.copy()
        print(" Player {}:Height-{},  Soccer Experience-{},  Guardian Name-{} ".format(name,chiku[name][0],chiku[name][1],chiku[name][2]))
        # Add group 1 selected player list in text file
        with open('teams.txt', 'a') as txtFile:
            txtFile.write("Player : {} \n :Height-{},  Soccer Experience-{},  Guardian Name-{} \n ".format(name,chiku[name][0],chiku[name][1],chiku[name][2]))

    print_line()
    print('Group 2 (Sharks)')
    print_line()

    with open('teams.txt', 'a') as txtFile:
        txtFile.write("-" * 50)
        txtFile.write("\n")
        txtFile.write('Group 2 Sharks')
        txtFile.write("\n")
        txtFile.write("-" * 50)
        txtFile.write("\n")

    for name in listTwo:
        chiku = {}
        chiku = temp_result.copy()
        print("Player {}:Height-{},  Soccer Experience-{},  Guardian Name-{} ".format(name,chiku[name][0],chiku[name][1],chiku[name][2]))
        # Add group 2 selected player list in text file
        with open('teams.txt', 'a') as txtFile:
            txtFile.write("Player : {} \n :Height-{},  Soccer Experience-{},  Guardian Name-{} \n ".format(name,chiku[name][0],chiku[name][1],chiku[name][2]))
    print_line()
    print('Group 3 (Raptors)')
    print_line()

    with open('teams.txt', 'a') as txtFile:
        txtFile.write("-" * 50)
        txtFile.write("\n")
        txtFile.write('Group 3 Raptors')
        txtFile.write("\n")
        txtFile.write("-" * 50)
        txtFile.write("\n")
    for name in listThree:
        chiku = {}
        chiku = temp_result.copy()
        print("Player {}:Height-{},  Soccer Experience-{},  Guardian Name-{} ".format(name,chiku[name][0],chiku[name][1],chiku[name][2]))
        # Add group 3 selected player list in text file
        with open('teams.txt', 'a') as txtFile:
            txtFile.write("Player : {} \n :Height-{},  Soccer Experience-{},  Guardian Name-{} \n ".format(name,chiku[name][0],chiku[name][1],chiku[name][2]))
    print_line()

# Create text file
def create_textFile():
    with open('teams.txt', 'w') as txtFile:
        txtFile.write()

#temp_result = {}
#temp_result = result.copy()
#print(temp_result)

listOne = []
listTwo = []
listThree = []
my_list = []

def createNew():
    result = temp_result.copy()
    print(result.copy())
    listOne = []
    listTwo = []
    listThree = []
    my_list = []
    return result

def command():
    print("if you enter 'end' or 'exit then your programe goes closed \n")
    print("if you enter ''YES' or 'NO' then you get list of experienced or non-experienced player list \n")
    print("if you enter 'print' then you may gate selected group members list printed \n")
    print("if you enter 'create' then you enter in group player selection part  \n")


while True:
    # if you enter 'end' or 'exit then your programe goes closed
    # if you enter ''YES' or 'NO' then you get list of experienced or non-experienced player list
    # if you enter 'print then you may gate selected group members list printed
    # if you enter 'create' then you enter in group player selection part
    word = input("enter your word >")
    ii = 0
    iii = 0
    if word == 'command':
        command()

    if word=='end' or word=='exit':
        print("Thank You, Programme is going to close!!")
        break
    if word == 'YES' or word == 'NO':
        for key in result.copy():

            if result[key][1] == word.upper():
                ii += 1;
                print("{} : {}".format(key,result[key]))
        print('Total Number {} expericed {} '.format(ii,word))
    if word == 'print':
        myList_print()
    if word == 'print all':
        print_All()
    if word == 'newcreate':
        result = createNew()
        listOne = []
        listTwo = []
        listThree = []
        my_list = []
    if word == 'create':
        cls()
        groupName = input("Enter group name 1 or 2 or 3")
        if groupName == str(1):
            my_list = listOne
        if groupName == str(2):
            my_list = listTwo
        if groupName == str(3):
            my_list = listThree
        print("Your selected {}".format(groupName))
        print(result.copy())
        for key in result.copy():
            if len(my_list) >= 6:
                print('there is limit of 6 in single group')
                if groupName == 1:
                    listOne = my_list
                if groupName == 2:
                    listTwo = my_list
                if groupName == 3:
                    listThree = my_list
                my_list = []
                break
            iii += 1
            print("{} : {} count {}".format(key, result[key],iii))
            select = input("enter selection in 'y' or 'n' > ")
            if select == 'close':
                break
            if select == 'Y' or select == 'y':

                if  iii == 18:
                    print('finished')

                my_list.append(key)
                result.pop(key, None)
                #print(result)
                print(my_list)
            if select == 'N' or select == 'n':
                continue









