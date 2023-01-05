import random
import time
# import playsound

# import pygame

# pygame.mixer.init()
# pygame.mixer.music.load('crowd.mp3')
# pygame.mixer.music.play()
i = 1


def displayruns(pscore):
    """
    to display score
    """
    if pscore == 0:
        print("Dot ball")
    elif pscore == 1:
        print("A Quick Single")
    elif pscore == 2:
        print("Good Running, that's 2 runs")
    elif pscore == 3:
        print("Great Running between wickets, Converted 2's into 3")
    elif pscore == 4:
        print("FOUR!!!, Wonderful shot...")
    elif pscore == 6:
        print("That's a HUGE SIX, A massive one")
    else:
        print("THATS OUT!!!!!")
        print("A Wonderful Inning came to an end")


def playingshots(balls, total):
    """
    playing cricket
    """
    # i = 1
    Runs = [0, 1, 2, 3, 4, 6, "OUT"]
    pscore = 0
    global i
    while i <= balls:
        lchoice = random.randint(0, 6)
        ofchoice = random.randint(0, 6)
        schoice = random.randint(0, 6)
        print("\nBall:", i)
        pchoice = input(
            "press\n6. to play on leg side\n4. to play on off side\n2 to play on staight\n-->>")
        if pchoice == '6':
            print("\n")
            time.sleep(0.5)
            displayruns(Runs[lchoice])
            if Runs[lchoice] == "OUT":
                i = i+1
                break
            else:
                pscore = pscore+Runs[lchoice]
                print("\nCurrent Score-->", pscore)
                print("\nCurrent TEAM Score-->", pscore+total)
            time.sleep(1)
        elif pchoice == '4':
            print("\n")
            time.sleep(0.5)
            displayruns(Runs[ofchoice])
            if Runs[ofchoice] == "OUT":
                i = i+1
                break
            else:
                pscore = pscore+Runs[ofchoice]
                print("\nCurrent Score-->", pscore)
                print("\nCurrent TEAM Score-->", pscore+total)
            time.sleep(1)
        elif pchoice == '2':
            print("\n")
            time.sleep(0.5)
            displayruns(Runs[schoice])
            if Runs[schoice] == "OUT":
                i = i+1
                break
            else:
                pscore = pscore+Runs[schoice]
                print("\nCurrent Score-->", pscore)
                print("\nCurrent TEAM Score-->", pscore+total)
            time.sleep(1)
        else:
            print("Invalid Input")
            displayruns(0)
            print("\nCurrent Score-->", pscore)
            print("\nCurrent TEAM Score-->", pscore+total)
        i = i+1
    return pscore


def playingloft(balls, total):
    """
    playing cricket
    """
    # i = 1
    ground = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 0, 0, 0 ,"OUT"]
    lofted = [6, 4, 4, "OUT"]
    pscore = 0
    global i
    while i <= balls:
        grd = random.randint(0, 13)
        loft = random.randint(0, 3)
        print("\nBall:", i)
        pchoice = input(
            "press\nl. to play lofted shot\ng. to play grounded shot\n-->>")
        if pchoice == 'l':
            print("\n")
            time.sleep(0.5)
            displayruns(lofted[loft])
            if lofted[loft] == "OUT":
                i = i+1
                break
            else:
                pscore = pscore+lofted[loft]
                print("\nCurrent Score-->", pscore)
                print("\nCurrent TEAM Score-->", pscore+total)
            time.sleep(1)
        elif pchoice == 'g':
            print("\n")
            time.sleep(0.5)
            displayruns(ground[grd])
            if ground[grd] == "OUT":
                i = i+1
                break
            else:
                pscore = pscore+ground[grd]
                print("\nCurrent Score-->", pscore)
                print("\nCurrent TEAM Score-->", pscore+total)
            time.sleep(1)
        else:
            print("Invalid Input")
            displayruns(0)
            print("\nCurrent Score-->", pscore)
            print("\nCurrent TEAM Score-->", pscore+total)
        i = i+1
    return pscore


print("\n~~~~   VIRTUAL BOOK CRICKET ~~~~\n")
time.sleep(1)
print("This game is created by AMAAN KHAN\nEnjoy playing the game\n")
time.sleep(1)
# print("\n")
overs = int(input("How many overs would you like to play : "))
player = ["", "", "", "", "", "", "", "", "", "", ""]
playchoice = int(input(
    "Would you like to play with existing teams or you wanna create a new team?\npress\n1. to play with existing team\n2. to create a new team \n=>"))

if playchoice == 1:
    team = input("TEAM NAME : ")
    f1 = open(f"{team.upper()}.txt", "r")
    t = 0
    while t < 11:
        player[t] = f1.readline()
        t += 1
    f1.close()
elif playchoice == 2:
    team = input("TEAM NAME : ")
    f2 = open(f"{team.upper()}.txt", "a")
    t = 0
    while t < 11:
        player[t] = input(f"player {t+1}: ")
        f2.write(f"{player[t]}"+"\n")
        t += 1
    f2.close()
else:
    print("Invalid Input")


balls = 6*overs
pscore = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pballs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total = 0
k = 0
controls = int(input(
    "How would you like to play?\npress\n1. play shots on leg, off ,straight\n2. play lofted and grounded shots\n////// "))
if controls == 1:
    while k < 10 and i <= balls:
        time.sleep(1)
        a1 = i
        # pygame.mixer.music.load('crowd.mp3')
        # pygame.mixer.music.play()
        print("\n````````````````````````````````")
        print(f"On strike no.{k+1} - {player[k]}")
        pscore[k] = playingshots(balls, total)
        a2 = i
        # i = i+1
        pballs[k] = a2-a1
        print(f"{player[k][0:(len(player[k])-1)]} - {pscore[k]}({pballs[k]})")
        total = total+pscore[k]
        print(f"Score - {total}")
        k += 1
elif controls == 2:
    while k < 10 and i <= balls:
        time.sleep(1)
        a1 = i
        # pygame.mixer.music.load('crowd.mp3')
        # pygame.mixer.music.play()
        print("\n````````````````````````````````")
        print(f"On strike no.{k+1} - {player[k]}")
        pscore[k] = playingloft(balls, total)
        a2 = i
        # i = i+1
        pballs[k] = a2-a1
        print(f"{player[k][0:(len(player[k])-1)]} - {pscore[k]}({pballs[k]})")
        total = total+pscore[k]
        print(f" Team Score - {total}")
        k += 1

print("\n-------------SCORE----------------\n")

j = 0
f = open("Scorecard.txt", "a")
f.write("\n"+team.upper()+"\n")
while j < 10:
    print(player[j][0:(len(player[j])-1)], end=" - ")
    print(f"{pscore[j]}({pballs[j]})")
    f.write("\n"+player[j][0:(len(player[j])-1)] +
            " - "+str(pscore[j])+"("+str(pballs[j])+")")
    j += 1

f.write("\n")
print(f"Team total - {total}")
f.write(f"Team total - {total}")
f.close()
