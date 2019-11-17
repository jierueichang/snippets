def find_coefficient_factors(num):
    num = float(num)
    factors = []
    if num<0:
        num = -num
    if num>6:
        for i in range(1,int(num/2)+1):
            if num%i == 0:
                factors.append(i)
                factors.append(int(num/i))
    else:
        for i in range(1,int(num)+1):
            if num%i == 0:
                factors.append(int(i))
    factors.sort()
    print factors
    return factors

def calc_all_combinations(f1,f2):
    combinations = []
    for i in f1:
        for j in f2:
            if j%i==0:
                combinations.append(str(j/i))
            else:
                combinations.append(str(j)+'/'+str(i))
    return combinations

def prompt():
    cl = raw_input('coefficients: ').split(' ')
    for i in cl:
        i = float(i)
    return cl

def try_candidates(combos,cl):
    zeros = []
    recreated_eq = ''
    for j in range(len(cl)):
        recreated_eq+='('+str(cl[j])+')*x**('+str(len(cl)-j-1)+')+'
    recreated_eq=recreated_eq[:-1]
    print(recreated_eq)
    for i in combos:
        x = float(eval(i))
        print x
        print eval(recreated_eq)
        if eval(recreated_eq)==0: zeros.append(i)
        x = -x
        if eval(recreated_eq)==0: zeros.append('-'+i)
    return zeros

def handle():
    coefficients = prompt()
    lc = coefficients[0]
    ct = coefficients[-1]
    f1 = find_coefficient_factors(lc)
    f2 = find_coefficient_factors(ct)
    combos = calc_all_combinations(f1,f2)
    print combos
    print try_candidates(combos,coefficients)

handle()
