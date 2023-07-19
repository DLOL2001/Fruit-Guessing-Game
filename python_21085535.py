#MasterMind Board Game

#Set Up Replayability
ply_again='Y'
while ply_again=='Y' or ply_again=='y':

    #Initialization (Answer & Attempts)
    import random
    ans_lst=[]
    user_ans=[1,2,3,4]
    frts=['apple','orange','banana','grape','mango','pear','kiwi','durian','papaya','lemon']
    
    attempts=0

    for i in range(0,4):
        ans_lst.append(random.choice(frts))
    
    #Introduction
    print('Welcome to the on-screen version of...')
    print('||==================================||')
    print('||   !! Master Mind Board Game !!   ||')
    print('||==================================||')
    print('||    Guess 4 Fruits Correctly in   ||')
    print('||       the Correct Sequence.      ||')
    print('||                                  ||')
    print('||         Infinite Attempts        ||')
    print('||                                  ||')
    print('||     Beware of Duplicate Fruits   ||')
    print('||==================================||')
    print('||      !! Available Fruits !!      ||')
    print('||==================================||')
    print('||        Apple Orange Banana       ||') 
    print('||       Grape Mango Pear Kiwi      ||')
    print('||        Durian Papaya Lemon       ||')
    print('||==================================||')
    print()

    #Game Begins
    while ans_lst!=user_ans:

        #User's Guesses
        def user_guesses():
            place=1
            for i in range(0,4):
                user_guess=input('Enter Your Place '+str(place)+' Fruit (Singular Form):')
                user_ans[i]=user_guess.strip()
                place=place+1

            for i in range(len(user_ans)):
                user_ans[i]=user_ans[i].lower()
                
            print()
            print('Your Guesses Are:',user_ans)
            print()
            return user_ans

        user_ans=user_guesses()

        #Correct/Wrong Fruits
        def chk_ans():
            t_lst=[]
            t_lst.insert(0,ans_lst[0])
            t_lst.insert(1,ans_lst[1])
            t_lst.insert(2,ans_lst[2])
            t_lst.insert(3,ans_lst[3])
            
            idx_cnt1=0
            crt_frt=0
            wrg_frt=0
    
            while idx_cnt1<=3:
                
                if user_ans[idx_cnt1]==t_lst[0]:
                    crt_frt=crt_frt+1
                    t_lst[0]='done'
                    
                elif user_ans[idx_cnt1]==t_lst[1]:
                    crt_frt=crt_frt+1
                    t_lst[1]='done'
                    
                elif user_ans[idx_cnt1]==t_lst[2]:
                    crt_frt=crt_frt+1
                    t_lst[2]='done'
                    
                elif user_ans[idx_cnt1]==t_lst[3]:
                    crt_frt=crt_frt+1
                    t_lst[3]='done'
                    
                else:
                    wrg_frt=wrg_frt+1

                idx_cnt1=idx_cnt1+1
        
            return crt_frt,wrg_frt

        crt_frt,wrg_frt=chk_ans()   

        #Correct Fruits in Correct Places
        idx_cnt2=0
        crt_plc=0
        
        for i in range(0,4):
            
            if user_ans[idx_cnt2]==ans_lst[idx_cnt2]:
                crt_plc=crt_plc+1
                
            idx_cnt2=idx_cnt2+1

        #User's Performance
        print('||==================================||')
        print('||        !! Your Score !!          ||')
        print('||==================================||')
            
        print()
        print('Correct Fruits:',crt_frt)
        print('Wrong Fruits:',wrg_frt)
        print('Correct Fruits in Correct Place:',crt_plc)
        print('Correct Fruits in Wrong Place:',4-crt_plc-wrg_frt)
        print()        

        #User's Attempts Counter
        attempts=attempts+1

    #Congratz Message
    print('Congrats! You took '+str(attempts)+' attempts to get it right.')

    #Replay
    ply_again=input('Play Again? (y/n):')
    print()

#GoodBye Message
print('See You Soon!')
