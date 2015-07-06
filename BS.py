import random

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
dice3 = [1,2,3,4,5,6]

ini_wallet=30000
bet_money=100
Target_money=30500
game_cnt_total=100
try_cnt_total=10000

wallet=ini_wallet
current_bet_money=bet_money

big_cnt=0
small_cnt=0
big_f=False
small_f=False
small_continue=0
big_continue=0
small_array=[]
big_array=[]

game_cnt=0
try_cnt=0

success_game=0
fatal_game=0

#game start
while try_cnt<try_cnt_total:

    while game_cnt<game_cnt_total and wallet<Target_money and wallet>0:

        diceshowing=random.sample(dice1, 1) + random.sample(dice2, 1) + random.sample(dice3, 1)

        wallet-=current_bet_money

        if sum(diceshowing) < 11:
            small_cnt += 1

            if small_f==True:
                small_continue+=1
                small_array.append(small_continue)

            if big_f==True:
                big_f=False

     
                big_continue=0
          
            small_f=True

        else:
            big_cnt += 1

            if big_f==True:
                big_continue+=1
                big_array.append(big_continue)

            if small_f==True:
                small_f=False

     
                small_continue=0
          
            big_f=True


        #result check
        if big_f==True:
            wallet+=current_bet_money*2
            current_bet_money = bet_money
        else:
            current_bet_money = current_bet_money*2

        #print sum(diceshowing), wallet, current_bet_money


        game_cnt+=1

    if wallet>0:
        success_game+=1
        current_bet_money = bet_money
        wallet=ini_wallet
        big_f=False
        small_f=False
        small_continue=0
        big_continue=0
    else:
        fatal_game+=1
        current_bet_money = bet_money
        wallet=ini_wallet
        big_f=False
        small_f=False
        small_continue=0
        big_continue=0
    try_cnt+=1



#print big_array
#print sum(big_array)
#print small_array
#print sum(small_array)
print "small_cnt:", small_cnt
print "big_cnt:", big_cnt
print "success_game:", success_game
print "fatal_game:", fatal_game
print "small_max_cnt:", max(small_array)
print "big_max_cnt:", max(big_array)

print "wallet:", wallet
