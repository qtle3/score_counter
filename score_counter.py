# This program simulates game scoring.

def main() :
    #enter name of players
    playerA = input("Give the name of the first player: ")
    playerB = input("Give the name of the second player: ")

    scoreA = 0
    scoreB = 0
    #score counter
    while not((scoreA >= 15 and scoreA - scoreB >= 2) or 
              (scoreB >= 15 and scoreB - scoreA >= 2) or
              (scoreA == 7 and scoreB == 0) or 
              (scoreB == 7 and scoreA == 0)):
        #continue playing
        print("Current score:",playerA,scoreA,"|",playerB,scoreB)
        point_winner = input("Who won the point? ")
        if point_winner==playerA :
            scoreA += 1
        elif point_winner==playerB :
            scoreB += 1
        else :
            print("Incorect player name given. Please give",playerA,"or",playerB+".")
    #display winner
    if scoreA > scoreB :
        print(playerA,"is the winner!")
    else :
        print(playerB,"is the winner!")
main()


    
    
