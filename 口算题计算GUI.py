import easygui,random
from os import system

def CheckWrong(InputSay,ERROR=ValueError,WrongSay='输入错误，你只能输入整数！',):
    Wrong = True
    global temp
    while Wrong:
        try:
            temp = int(easygui.enterbox(InputSay))
        except ERROR:
            easygui.msgbox(WrongSay)
        else:
            Wrong =  False
    return temp

CloseDesktop = easygui.ccbox(msg="是否关闭桌面？桌面会在答完指定题量后自动恢复。",title="是否关闭桌面？",choices=('关！整死这个小兔崽子！','不关！我桌面还要用！'))

if CloseDesktop:
    system('TASKKILL /IM explorer.exe /F')

CheckWrong("请输入算术题的最小范围：")
smallest = temp
CheckWrong("请输入算术题的最大范围：")
bigest = temp
CheckWrong("应该答多少题后让他自由呢？：")
channe = temp

def CheckAnswer(answer,guest):
    global channe
    if guest == answer:
        channe = channe - 1
        easygui.msgbox(f"正确，你还需要再答{channe}题！")
    else:
        easygui.msgbox(f"错误！答案为{answer}!你还需要再答{channe}题！")
    return channe

while channe > 0:
    mode = random.randint(1, 4)
    plus1 = random.randint(smallest, bigest)
    plus2 = random.randint(smallest, bigest)

    if mode == 1:
        answer = plus1 + plus2
        CheckWrong(str(plus1)+'+'+str(plus2)+'=')
        guest = temp
        CheckAnswer(answer,guest)

    elif mode == 2:
        answer = plus1 * plus2  # 积=乘数*乘数
        CheckWrong(str(plus1)+'*'+str(plus2)+'=')
        guest = temp
        CheckAnswer(answer,guest)

    elif mode == 3:
        beichushu = plus1 * plus2
        answer = plus1  # 被除数=商*除数
        CheckWrong(str(beichushu)+'÷'+str(plus2)+'=')
        guest = temp
        CheckAnswer(answer,guest)

    else:
        beijianshu = plus1 + plus2  # 被减数=差+减数
        answer = plus1
        CheckWrong(str(beijianshu)+'-'+str(plus2)+'=')
        guest = temp
        CheckAnswer(answer,guest)

if CloseDesktop:
    easygui.msgbox("恭喜你答完了，正在打开桌面......")
    system('C:\\Windows\\explorer.exe')
else:
    easygui.msgbox("恭喜你答完了，正在退出......")