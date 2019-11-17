import sys, math
if len(sys.argv) < 2:
    print 'Usage: a1, r, n'
if len(sys.argv) > 5:
    print 'Too many arguments'
if len(sys.argv) == 4:
    a1 = float(sys.argv[1])
    r  = eval(sys.argv[2])
    n  = float(sys.argv[3])
    print '       %d(1-%s^%d) ' %(a1,str(r),n)
    print 'S_%d = -----------' %(n)
    print '          1-%s    ' %(str(r))
    print '    %d(%s)' %(a1,str(1-r**n))
    print '=  --------------'
    print '      %s  ' %(str(1-r))
    print ' = '+str((a1*(1-(r**n)))/(1-r))
'''if len(sys.argv) == 5:
    a1 = float(sys.argv[1])
    r  = float(sys.argv[2])
    end = float(sys.argv[3])
    n = math.abs(end)/math.abs(1)'''
