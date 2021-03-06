from os import system, terminal_size
from random import randint
from tkinter.constants import TRUE
from easygui import msgbox,multenterbox,enterbox,ccbox

def Make():
    global x,y,fxbs,fybs,sxbs,sybs,fh,channe
    x = randint(1,10)
    y = randint(1,10)
    fxbs = randint(1,10)
    fybs = randint(1,10)
    sxbs = randint(1,10)
    sybs = randint(1,10)
    fh = randint(1,4)
    return x,y,fxbs,fybs,sxbs,sybs,fh,channe

def Get():
    global ix,iy,ClickCancel,NotType
    ClickCancel = False
    NotType = False
    try:
        ix = OutList[0]
        iy = OutList[1]
    except TypeError:
        msgbox("别点Cancel！此题作废！")
        ClickCancel = True
        return ClickCancel
    else:
        if ix == '' or iy == '':
            NotType = True
            msgbox('你是不是有空没有输入？记得每个空一定都要输入，别空着，此题作废！')
        return ix,iy,ClickCancel,NotType

def CheckAnswer(ix,iy,x,y):
    global channe
    if ix == str(x) and iy == str(y):
        channe -= 1
        msgbox('x正确.y正确.还需要答'+str(channe)+'次。',title='都正确！')
    elif ix != str(x) and iy == str(y):
        msgbox('x不正确,y正确。x为'+str(x)+'\n'+'\n'+'还需要答'+str(channe)+'次。',title='有错误！')
    elif ix == str(x) and iy != str(y):
        msgbox('y不正确,x正确。x为'+str(y)+'\n'+'\n'+'还需要答'+str(channe)+'次。',title='有错误！')
    else:
        msgbox('x和y都不正确。x为'+str(x)+','+'y为'+str(y)+'\n'+'\n'+'还需要答'+str(channe)+'次。',title='有错误！')

def OutPut(x,y,fxbs,fybs,sxbs,sybs,fh):
    global FirstAnswer,SecondAnswer,OutList

    if fh == 1:
        FirstAnswer = fxbs *x + fybs * y
        SecondAnswer = sxbs * x + sybs * y
        OutStr = str(fxbs)+'x + '+str(fybs)+'y = ' +str(FirstAnswer)+' \n' + str(sxbs)+'x + ' + str(sybs)+'y = '+str(SecondAnswer) + '\n输入后请点击OK'
        OutList = multenterbox(OutStr,title='输入',fields=['x','y'])
    elif fh == 2:
        FirstAnswer = fxbs *x - fybs * y
        SecondAnswer = sxbs * x - sybs * y
        OutStr = str(fxbs)+'x - '+str(fybs)+'y = ' +str(FirstAnswer)+' \n' + str(sxbs)+'x - ' + str(sybs)+'y = '+str(SecondAnswer) + '\n输入后请点击OK'
        OutList = multenterbox(OutStr,title='输入',fields=['x','y'])
    elif fh ==3:
        FirstAnswer = fxbs *x + fybs * y
        SecondAnswer = sxbs * x - sybs * y
        OutStr = str(fxbs)+'x + '+str(fybs)+'y = ' +str(FirstAnswer)+' \n' + str(sxbs)+'x - ' + str(sybs)+'y = '+str(SecondAnswer) + '\n输入后请点击OK'
        OutList = multenterbox(OutStr,title='输入',fields=['x','y'])
    else:
        FirstAnswer = fxbs *x - fybs * y
        SecondAnswer = sxbs * x + sybs * y
        OutStr = str(fxbs)+'x - '+str(fybs)+'y = ' +str(FirstAnswer)+' \n' + str(sxbs)+'x + ' + str(sybs)+'y = '+str(SecondAnswer) + '\n输入后请点击OK'
        OutList = multenterbox(OutStr,title='输入',fields=['x','y'])

    return FirstAnswer,SecondAnswer,OutList

if __name__ == '__main__':
    Wrong = True
    Close = ccbox(msg='是否先关闭桌面?桌面会在答完题目后自动回复。',title='关闭桌面？',choices=('关掉关掉!一定要关掉!','打开打开！一定要打开！'))
    if Close:
        system('TASKKILL /F /IM explorer.exe')
    while Wrong:
        try:
            channe = int(enterbox(msg='应该答对多少题后结束呢？',title='请输入:'))
        except TypeError:
            msgbox(msg='别点Cancel！请重新输入！',title='输入错误！')
        except ValueError:
            msgbox(msg='输入错误！你只能输入一个正整数！请重新输入！',title='输入错误！')
        else:
            Wrong = False
    while channe > 0:
        Make()
        OutPut(x,y,fxbs,fybs,sxbs,sybs,fh)
        Get()
        if ClickCancel or NotType:
            continue
        CheckAnswer(ix,iy,x,y)
    
    if Close:
        msgbox("恭喜你答完了所有的题！正在恢复桌面。。。。。。")
        system('C:/Windows//explorer.exe')
    else:
        msgbox('恭喜你答完了所有的题！正在退出。。。。。。')