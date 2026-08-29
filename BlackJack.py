import random          # random is a standard-library module and we will use shuffle() func from random below.

cards = []   
suits = ["Hearts","Diamonds","Clubs","Spades"]
ranks = ["A","2","3","4","5","6","7","8","9","10","K","J","Q",]

for suit in suits:
    for rank in ranks:
        #print([suit,rank])      # It will print everything in Lists.
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []

    for each in range(number):
        card = cards.pop()
        cards_dealt.append(card)
        
    return cards_dealt 


shuffle()
player_cards_dealt = deal(2)
dealer_cards_dealt = deal(2)

cards_with_values_player = []
ace_count_player = 0
total_value_player = 0

for card in player_cards_dealt:     # take each card one by one from player_cards_dealt

        rank = card[1]
        if rank=="A":
            value =11
            ace_count_player = ace_count_player + 1 
        elif rank == "K" or rank=="J" or rank == "Q":
            value = 10
        else:
            value = int(rank)

        rank_dict = {"rank": rank , "value": value}

        cards_with_values_player.append(rank_dict)
        total_value_player = total_value_player + rank_dict["value"]

while (total_value_player > 21) and (ace_count_player > 0):
    total_value_player = total_value_player - 10
    ace_count_player = ace_count_player - 1


cards_with_values_dealer = []
ace_count_dealer = 0
total_value_dealer = 0

for card in dealer_cards_dealt:     # take each card one by one from dealer_cards_dealt

        rank = card[1]
        if rank=="A":
            value =11
            ace_count_dealer = ace_count_dealer + 1 
        elif rank == "K" or rank=="J" or rank == "Q":
            value = 10
        else:
            value = int(rank)

        rank_dict = {"rank": rank , "value": value}

        cards_with_values_dealer.append(rank_dict)
        total_value_dealer = total_value_dealer + rank_dict["value"]

while (total_value_dealer > 21) and (ace_count_dealer > 0):
    total_value_dealer = total_value_dealer - 10
    ace_count_dealer = ace_count_dealer - 1



print("PLAYER:", cards_with_values_player)
print("PLAYER TOTAL:", total_value_player)

print("DEALER:", cards_with_values_dealer[0])
print("DEALER SECOND CARD IS HIDDEN\n")
# print("DEALER TOTAL:", total_value_dealer)


if total_value_player == 21 and total_value_dealer == 21:
    print("BOTH HAVE BLACKJACK")
    print("PUSH! IT'S A DRAW.")

elif total_value_player == 21:
    print("PLAYER WINS THE GAME WITH BLACKJACK")

elif total_value_dealer == 21:
    print("DEALER WINS THE GAME WITH BLACKJACK")


else:
    while True:    # if the total is below 21 after a HIT, none of the breaks execute, so the while True: starts another iteration and asks again to Hit or Stand.

        choice = input("Do you want to Hit or Stand? ").upper()

        if choice == "HIT":

                    print("PLAYER CHOSE HIT\n")
                    new_card_player = deal(1)
                    new_card = new_card_player[0]
                    print("New card player got: ", new_card)
                    rank = new_card[1]

                    if rank=="A":
                        value =11
                        ace_count_player = ace_count_player + 1 
                    elif rank == "K" or rank=="J" or rank == "Q":
                        value = 10
                    else:
                        value = int(rank)

                    rank_dict_new = {"rank": rank , "value": value}
                    cards_with_values_player.append(rank_dict_new)
                    total_value_player = total_value_player + rank_dict_new["value"]
                    
                    while (total_value_player > 21) and (ace_count_player > 0):
                        total_value_player = total_value_player - 10
                        ace_count_player = ace_count_player - 1

                    print("Now, Player have: ",cards_with_values_player)    
                    print("Player Total: ",total_value_player)

                    if total_value_player > 21:
                        print("\nBUST! PLAYER LOSES. \nDEALER WINS")
                        break
                    elif total_value_player == 21:
                        print("Player has 21")
                        break

        elif choice == "STAND":
            print("PLAYER CHOSE STAND\n")
            break

        else:
            print("INVALID INPUT")

        #Player Logic ended here.


    if total_value_player <= 21:
        
        print("DEALER'S TURN")
        print("DEALER:", cards_with_values_dealer)
        print("DEALER TOTAL:", total_value_dealer)

        while (total_value_dealer < 17):
                
                print("DEALER HITS AS TOTAL IS LESS THAN 17 \n")

                new_card_dealer = deal(1)   #it returns a list
                new_card = new_card_dealer[0]   # list is extracted and formed a comma seperated value
                rank= new_card[1]     # rank is extracted using indexing
                print("New card dealer got: ", new_card)

                if rank=="A":
                    value =11
                    ace_count_dealer = ace_count_dealer + 1 
                elif rank == "K" or rank=="J" or rank == "Q":
                    value = 10
                else:
                    value = int(rank)
                
                rank_dict_new = {"rank": rank , "value": value}
                cards_with_values_dealer.append(rank_dict_new)
                total_value_dealer = total_value_dealer + rank_dict_new["value"]
                    
                while (total_value_dealer > 21) and (ace_count_dealer > 0):    # Ace adjustment of dealer
                    total_value_dealer = total_value_dealer - 10
                    ace_count_dealer = ace_count_dealer - 1

                print("So, Now Dealer have :", cards_with_values_dealer)
                print("New Total of Dealer :", total_value_dealer)


        if total_value_dealer <= 21:
            print("DEALER STANDS\n")
            print("FINAL PLAYER TOTAL", total_value_player)
            print("FINAL DEALER TOTAL:", total_value_dealer)      


        if total_value_dealer > 21:
             print("\nPLAYER WINS! DEALER BUSTED.")

        elif total_value_player > total_value_dealer:
            print("\nPLAYER WINS!")

        elif total_value_dealer > total_value_player:
            print("\nDEALER WINS!")

        else:
            print("\nPUSH! IT'S A DRAW.")


                    
