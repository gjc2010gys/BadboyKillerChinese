import random

stop = 'n'

class Programme(object):
    def sc(x,y,sxbs,sybs,fxbs,fybs,fh):
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
        if x == ix and y == iy:
            print('X和Y都正确！')
        elif x == ix:
            print('X正确！')
        elif x != ix:
            print('X不正确!,X的值为'+str(x))
        elif y == iy:
            print('Y正确！')
        elif y != iy:
            print('Y不正确!,Y的值为'+str(y))

    def sr():
        global ix,iy
        ix = int(input('请输入x：'))
        iy = int(input('请输入y：'))
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

if __name__ == '__main__':
    while stop != 'y':   
        Programme.make()
        Programme.jjjs(x,y,fxbs,fybs,sxbs,sybs,fh)
        Programme.sc(x,y,sxbs,sybs,fxbs,fybs,fh)
        Programme.sr()
        Programme.pd(x,y,ix,iy)
        stop = input("Do you want to stop?(Type 'y' or 'n)")