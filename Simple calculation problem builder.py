import random

smallest = eval(input("请输入算术题的最小范围"))
bigest = eval(input("请输入算术题的最大范围"))
fun = input('Will fun gonna end?(input"y"or"n")')
right = 0


def panduan():
    global right
    global channe
    if answer == guest:
        print("答对了！")
        right = right + 1
        print("答对了", right, "题！")
    else:
        print("答错了！答案是", answer)
        channe = channe - 1
        print("剩下次数为", channe)
    return channe

def panduan2():
    global right
    global channe
    if plus2 == guest:
        print("答对了！")
        right = right + 1
        print("答对了", right, "题！")
    else:
        print("答错了！答案是", plus2)
        channe = channe - 1
        print("剩下次数为", channe)
    return channe

def MakeAnswer():
    global mode,plus1,plus2
    mode = random.randint(1, 4)
    plus1 = random.randint(smallest, bigest)
    plus2 = random.randint(smallest, bigest)
    return mode,plus1,plus2

while 'n' == fun:
    MakeAnswer()
    if mode == 1:

        answer = plus1 + plus2
        print(plus1, "+", plus2, end=" ")
        guest = eval(input("="))

        panduan()

    elif mode == 2:

        answer = plus1 * plus2  # 积=乘数*乘数
        print(plus1, "*", plus2, end=" ")
        guest = eval(input("="))

        panduan()

    elif mode == 3:

        beichushu = plus1 * plus2  # 被除数=商*除数
        print(beichushu, "÷", plus1, end=" ")
        guest = eval(input("="))

        panduan2()

    else:

        beijianshu = plus1 + plus2  # 被减数=差+减数
        print(beijianshu, "-", plus1, end=" ")
        guest = eval(input("="))

        panduan2()
    
    fun = input('Will fun gonna end?(input"y"or"n")')