import random
ticket=[3,4,1,2,9,7,1,8,5,6,"y","s","z","m","x"]
zj_ticket=random.sample(ticket,5)
print("中奖号码是：",zj_ticket)
my_ticket=[]
cj_count=0
while True:
    for i in range(5):
        my_ticket.append(random.choice(ticket))
    # print("我的号码是：",my_ticket)
    if my_ticket==zj_ticket:
        print(f"中奖了！共尝试了{cj_count}次")
        break
    else:
        cj_count+=1
        my_ticket.clear()
