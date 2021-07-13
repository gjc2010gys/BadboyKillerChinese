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
            print('Input Wrong!You only can input int number!')
        else:
            Wrong =  False
    return temp

def CheckAnswer(InputRabbit,InputChiken,Rabbit,Chiken):
    if InputChiken == Chiken:
        print("The number of chickens is correct!")
    else:
        print("The number of chickens is not correct!There are "+str(chiken)+"in the cage.")

    if InputRabbit == rabbit:
        print("The number of rabbit is correct!")
    else:
        print("The number of rabbit is not correct!There are "+str(rabbit)+"in the cage.")

while True:
    MakeAnswer()
    print("There are "+str(chiken+rabbit)+" animal in the cage.There are "+str(ChikenLeg+RabbitLeg)+" Legs on the floor.")
    CheckWrong('How many rabbit are there in the cage?')
    InputRabbit = temp
    CheckWrong('How many Chiken are there in the cage?')
    InputChiken = temp
    CheckAnswer(InputRabbit,InputChiken,rabbit,chiken)
