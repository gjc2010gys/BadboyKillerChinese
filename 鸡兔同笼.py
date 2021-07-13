import random

def MakeAnswer():
    global chiken,rabbit,ChikenLeg,RabbitLeg
    chiken = random.randint(1,20)
    rabbit = random.randint(1,20)
    ChikenLeg = chiken * 2
    RabbitLeg = rabbit * 4
    return chiken,rabbit,ChikenLeg,RabbitLeg

def CheckWrong(InputSay):
    Wrong = True
    global temp
    while Wrong:
        try:
            temp = int(input(InputSay))
        except ValueError:
            print('输入错误，你只能输入整数！')
        else:
            Wrong =  False
    return temp

def CheckAnswer(InputRabbit,InputChiken,Rabbit,Chiken):
    if InputChiken == Chiken:
        print("鸡的数量正确！")
    else:
        print("鸡的数量正确！!实际上有"+str(chiken)+"只鸡在笼子里！.")

    if InputRabbit == rabbit:
        print("兔子的数量正确！")
    else:
        print("兔子的数量正确！!实际上有"+str(chiken)+"只兔子在笼子里！.")

while True:
    MakeAnswer()
    print("笼子里有"+str(chiken+rabbit)+"个头.有"+str(ChikenLeg+RabbitLeg)+"只腿在地上.")
    CheckWrong('有多少兔子在笼子里?')
    InputRabbit = temp
    CheckWrong('有多少鸡在笼子里?')
    InputChiken = temp
    CheckAnswer(InputRabbit,InputChiken,rabbit,chiken)
