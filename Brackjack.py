import random

cardnum = ["1","2","3","4","5","6","7","8","9","T","J","Q","K"]
suit = ["H","S","D","C"]
decknum = ["a", "b", "c", "d", "e", "f"]


#EDIT
wallet=100000
bet_money=500
game_cnt_total=100
####


win=0
lose=0
draw=0
surrender=0
bj_cnt=0
double_cnt=0
split_cnt=0

deck=[]



def rest():
    print "rest of card:",len(deck)

#build of decks
def redeck(x):

    for i in decknum:
        for j in suit:
            for k in cardnum:
                strnum=str(i)+str(j)+str(k)
                x.append(strnum)
    return x

redeck(deck)
rest()

def card_distribute(x):
    hand=random.sample(deck, x)
    for i in hand:
        deck.remove(i)
    return hand


#Calculation
def card_num_change(x):
    hand_cal=[]
    for i in x:
        card_str=i[2:3]
        if card_str == "T" or card_str == "J" or card_str == "Q" or card_str == "K":
            card_str=10
        if card_str == "1":
            card_str=11
        hand_cal.append(int(card_str))
    return hand_cal

def A_count(x):
    return x.count(11)

def hand_sum(x):
    sumlist=sum(x)
    a_count=x.count(11)
    while sumlist>21 and a_count>0:
        sumlist -= 10
        a_count -= 1
    return sumlist
#Calculation//

def playerdraw(x,y,wallet,bet_money):
    deal_status=""
    double_f = False
    first_hit=True

    #bet
    wallet-=bet_money

    while deal_status=="" or deal_status=="hit":
        #print "p_hand:",x
        #p_hand_check
        if hand_sum(x)<=21:
            if hand_sum(x)>=17:
                deal_status="stay"
            elif hand_sum(x)==16 and y[0]==9 and first_hit==True and x[0]<>11 and x[1]<>11 and y[0]<>11:
                deal_status="surrender"
            elif hand_sum(x)==16 and y[0]==10 and first_hit==True and x[0]<>11 and x[1]<>11 and y[0]<>11:
                deal_status="surrender"
            elif hand_sum(x)==15 and y[0]==10 and first_hit==True and x[0]<>11 and x[1]<>11 and y[0]<>11:
                deal_status="surrender"
            elif hand_sum(x)>=13 and hand_sum(x)<=16:
                if y[0]>=7:
                    deal_status="hit"
                else:
                    deal_status="stay"

            elif hand_sum(x)==12:
                if y[0]>=7 or y[0]==2 or y[0]==3:
                    deal_status="hit"
                else:
                    deal_status="stay"
            elif hand_sum(x)==10:
                if y[0]==11 or y[0]==10:
                    deal_status="hit"
                else:
                    if first_hit==True:
                        deal_status="double"
                        wallet-=bet_money
                        first_hit=False
                        double_f=True
                    else:
                        deal_status="hit"
            elif hand_sum(x)==11:
                if y[0]==11:
                    deal_status="hit"
                else:
                    if first_hit==True:
                        deal_status="double"
                        wallet-=bet_money
                        first_hit=False
                        double_f=True
                    else:
                        deal_status="hit"
            else:
                deal_status="hit"
        else:

            deal_status="burst"

        if deal_status=="hit":#Plus one card
            p_next_card=card_num_change(card_distribute(1))
            x.append(p_next_card[0])

        first_hit=False
        print "Deal?:",deal_status

    #deal_check(double)
    if deal_status=="double":
        p_next_card=card_num_change(card_distribute(1))
        x.append(p_next_card[0])

        if hand_sum(x)>21:
            deal_status=="burst"

        #print "p_hand:",x
        deal_status="stay"

    #deal_check
    if deal_status=="stay":
        #dealer draw
        while hand_sum(y)<=16:
            d_next_card=card_num_change(card_distribute(1))
            y.append(d_next_card[0])
            #print "d_hand:",y

        if hand_sum(y)>21:
            game_result="win"
        else:
            if hand_sum(y)>hand_sum(x):
                game_result="lose"
            elif hand_sum(y)<hand_sum(x):
                game_result="win"
            elif hand_sum(y)==hand_sum(x):
                if len(x)==2 and hand_sum(x)==21 and len(y)<>2:
                    game_result="win"
                else:
                    game_result="draw"
    elif deal_status=="burst":
        game_result="lose"
    elif deal_status=="surrender":
        game_result="surrender"


    if game_result=="win":
        if double_f==True:
            wallet+=bet_money*4
        elif len(x)==2 and hand_sum(x)==21:
            wallet+=bet_money*2.5    
        else:
            wallet+=bet_money*2
    elif game_result=="draw":
        wallet+=bet_money
    elif game_result=="surrender":
        wallet+=bet_money/2


    #return x,y,deal_status,game_result,double_f
    return x,y,double_f,game_result,wallet

game_cnt=0

#game start
while game_cnt<game_cnt_total:

    #reset
    d_hand_cal=[]
    p_hand_cal=[]

    p_hand_cal_s1=[]
    p_hand_cal_s2=[]

    deal_status=""
    split_f = False
    double_f = False
    first_hit=True


    #redeck
    if len(deck)<30:
        deck=[]
        redeck(deck)

    d_hand_cal = card_num_change(card_distribute(2))
    p_hand_cal = card_num_change(card_distribute(2))

    print p_hand_cal,hand_sum(p_hand_cal),"Acnt:",A_count(p_hand_cal)
    print d_hand_cal,hand_sum(d_hand_cal),"Acnt:",A_count(d_hand_cal)


    #split check
    if p_hand_cal[0]==p_hand_cal[1]:
        if p_hand_cal[0]==2 or p_hand_cal[0]==3 or p_hand_cal[0]==7:
            if d_hand_cal[0] >= 8:
                split_f = False
            else:
                split_f = True
        if p_hand_cal[0]==4:
            if d_hand_cal[0]==5 or d_hand_cal[0]==6:
                split_f = True
            else:
                split_f = False
        if p_hand_cal[0]==6:
            if d_hand_cal[0] >= 7:
                split_f = False
            else:
                split_f = True
        if p_hand_cal[0]==9:
            if d_hand_cal[0]==7 or d_hand_cal[0]==10 or d_hand_cal[0]==11:
                split_f = False
            else:
                split_f = True
        if p_hand_cal[0]==5 or p_hand_cal[0]==10:
            split_f = False
        if p_hand_cal[0]==8 or p_hand_cal[0]==11:
            split_f = True
    #//split check

    print "Split:",split_f
    if split_f==True:
        split_cnt+=1

    #Player draw
    if split_f==False:
        deal_status=playerdraw(p_hand_cal,d_hand_cal,wallet,bet_money)

        p_hand_cal=deal_status[0]
        d_hand_cal=deal_status[1]
        double_f=deal_status[2]
        game_result=deal_status[3]
        wallet=deal_status[4]

        if game_result=="win":
            win +=1
            if len(p_hand_cal)==2 and hand_sum(p_hand_cal)==21:
                bj_cnt+=1 
        elif game_result=="lose":
            lose +=1
        elif game_result=="draw":
            draw +=1
        elif game_result=="surrender":
            surrender +=1

        if double_f==True:
            double_cnt +=1

    else:

        p_hand_cal_s1.append(p_hand_cal[0])
        p_hand_cal_s2.append(p_hand_cal[1])

        p_next_card=card_num_change(card_distribute(1))
        p_hand_cal_s1.append(p_next_card[0])
        p_next_card=card_num_change(card_distribute(1))
        p_hand_cal_s2.append(p_next_card[0])

        deal_status=playerdraw(p_hand_cal_s1,d_hand_cal,wallet,bet_money)

        p_hand_cal_s1=deal_status[0]
        d_hand_cal=deal_status[1]
        double_f=deal_status[2]
        game_result=deal_status[3]
        wallet=deal_status[4]

        if game_result=="win":
            win +=1
            if len(p_hand_cal_s1)==2 and hand_sum(p_hand_cal_s1)==21:
                bj_cnt+=1 
        elif game_result=="lose":
            lose +=1
        elif game_result=="draw":
            draw +=1
        elif game_result=="surrender":
            surrender +=1

        if double_f==True:
            double_cnt +=1

        deal_status=playerdraw(p_hand_cal_s2,d_hand_cal,wallet,bet_money)

        p_hand_cal_s2=deal_status[0]
        d_hand_cal=deal_status[1]
        double_f=deal_status[2]
        game_result=deal_status[3]
        wallet=deal_status[4]

        if game_result=="win":
            win +=1
            if len(p_hand_cal_s2)==2 and hand_sum(p_hand_cal_s2)==21:
                bj_cnt+=1 
        elif game_result=="lose":
            lose +=1
        elif game_result=="draw":
            draw +=1
        elif game_result=="surrender":
            surrender +=1

        if double_f==True:
            double_cnt +=1


    game_cnt+=1

    print "---result---"
    if split_f==False:
        print "last_p_hand:",p_hand_cal,hand_sum(p_hand_cal)
    else:
        print "last_p_hand_s1:",p_hand_cal_s1,hand_sum(p_hand_cal_s1)
        print "last_p_hand_s2:",p_hand_cal_s2,hand_sum(p_hand_cal_s2)
    print "last_d_hand:",d_hand_cal,hand_sum(d_hand_cal)
    print game_result
    print "win:",win,"(BJ:",bj_cnt,") lose:",lose," draw:",draw," surrender:",surrender
    print "split:",split_cnt,"double:",double_cnt
    print "game_cnt:",game_cnt
    print "wallet:",wallet
    rest()
    print "----------------------"
