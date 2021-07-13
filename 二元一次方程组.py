
import random

stop = 'n'
Wrong = True

class Programme(object):
    def output(x,y,sxbs,sybs,fxbs,fybs,fh):
        if fh == 0:
            print(str(fxbs)+'x'+'+'+str(fybs)+'y'+'='+str(fjg))
            print(str(sxbs)+'x'+'+'+str(sybs)+'y'+'='+str(sjg)+'\n')
        elif fh == 1:
            print(str(fxbs)+'x'+'-'+str(fybs)+'y'+'='+str(fjg))
            print(str(sxbs)+'x'+'-'+str(sybs)+'y'+'='+str(sjg)+'\n')
        elif fh == 2:
            print(str(fxbs)+'x'+'-'+str(fybs)+'y'+'='+str(fjg))
            print(str(sxbs)+'x'+'+'+str(sybs)+'y'+'='+str(sjg)+'\n')
        elif fh == 3:
            print(str(fxbs)+'x'+'+'+str(fybs)+'y'+'='+str(fjg))
            print(str(sxbs)+'x'+'-'+str(sybs)+'y'+'='+str(sjg)+'\n')

    def make():
        global x,y,xbs,ybs,fh,fxbs,fybs,sxbs,sybs
        x = random.randint(1,10)
        y = random.randint(1,10)
        fxbs = random.randint(1,5)
        fybs = random.randint(1,5)
        sxbs = random.randint(1,5)
        sybs = random.randint(1,5)
        fh = random.randint(0,3)
        return x,y,fxbs,fybs,fh,sybs,sxbs

    def pd(x,y,ix,iy):
        if ix == x:
            print('x正确.')
        else:
            print('x不正确。x为'+str(x))
        if iy == y:
            print('y正确.')
        else:
            print('y不正确。x为'+str(y))
    def sr():
        global ix,iy
        CheckWrong('请输入x：')
        temp = ix
        CheckWrong('请输入y：')
        temp = iy
        return ix,iy

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

if __name__ == '__main__':
    OutputNoInput=input('输出模式或者答题模式？(输出为1，答题为2)')
    if OutputNoInput == '2':
        while True:   
            Programme.make()
            Programme.jjjs(x,y,fxbs,fybs,sxbs,sybs,fh)
            Programme.output(x,y,sxbs,sybs,fxbs,fybs,fh)
            Programme.sr()
            Programme.pd(x,y,ix,iy)
    else:
        CheckWrong('你想要多少个问题?')
        questiontime = temp
        for i in range(0,questiontime):   
            Programme.make()
            Programme.jjjs(x,y,fxbs,fybs,sxbs,sybs,fh)
            Programme.output(x,y,sxbs,sybs,fxbs,fybs,fh)
            print('x='+str(x)+'\n'+'y='+str(y))
