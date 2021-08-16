import random,easygui,os,sys

def make_need():
    global left,right,fh,answer
    left = random.randint(1,biggest)
    right = random.randint(1,biggest)
    fh = random.randint(1,4)
    if fh == 1 or fh == 2:
        answer = left + right
    else:
        answer = left * right
    return left,right,fh,answer

def Safty_get(word,title_word):
    global input_thing
    Wrong = True
    while Wrong:
        try:
            input_thing = int(easygui.enterbox(msg=word,title=title_word))
        except ValueError:
            easygui.msgbox(msg='输入错误，请重新输入！',title="输入错误！")
        except TypeError:
            easygui.msgbox(msg='请不要点击Cancel或尝试关闭本程序，请重新输入！',title="输入错误！")
        else:
            Wrong = False
    return input_thing

def get_answer(fh,answer,left,right):
    global enter
    if fh == 1:
        fh_str = "+"
    elif fh == 2:
        fh_str = '-'
    elif fh == 3:
        fh_str = '*'
    else:
        fh_str = '÷'
    if fh == 4 or fh == 2: 
        output_word = "请输入答案:\n" + str(answer) + fh_str + str(left) + "="
    else:
        output_word = "请输入答案:\n" + str(left) + fh_str + str(right) + "="

    Safty_get(word=output_word,title_word="请输入！")
    enter = input_thing
    return enter

def CheckAnswer(answer,enter):
    global time
    if fh == 4 or fh == 2:
        if enter == right:
            time -= 1
            easygui.msgbox(msg="好样的！你成功答对了这题！你还剩下"+str(time)+'题就结束了。',title='好样的！',ok_button='下一题！')
        elif CF_mode:
            time += 1
            easygui.msgbox(msg="你答错了这题！，正确答案为"+str(right)+'.你还剩下'+str(time)+'题就结束了。',title='失败！',ok_button='下一题！')
        else:
            easygui.msgbox(msg="你答错了这题！，正确答案为"+str(right)+'.你还剩下'+str(time)+'题就结束了。',title='失败！',ok_button='下一题！')
    else:
        if enter == answer:
            time -= 1
            easygui.msgbox(msg="好样的！你成功答对了这题！你还剩下"+str(time)+'题就结束了。',title='好样的！',ok_button='下一题！')
        elif CF_mode:
            time += 1
            easygui.msgbox(msg="你答错了这题！，正确答案为"+str(answer)+'.你还剩下'+str(time)+'题就结束了。',title='失败！',ok_button='下一题！')
        else:
            easygui.msgbox(msg="你答错了这题！，正确答案为"+str(answer)+'.你还剩下'+str(time)+'题就结束了。',title='失败！',ok_button='下一题！')

while True:
    easygui.msgbox(msg="欢迎使用BadBoyKiller口算题生成器GUI版本！",title="欢迎！")
    Safty_get(word="请问程序应该在答对多少题之后结束呢？",title_word="请输入")
    time = input_thing
    if time <= 0:
        easygui.msgbox(msg="你是想作弊吗？这是不可能的！已设置题目数量为100",title="警告！")
        time = 100
    Safty_get(word="请输入算式中的数字可能出现的最大值（最小值为10，若输入值小于10则自动分配！）：",title_word="请输入")
    if input_thing < 10:
        input_thing = random.randint(1,100)
        easygui.msgbox(msg="输入值小于10，已随机分配为"+str(input_thing)+"!",title="输入警告！")
    biggest = input_thing
    CF_mode = easygui.ccbox(msg="是否开启惩罚机制？开启时答题错误会自动增加所需要答题的数量！",title="惩罚机制。",choices=("开启","关闭"))
    while time > 0:
        make_need()
        get_answer(fh,answer,left,right)
        CheckAnswer(answer,enter)
    easygui.msgbox(msg="好样的，你已经成功答完了题目，点击下面的按钮来关闭本程序！",title='恭喜你！',ok_button='关闭本程序！')
    sys.exit()