from os import system
from random import randint
from easygui import ccbox,enterbox,msgbox

stop = 'n'
Wrong = True

class Programme(object):
    def output(x,y,sxbs,sybs,fxbs,fybs,fh):
        global ix,iy
        if fh == 0:
            CheckWrong(str(fxbs)+'x'+'+'+str(fybs)+'y'+'='+str(fjg)+'\n'+str(sxbs)+'x'+'+'+str(sybs)+'y'+'='+str(sjg)+'\n'+'\n'+'请输入x:')
            ix = temp
            CheckWrong(str(fxbs)+'x'+'+'+str(fybs)+'y'+'='+str(fjg)+'\n'+str(sxbs)+'x'+'+'+str(sybs)+'y'+'='+str(sjg)+'\n'+'\n'+'请输入y:')
            iy = temp
        elif fh == 1:
            CheckWrong(str(fxbs)+'x'+'-'+str(fybs)+'y'+'='+str(fjg)+'\n'+str(sxbs)+'x'+'-'+str(sybs)+'y'+'='+str(sjg)+'\n'+'\n'+'请输入x:')
            ix = temp
            CheckWrong(str(fxbs)+'x'+'-'+str(fybs)+'y'+'='+str(fjg)+'\n'+str(sxbs)+'x'+'-'+str(sybs)+'y'+'='+str(sjg)+'\n'+'\n'+'请输入y:')
            iy = temp
        elif fh == 2:
            CheckWrong(str(fxbs)+'x'+'-'+str(fybs)+'y'+'='+str(fjg)+'\n'+str(sxbs)+'x'+'+'+str(sybs)+'y'+'='+str(sjg)+'\n'+'\n'+'请输入x:')
            ix = temp
            CheckWrong(str(fxbs)+'x'+'-'+str(fybs)+'y'+'='+str(fjg)+'\n'+str(sxbs)+'x'+'+'+str(sybs)+'y'+'='+str(sjg)+'\n'+'\n'+'请输入y:')
            iy =temp
        elif fh == 3:
            CheckWrong(str(fxbs)+'x'+'+'+str(fybs)+'y'+'='+str(fjg)+'\n'+str(sxbs)+'x'+'-'+str(sybs)+'y'+'='+str(sjg)+'\n'+'\n'+'请输入x:')
            ix = temp
            CheckWrong(str(fxbs)+'x'+'+'+str(fybs)+'y'+'='+str(fjg)+'\n'+str(sxbs)+'x'+'-'+str(sybs)+'y'+'='+str(sjg)+'\n'+'\n'+'请输入y:')
            iy = temp
        return ix,iy

    def make():
        global x,y,xbs,ybs,fh,fxbs,fybs,sxbs,sybs
        x = randint(1,10)
        y = randint(1,10)
        fxbs = randint(1,5)
        fybs = randint(1,5)
        sxbs = randint(1,5)
        sybs = randint(1,5)
        fh = randint(0,3)
        return x,y,fxbs,fybs,fh,sybs,sxbs

    def pd(x,y,ix,iy):
        if ix == x and iy == y:
            msgbox('x正确.y正确.')
        elif ix != x and iy == y:
            msgbox('x不正确,y正确。x为'+str(x)+'\n'+'\n'+'还剩下'+str(channe)+'次机会。')
        elif ix == x and iy != y:
            msgbox('y不正确,x正确。x为'+str(y)+'\n'+'\n'+'还剩下'+str(channe)+'次机会。')
        else:
            msgbox('x和y都不正确。x为'+str(x)+','+'y为'+str(y)+'\n'+'\n'+'还剩下'+str(channe)+'次机会。')

    def jjjs(x,y,fxbs,fybs,sxbs,sybs,fh):
        global fjg,sjg
        if fh == 0:
            fjg = x * fxbs + y * fybs
            sjg = x * sxbs + y * sybs
        elif fh == 1:
            fjg = x * fxbs - y * fybs
            sjg = x * sxbs - y * sybs
        elif fh == 2:
            fjg = x * fxbs - y * fybs
            sjg = x * sxbs + y * sybs
        elif fh == 3:
            fjg = x * fxbs + y * fybs
            sjg = x * sxbs - y * sybs
        return fjg,sjg

def CheckWrong(InputSay,ERROR=ValueError,WrongSay='输入错误，你只能输入整数！',):
    Wrong = True
    global temp
    while Wrong:
        try:
            temp = int(enterbox(InputSay))
        except ERROR:
            msgbox(WrongSay)
        else:
            Wrong =  False
    return temp

if __name__ == '__main__':
    CloseDesktop = ccbox(msg="是否关闭桌面？桌面会在答完指定题量后自动恢复。",title="是否关闭桌面？",choices=('关！整死这个小兔崽子！','不关！我桌面还要用！'))
    if CloseDesktop:
        system('TASKKILL /IM explorer.exe /F')
    CheckWrong("应该答多少题后让他自由呢？：")
    channe = temp
    while channe > 0:   
        Programme.make()
        Programme.jjjs(x,y,fxbs,fybs,sxbs,sybs,fh)
        Programme.output(x,y,sxbs,sybs,fxbs,fybs,fh)
        Programme.pd(x,y,ix,iy)
