import csv, os, sys
import os.path

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

#print(d)
#print(d1)

# Merge Both dictionary d and d1 having same key Name name result
print("\n \n")

result = {}
for key in (d.keys() | d1.keys() | d2.keys()):
    if key in d: result.setdefault(key, []).append(d[key])
    if key in d1: result.setdefault(key, []).append(d1[key])
    if key in d2: result.setdefault(key, []).append(d2[key])

#print (result)

temp_result = {}
temp_result = result.copy()
#print(temp_result)


i = 0
for key in  result:
    i += 1
    #print(key)
    #print(result[key])
print("Total Number of players are {} \n so In each team there would be 6 members will come!".format(i))
#print(result['Ben Finkelstein'][2])

# create new csv file named reult.csv
def createCSVFile():
    with open('tempLeagueDict.csv', 'w') as csvfile:
        fieldNames = {'Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)'}
        fileLeagueWriter = csv.DictWriter(csvfile, fieldNames)
        fileLeagueWriter.writeheader()
        for key, value in sorted(result.items(),
                                 key=lambda item: ('Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)')):
            fileLeagueWriter.writerow({
                'Name': key,
                'Height (inches)': result[key][0],
                'Soccer Experience': result[key][1],
                'Guardian Name(s)': result[key][2]
            })



def print_line():
    print("-"*60)

# rearranging order
def rearrangingOrder():
    with open('tempLeagueDict.csv', 'r') as infile, open('reordered.csv', 'w') as outfile:
        # output dict needs a list for new column ordering
        fieldnames = ['Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)



#Group name retutn function
def findGroup(yourGroup):
    '''
    enter group list and returns Name of Group
    '''
    if yourGroup == listOne or yourGroup == group1:
        return 'Dragons'
    if yourGroup == listTwo or yourGroup == group2:
        return 'Sharks'
    if yourGroup == listThree or yourGroup == group3:
        return 'Raptors'


# small print group list function
def myList_print():
    '''
    it selects group printing if you select 1, 2, or 3
    '''
    myGroup = input('enter group name for print >')
    if myGroup == str(1):
        print(listOne)
    if myGroup == str(2):
        print(listTwo)
    if myGroup == str(3):
        print(listThree)

def print_All():
    '''
    function creates 'teams.txt' file that shows three team finalized with all players details
    Showing thier group.
    '''
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

#---------------------create letters to all soccer group members--------------------
def print_all_individul_members_ofAllGroup():
    '''This function creates text letters to all players parents welcoming and intimation in subfolder 'letters'. '''
    global listOne, listTwo, listThree

    group_list = [listOne,listTwo,listThree]
    #print(listOne)
    #xx = 0
    #yy = 0
    for yy in group_list:
        #xx = 0
        #print("llll")
        #print(yy)
        for xx in yy:
            group = findGroup(yy)
            print(xx)
            player = "{}".format(xx)
            player1 = player.replace(" ", "_")
            fileNamePlayer = "{}.txt".format(player1.lower())
            print(player1)
            print(fileNamePlayer)
            for key in temp_result:
                if key == xx:
                    print(key)
                    print('nnnn')
                    print(temp_result[key][2])
                    parents = temp_result[key][2]
            # parents = result[xx][2]
            # print('parents = {}'.format(parents))
            subDrectory = "letters"
            try:
                os.mkdir(subDrectory)
            except Exception:
                pass
            with open(os.path.join(subDrectory, fileNamePlayer), 'w') as txtFile:
                line1 = " Well Come Letter \n"
                line2 = ' Dear {}, \n'.format(parents)
                line3 = ' We would like to welcome your son {} in Soccer League Group {} \n'.format(player, group)
                line4 = ' On Date 28 January 2018 newly formed group will start its practise at 8:00 AM \n'
                line5 = ' We are looking forward {} at the venue. \n \n'.format(player)
                line6 = ' Best Regards, \n {} Team \n H Devis'.format(group)

                finalLine = line1 + line2 + line3 + line4 + line5 + line6
                txtFile.write(finalLine)



#---------------------create letters end-----------------

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
tito = 89

def createNew():
    result = temp_result.copy()
    print(result.copy())
    listOne = []
    listTwo = []
    listThree = []
    my_list = []
    return result

def command():
    print("---------------- COMMAND Instruction --------------")
    print("1. if you enter 'end' or 'exit' then your programe goes closed at prompt >>>  \n")
    print("2. if you enter ''YES' or 'NO' then you get list of experienced or non-experienced player list \n")
    print("3. if you enter 'print' then you may gate selected group members list printed \n")
    print("4. if you enter 'create' then you enter in group player selection part  \n")
    print("5. You can come out from group creation/selection typing 'close' at the prompt >> and gets prompt >>> \n ")
    print("6. Selection Help::Enter 1 for Group Name 'Dragons', 2 for 'Sharks', 3 for 'Raptors' in selection prompt > \n")
    print("7. if you enter 'rint all' then teams.txt file will generate. Make sure manual selection completed before it ")
    print("8. Enter 'letter l' for creating text files (Well Come Letters) to all players in subfolder 'letters'  ")
    print("9. Enter 'newcreate' after finishing for new arranged formation of group")
    print("10. Enter 'auto' or 'a' then team will devide automatic in three parts and teams.txt file generates")

cls()

def mainFun():
    command_count = 0
    while True:
        # if you enter 'end' or 'exit then your programe goes closed
        # if you enter ''YES' or 'NO' then you get list of experienced or non-experienced player list
        # if you enter 'print then you may gate selected group members list printed
        # if you enter 'create' then you enter in group player selection part
        global listOne
        global listTwo
        global listThree, result
        #print("  hi {}".format(listOne))
        print_line()
        if command_count == 0:
            command()
            command_count = 1;
        print_line()
        word = input("enter your word >>> ")
        ii = 0
        iii = 0
        if word == 'command':
            command()

        if word == 'end' or word == 'exit':
            print("Thank You, Programme is going to close!!")
            break
        if word == "auto" or word == "a":
            autumatic_selection_team()
            print("three team selected and teams.txt file generated")
            break
        if word == 'YES' or word == 'NO':
            for key in result.copy():

                if result[key][1] == word.upper():
                    ii += 1;
                    print("{} : {}".format(key, result[key]))
            print('Total Number {} expericed {} '.format(ii, word))
        if word == 'print':
            cls()
            myList_print()
        if word == 'print all':
            cls()
            print_All()
        if word == 'newcreate':
            result = createNew()
            listOne = []
            listTwo = []
            listThree = []
            my_list = []
        if word == 'print l':
            print_all_individul_members_ofAllGroup()
        if word == 'create':
            cls()
            print("You can come out from group creation typing 'close' ")
            print("Selection Help:: 1 for Dragons, 2 for Shark, 3 for Raptors")
            groupName = input("Enter group name 1 or 2 or 3 >>")
            if groupName == str(1):
                my_list = listOne
            elif groupName == str(2):
                my_list = listTwo
            elif groupName == str(3):
                my_list = listThree
            else:
                print('Wrong Selection, Select 1 or 2 or 3')
                continue
            print("Your selected {}".format(groupName))
            # print(result.copy())
            for key in result.copy():
                if len(my_list) >= 6:
                    print('there is limit of 6 in single group')
                    print("Type 'print' command will show your selected group ")
                    print("Type 'print all' give selected and finalized team list in 'teams.txt' file ")
                    if groupName == 1:
                        listOne = my_list
                    if groupName == 2:
                        listTwo = my_list
                    if groupName == 3:
                        listThree = my_list
                    my_list = []
                    break
                iii += 1
                print("{} : {} count {}".format(key, result[key], iii))
                select = input("enter selection in 'y' or 'n' > ")
                if select == 'close':
                    break
                if select == 'Y' or select == 'y':
                    my_list.append(key)
                    result.pop(key, None)
                    cls()
                    # print(result)
                    print(my_list)
                if select == 'N' or select == 'n':
                    continue

expList = []
unexpList = []
group1 = []
group2 = []
group3 = []
import random
def autumatic_selection_team():
    for key in  result.copy():
        print(result[key][1])
        if result[key][1] == 'YES':
            expList.append(key)
        if result[key][1] == 'NO':
            unexpList.append(key)

    print(expList)
    print(unexpList)
    nn = len(expList)
    print(nn)
    #r = random.randint(0,nn-1)
    num = 0
    while True:
        if len(expList)==0:
            print(expList)
            print(group1)
            print(group2)
            print(group3)
            break
        #print(expList[num])
        if num == 100:
            print("hi")
            print(group1)
            print(group2)
            print(group3)

            num = 0
            #break

        r = random.randint(1, 3)
        #print("num = {} and expList {}".format(num),expList[num-1])
        #print(expList[r])
        #expList.pop(0)
        if r == 1:
            if len(group1)==3:
                continue
            group1.append(expList[num])
            expList.pop(num)
            #num += 1
        if r == 2:
            if len(group2)==3:
                continue
            group2.append(expList[num])
            expList.pop(num)
            #num += 1
        if r == 3:
            if len(group3)==3:
                continue
            group3.append(expList[num])
            expList.pop(num)
            #num = 0
    num = 0
    while True:
        if len(unexpList)==0:
            print(unexpList)
            print(group1)
            print(group2)
            print(group3)
            break
        #print(expList[num])
        if num == 100:
            print("hi")
            print(group1)
            print(group2)
            print(group3)

            num = 0
            #break

        r = random.randint(1, 3)
        #print("num = {} and expList {}".format(num),expList[num-1])
        #print(expList[r])
        #expList.pop(0)
        if r == 1:
            if len(group1)==6:
                continue
            group1.append(unexpList[num])
            unexpList.pop(num)
            #num += 1
        if r == 2:
            if len(group2)==6:
                continue
            group2.append(unexpList[num])
            unexpList.pop(num)
            #num += 1
        if r == 3:
            if len(group3)==6:
                continue
            group3.append(unexpList[num])
            unexpList.pop(num)
            #num = 0
    with open("teams.txt",'w') as f:
        f.write("-"*60)
        f.write("\n")
        f.write('Soccer Team Groups \n')
        f.write("-" * 60)
        f.write("\n")
        print_line()
        f.write("Group Name Dragons \n")
        for player in group1:
            for key in result:
                if player == key:
                    f.write("Player Name:: {} \n".format(player))
                    f.write('Deatils :: Height {}, Experience {}, Parents Name {} \n'.format(result[player][0],
                                                                                             result[player][1],
                                                                                             result[player][2]))
        f.write("-" * 60)
        f.write("\n")
        f.write("Group Name Sharks \n")
        for player in group2:
            for key in result:
                if player == key:
                    f.write("Player Name:: {} \n".format(player))
                    f.write('Deatils :: Height {}, Experience {}, Parents Name {} \n'.format(result[player][0],
                                                                                             result[player][1],
                                                                                             result[player][2]))
        f.write("-" * 60)
        f.write("\n")
        f.write("Group Name Raptors \n")
        for player in group3:
            for key in result:
                if player == key:
                    f.write("Player Name:: {} \n".format(player))
                    f.write('Deatils :: Height {}, Experience {}, Parents Name {} \n'.format(result[player][0],
                                                                                             result[player][1],
                                                                                             result[player][2]))
        print_Automatic_all_individul_members_ofAllGroup(group1,group2,group3)





#---------------------Automatic create letters to all soccer group members--------------------
def print_Automatic_all_individul_members_ofAllGroup(g1,g2,g3):
    '''This function creates text letters to all players parents welcoming and intimation in subfolder 'letters'. '''
    #global listOne, listTwo, listThree

    group_list = [g1,g2,g3]
    #print(listOne)
    #xx = 0
    #yy = 0
    for yy in group_list:
        #xx = 0
        #print("llll")
        #print(yy)
        for xx in yy:
            group = findGroup(yy)
            print(xx)
            player = "{}".format(xx)
            player1 = player.replace(" ", "_")
            fileNamePlayer = "{}.txt".format(player1.lower())
            print(player1)
            print(fileNamePlayer)
            for key in temp_result:
                if key == xx:
                    print(key)
                    print('nnnn')
                    print(temp_result[key][2])
                    parents = temp_result[key][2]
            # parents = result[xx][2]
            # print('parents = {}'.format(parents))
            subDrectory = "letters"
            try:
                os.mkdir(subDrectory)
            except Exception:
                pass
            with open(os.path.join(subDrectory, fileNamePlayer), 'w') as txtFile:
                line1 = " Well Come Letter \n"
                line2 = ' Dear {}, \n'.format(parents)
                line3 = ' We would like to welcome your son {} in Soccer League Group {} \n'.format(player, group)
                line4 = ' On Date 28 January 2018 newly formed group will start its practise at 8:00 AM \n'
                line5 = ' We are looking forward {} at the venue. \n \n'.format(player)
                line6 = ' Best Regards, \n {} Team \n H Devis'.format(group)

                finalLine = line1 + line2 + line3 + line4 + line5 + line6
                txtFile.write(finalLine)



#--------------------- Automatic create letters end-----------------

mainFun()
#autumatic_selection_team()











