
import json
import random
import time
# name - Sample
# rarity -       Common = 1  Uncommon = 2  Rare = 3  Epic = 4  Legendary = 5
# color - RGB - [r,g,b]
# stats - [STR,DEX,MAG,CON]

# S A B C D

# D - C
# D - D
# D
# D

def initiate(_json):
    start_time = time.time()

   # with open('gamegen\generator\modificators.json') as json_file:
    with open(_json) as json_file:
        data = json.load(json_file)
    
        # Print the type of data variable
        print("Type:", type(data))
    
        # Print the data of dictionary
    ##############################################

    return data, start_time

def gen (data, rarity):    
    stats = [0, 0, 0, 0]
    color1 = [0,0,0]
    color2 = [0,0,0]
    statw = ['D', 'C', 'B', 'A', 'S']
    rar = -1
    atdouble = False
    while rarity != rar:
        mod1 = random.randint(0,len(data['modificators']) - 1)
        att1 = data['modificators'][mod1]
        atdouble = False
        if (att1['rarity'] < 3) and (random.randint(0,2) == 1):
            mod2 = random.randint(0,len(data['modificators']) - 1)
            att2 = data['modificators'][mod2]
            atdouble = True

        
        if (not atdouble):
            rar = att1['rarity']
        else:
            rar = att1['rarity'] + att2['rarity']



    num = random.randint(0,len(data['names']) - 1)
    name = data['names'][num]

    if (atdouble):
        STR = statw[stats[0] + att1['stats'][0] + att2['stats'][0]]
        DEX = statw[stats[1] + att1['stats'][1] + att2['stats'][1]]
        MAG = statw[stats[2] + att1['stats'][2] + att2['stats'][2]]
        CON = statw[stats[3] + att1['stats'][3] + att2['stats'][3]]
    else:
        STR = statw[stats[0] + att1['stats'][0]]
        DEX = statw[stats[1] + att1['stats'][1]]
        MAG = statw[stats[2] + att1['stats'][2]]
        CON = statw[stats[3] + att1['stats'][3]]



    print("-------------------------------")
    if (atdouble):
        print("{} {} {}".format(att1['name'], att2['name'] ,name['name']))
    else:
        print("{} {}".format(att1['name'],name['name']))

    if (not atdouble):
        print("Rarity - {}".format(int(att1['rarity'])))
    else:
        print("Rarity - {}".format((att1['rarity']) + (att2['rarity'])))

    print("-------------------------------")

    print("Alignment - {}".format(name['alignment']))

    if (not atdouble):
        print("att color - {}".format(att1['color']))
    else:
        mixcolor = [0,0,0]
        for i in range(3):
            mixcolor[i] = int((att1['color'][i] + att2['color'][i]) / 2)
        print("att color - {}".format(mixcolor))

    print("name color - {}".format(name['color']))
    print("-------------------------------")
    print("Stats:")
    print("STR = {}".format(STR))
    print("DEX = {}".format(DEX))
    print("MAG = {}".format(MAG))
    print("CON = {}".format(CON))

    return(rar)

#########################################
def output(data, start_time):
    rarsum = 15
    counter = 1
    while counter <= 5:
        if (random.randint(1,100) == 1) and (counter <= 5): 
            print("___________________________")
            print(counter)
            print("___________________________")
            gen(data, 5)
            counter += 1
        if (random.randint(1,20) == 1) and (counter <= 5): 
            print("___________________________")
            print(counter)
            print("___________________________")
            gen(data, 4)
            counter += 1
        if (random.randint(1,6) == 1) and (counter <= 5): 
            print("___________________________")
            print(counter)
            print("___________________________")
            gen(data, 3)
            counter += 1
        if (random.randint(1,3) == 1) and (counter <= 5): 
            print("___________________________")
            print(counter)
            print("___________________________")
            gen(data, 2)
            counter += 1
        if (random.randint(1,2) == 1) and (counter <= 5): 
            print("___________________________")
            print(counter)
            print("___________________________")
            gen(data, 1)
            counter += 1
            print("--- %s seconds ---" % (time.time() - start_time))


def start(_path):
    
    _data, _time = initiate(_path)
    output(_data, _time) 

if __name__ == '__main__':

    _data, _time = initiate()
    output(_data, _time)

# Сценарий 1 - Tutorial
# Сценарий 2 - Stage 2 choose (uncommon - rare)
# Сценарий 3 - Stage 3 choose (rare - epic)
# Сценарий 4 - Stage 4 choose (epic - legendary)
# Bonus - 
# Сценарий 5 - 


