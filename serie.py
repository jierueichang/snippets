import os
def clear():
    _=os.system('cls')

def startup():
    clear()
    print '________________________'
    print '   SERIE Version 1.02   '
    print 'Press Enter to continue'
    print '________________________'
    raw_input()

#Summation
def summation():
    clear()
    print('SUMMATION')
    print('use n as variable.')
    a = raw_input('equation: ')
    s = int(raw_input('start: '))
    end = int(raw_input('end: '))
    t = 0
    for n in range(s,end):
        t+=eval(a)
        print eval(a),
        if not n==end:
            print ' + ',
        else:
            print ' = ',
    print t
    raw_input()

#Arithmetic Series
def arithseries():
    clear()
    print('ARITHMETIC SERIES')
    a1 = float(raw_input('a1: '))
    d = float(raw_input('d: '))
    n = int(raw_input('n: '))
    an = a1+d*(n-1)
    print str(n*(a1+an)/2)
    raw_input()
#Geometric Series
def geoseries():
    clear()
    print('GEOMETRIC SERIES')
    a1 = float(raw_input('a1: '))
    r = float(raw_input('r: '))
    n = int(raw_input('n: '))
    print a1*(1-r**n)/(1-r)
    raw_input()

#Convergent Geometric Series
def congeoseries():
    clear()
    print('CONVERGENT GEOMETRIC SERIES')
    a1 = float(raw_input('a1: '))
    r = float(raw_input('r: '))
    print a1/(1.0-r)
    raw_input()

def main():
    startup()
    while True:
        clear()
        print '[Select option]'
        print '1: Summation'
        print '2: Arithmetic Series'
        print '3: Geometric Series'
        print '4: Con. Geo Series'
        option = raw_input('Option: ')
        if option == '1':
            summation()
        if option == '2':
            arithseries()
        if option == '3':
            geoseries()
        if option == '4':
            congeoseries()

if __name__ == '__main__':
    main()