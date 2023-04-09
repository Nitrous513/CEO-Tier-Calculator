import math
import random
import sys
import time

Levels = [1, 2, 3, 4, 5, 6, 7, 8] 
Toons = ["a", "b", "c", "d", "e", "f", "g", "h"]

TotalLevel = 0

# CALCULATE: Calculates the tier based on cog disguise levels.
def Calculate():
        global TotalLevel # This variable needs to be global in order to work
        TotalLevel = 0 # Reset the total level for each calculation
        for x in range (0,NumToons):
                print(Toons[x])
                TotalLevel = Levels[x] + TotalLevel

        Calculation = math.floor(TotalLevel / NumToons)

        print('''Average Level: ''' + str(Calculation))
        print('') # Line break

        if Calculation < 17:
                print('''It will be a Tier 1 run.

8 tables, 4 Corporate Raider Level 11s each
Total number of Cogs: 32
You will earn: 1 Pink Slip''')

        if Calculation > 16 and Calculation < 33:
                print('''It will be a Tier 2 run.

9 tables, 5 The Big Cheese Level 12s each
Total number of Cogs: 45
You will earn: 2 Pink Slips''')

        if Calculation > 32 and Calculation < 48:
                print('''It will be a Tier 3 run.

10 tables, 6 Corporate Raider Level 11s each
Total number of Cogs: 60
You will earn: 3 Pink Slips''')

        if Calculation > 47 and Calculation < 63:
                print('''It will be a Tier 4 run.

8 tables, 8 The Big Cheese Level 12s each
Total number of Cogs: 64
You will earn: 4 Pink Slips''')

        if Calculation > 64:
                print('''It will be a Tier 5 run.

13 tables, 5 The Big Cheese Level 12s each
Total number of Cogs: 65
You will earn: 5 Pink Slips''')

        print('') # Another line break
        Menu()

# GETLEVELS: Gets number of Toons and their respective disguises and levels.
def GetLevels():
        global NumToons
        # Get the number of Toons in the CEO run
        print('How many Toons do you have?')
        NumToons = int(input())
        while NumToons < 1 or NumToons > 8:
                print('Invalid input. Input a number between 1 and 8.')
                NumToons = int(input())
        
        if NumToons >= 1 and NumToons <= 8:
                for x in range(0,NumToons): # Ask what type of cog the toon is
                        print('''What type of cog is Toon ''' + str(x + 1) + '''?
                
1 - Flunky
2 - Pencil Pusher
3 - Yesman
4 - Micromanager
5 - Downsizer
6 - Head Hunter
7 - Corporate Raider
8 - The Big Cheese
9 - Exit''')
                        CogType = int(input())
                        if CogType == 9:
                                Menu()
                        
                        while CogType < 1 or CogType > 9: # Make sure the answer is in between parameters
                                print('Invalid input. Input a number between 1 and 8.')
                                CogType = int(input())
                                if CogType >= 1 and CogType <= 8:
                                        break
                                elif CogType == 9:
                                        Menu()
                        
                        print('What is their level?')
                        CogLevel = int(input())

                        # Type in the level for the cog (cog type is taken into consideration)
                        while CogLevel < CogType or CogLevel > 50 or CogType < 8 and CogLevel > (CogType + 4):
                                print('Invalid input.')
                                CogLevel = int(input())
                                if CogLevel >= CogType and CogLevel <= (CogType + 4) or CogType == 8 and CogLevel < 51:
                                       break
                        
						# ActualLevel is the level of the disguise as it adds up. There are always 5 levels in each disguise prior to Big Cheese.
                        if CogType == 1:
                                Cog = "Flunky Level " + str(CogLevel)
                                ActualLevel = CogLevel
                        elif CogType == 2:
                                Cog = "Pencil Pusher Level " + str(CogLevel)
                                ActualLevel = CogLevel + 4
                        elif CogType == 3:
                                Cog = "Yesman Level " + str(CogLevel)
                                ActualLevel = CogLevel + 8
                        elif CogType == 4:
                                Cog = "Micromanager Level " + str(CogLevel)
                                ActualLevel = CogLevel + 12
                        elif CogType == 5:
                                Cog = "Downsizer Level " + str(CogLevel)
                                ActualLevel = CogLevel + 16
                        elif CogType == 6:
                                Cog = "Head Hunter Level " + str(CogLevel)
                                ActualLevel = CogLevel + 20
                        elif CogType == 7:
                                Cog = "Corporate Raider Level " + str(CogLevel)
                                ActualLevel = CogLevel + 24
                        elif CogType == 8:
                                Cog = "The Big Cheese Level " + str(CogLevel)
                                ActualLevel = CogLevel + 28

                        Levels[x] = ActualLevel
                        Toons[x] = Cog
        Calculate()

def GetRandomLevels():
        global NumToons
        # Get the number of Toons in the CEO run
        print('Input the size of the group. (1 to 8 Toons)')
        NumToons = int(input())
        while NumToons < 1 or NumToons > 8:
                print('Invalid input. Input a number between 1 and 8.')
                NumToons = int(input())
        
        if NumToons >= 1 and NumToons <= 8:
                for x in range(0,NumToons):
                        CogType = math.floor(random.randint(1,8))
                        CogLevel = math.floor(random.randint(1,5))
                        if CogType == 1:
                                Cog = "Flunky Level " + str(CogLevel)
                                ActualLevel = CogLevel
                        elif CogType == 2:
                                Cog = "Pencil Pusher Level " + str(CogLevel + 1)
                                ActualLevel = CogLevel + 5
                        elif CogType == 3:
                                Cog = "Yesman Level " + str(CogLevel + 2)
                                ActualLevel = CogLevel + 10
                        elif CogType == 4:
                                Cog = "Micromanager Level " + str(CogLevel + 3)
                                ActualLevel = CogLevel + 15
                        elif CogType == 5:
                                Cog = "Downsizer Level " + str(CogLevel + 4)
                                ActualLevel = CogLevel + 20
                        elif CogType == 6:
                                Cog = "Head Hunter Level " + str(CogLevel + 5)
                                ActualLevel = CogLevel + 25
                        elif CogType == 7:
                                Cog = "Corporate Raider Level " + str(CogLevel + 6)
                                ActualLevel = CogLevel + 30
                        elif CogType == 8:
                                CogLevel = math.floor(random.randint(1, 43))
                                Cog = "The Big Cheese Level " + str(CogLevel + 7)
                                ActualLevel = CogLevel + 35

                        Levels[x] = ActualLevel
                        Toons[x] = Cog
        Calculate()

def TierInfo():
        print('''LIST OF TIERS
=================================================================================================
Tier 1 (Flunky Level 1 - Micromanager Level 4): 8 tables, 4 Lvl 11 Corporate Raiders each
Tier 2 (Micromanager Level 5 - Corporate Raider Level 8): 9 tables, 5 Lvl 12 The Big Cheeses each
Tier 3 (Corporate Raider Level 9 - The Big Cheese Level 19): 10 tables, 6 Lvl 11 Corporate Raiders each
Tier 4 (The Big Cheese Level 20 - 34): 8 tables, 8 Lvl 12 The Big Cheeses each
Tier 5 (The Big Cheese Level 35+): 13 tables, 5 Lvl 12 The Big Cheeses each

As the tiers increase, the number of pink slips also increase. (Ex. Tier 3 = 3 pink slips)
''')

def SoundlessStrats():
        print('''STRATEGIES FOR SOUNDLESS CEO RUNS:
Note: these strategies only work when the cog is LURED.

Level 9 - 4 Whole Cream Pies
Level 10 - 2 Cakes OR 3 Storms OR 3 Hoses + 1 Piano
Level 11 - 2 Cakes + 1 Pie OR 3 Storms + 1 Hose
Level 12 - 1 Hose + 2 Pianos
''')

def MenuSelect():
		Answer = input()
        if Answer == "1":
                GetLevels()
        elif Answer == "2":
                GetRandomLevels()
        elif Answer == "3":
                TierInfo()
                Menu()
        elif Answer == "4":
                SoundlessStrats()
                Menu()
        elif Answer == "9":
                sys.exit()

def Menu():
        print('''CEO Tier Calculator

1 - Calculate
2 - Randomly generate levels
3 - All tiers
4 - Soundless strategies
9 - Exit ''')
		MenuSelect()

        while Answer != "1" or "2" or "9":
                print('Invalid input.')
                MenuSelect()

Menu()
