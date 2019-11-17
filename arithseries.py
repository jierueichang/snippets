import sys
a1 = float(sys.argv[1])
a2 = float(sys.argv[2])
s = float(sys.argv[3])
d = a2-a1
print 'a_n=%d(n)+%d' %(d,-d+a1)
an = d*s+(-d+a1)
print '%d((%d+%d)/2)' %(s,a1,an)
print s*((a1+an)/2)
