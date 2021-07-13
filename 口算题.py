import random

def panduan():
    global right
    global channe
    if answer == guest:
        print("正确！")
        right = right + 1
        print("你已经答对了", right, "题！")
    else:
        print("错误！答案为", answer)
    return right

def panduan2():
    global right
    global channe
    if plus2 == guest:
        print("正确！")
        right = right + 1
        print("你已经答对了", right, "题！")
    else:
        print("错误！答案为", plus2)
    return right

def MakeAnswer():
    global mode,plus1,plus2
    mode = random.randint(1, 4)
    plus1 = random.randint(smallest, bigest)
    plus2 = random.randint(smallest, bigest)
    return mode,plus1,plus2

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


CheckWrong("请输入答案的最小值：")
smallest = temp
CheckWrong("请输入答案的最大值：")
bigest = temp
right = 0

while True:
    MakeAnswer()
    if mode == 1:

        answer = plus1 + plus2
        Output = str(plus1)+ "+"+str(plus2)+'='
        CheckWrong(Output)
        guest = temp
        panduan()

    elif mode == 2:

        answer = plus1 * plus2  # 积=乘数*乘数
        Output = str(plus1)+ "*"+str(plus2)+'='
        CheckWrong(Output)
        guest = temp
        panduan()

    elif mode == 3:

        beichushu = plus1 * plus2  # 被除数=商*除数
        Output = str(beichushu)+ "÷"+str(plus1)+'='
        CheckWrong(Output)
        guest = temp

        panduan2()

    else:

        beijianshu = plus1 + plus2  # 被减数=差+减数
        Output = str(beijianshu)+ "-"+str(plus1)+'='
        CheckWrong(Output)
        guest = temp
        panduan2()