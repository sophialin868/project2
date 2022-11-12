import random

def play_game(): 
    min=1
    max=100
    count=0
    random_value=random.randint(min,max)
    print(random_value)
    print("====猜數字遊戲")
    while True:
        count+=1
        keyin=int(input(f"猜數字的範圍{min}~{max}:"))
        if keyin>=min and keyin<=max:
            if (keyin==random_value):
                print(f"猜對了,答案是{random_value}")
                print(f"你猜了{count}次")
                break
            elif keyin>random_value:
                print("再小點")
                max=keyin-1
            elif keyin<random_value:
                print("再大點")
                min=keyin+1   
        else: 
            print("超出範圍")
    print("結束") 
if __name__=="__main__":
    while True:
        play_game()
        play_again=input("哩還要玩?(y.n)")
        if play_again=="n":
            break;