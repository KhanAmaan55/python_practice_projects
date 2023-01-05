import time
print("-----------------VOTING SYSTEM-----------------")
candidate1 = input("Enter The name of first candidate: ")
sym1 = input("Enter the charecter/number/alphabet for first candidate: ")
print()
candidate2 = input("Enter The name of second candidate: ")
sym2 = input("Enter the charecter/number/alphabet for second candidate: ")

canvote1 = 0
canvote2 = 0

voter_id = ["1","2","3","4","5","6","7","8","9","0"]
voters = len(voter_id)
print()
print(f"There are total {voters} voters")
print("So lets begin the Election")

while True:
    if voter_id == []:
        print()
        print("Voting is completed succesfully!!!")
        print("And the results are:")
        print()
        time.sleep(3)
        if canvote1 > canvote2:
            percan = (canvote1/voters)*100
            print(f"{candidate1} Has Won The Election with {percan}%")
        elif canvote2 > canvote1:
            percan = (canvote2/voters)*100
            print(f"{candidate2} Has Won The Election with {percan}%")
        else:
            print("Its a TIE!!!")
        break
    else:
        print()
        rem_id = input("Enter your voter id: ")
        if rem_id in voter_id:
            voter_id.remove(rem_id)
            print("------------------------------------")
            print(f"To Vote {candidate1} press {sym1}: ")
            print(f"To Vote {candidate2} press {sym2}: ")
            print("------------------------------------")
            vote = input("Enter your precious vote: ")
            if vote == sym1:
                canvote1 +=1
                print("Thank You for voting!!!")
            elif vote == sym2:
                canvote2 +=1
                print("Thank You for voting!!!")
            else:
                print("You press wrong symbol")
        else:
            print("You had already voted OR You are not a voter")