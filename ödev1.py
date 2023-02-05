def mul(f1, f2):
    result = {}
    result['s'] = f1['s'] * f2['s']
    result['m'] = f1['m'] * f2['m']
    return result

def sum(f1 , f2):
    result = {}
    result['s'] = (f1['s']*f2['m']) + (f1['m']*f2['s'])
    result['m'] = f1['m']*f2['m']
    return result

def taf(f1 , f2):
    result = {}
    result['s'] = (f1['s']*f2['m']) - (f1['m']*f2['s'])
    result['m'] = f1['m']*f2['m']
    return result

def tag(f1 , f2):
    result = {}
    result['s'] = f1['s'] * f2['m']
    result['m'] = f1['m'] * f2['s']
    return result

def show(f):
    print(f['s'], '/', f['m'])

while True:
    f1_s = int(input("enter f1-s : "))
    f1_m = int(input("enter f1-m : "))
    f2_s = int(input("enter f2-s : "))
    f2_m = int(input("enter f2-m : "))

    a = {'s':f1_s, 'm':f1_m}
    b = {'s':f2_s, 'm':f2_m}
    show(a)
    show(b)
    right = input("right?? ok / no :")
    if right == "ok":
        op = input("enter * or + or - or / :")
        if op == "*":
            mul_result = mul(a , b)
            show(mul_result)

        if op == "+":
            sum_result = sum(a , b)
            show(sum_result)

        if op == "-":
            taf_result = taf(a , b)
            show(taf_result)

        if op == "/":
            tag_result = tag(a, b)
            show(tag_result)
        
        exit = input("continue(c) or exit(e) : ")
        if exit == "c":
            continue
        if exit == "e":
            break
        

    if op == "no":
        continue
    
# mul: 2/3 * 4/5 = (2*4) / (3*5)
# sum: 2/3 + 4/5 = ((2*5)+(4*3)) / (3*5)
# taf: 2/3 - 4/5 = ((2*5)-(4*3)) / (3*5)
# tag: 2/3 / 4/5 = (2*5) / (3*4)