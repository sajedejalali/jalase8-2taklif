def sum(t1 , t2):
    result = {}
    result['h'] = t1['h'] + t2['h']
    result['m'] = t1['m'] + t2['m']
    result['s'] = t1['s'] + t2['s']
    
    if result['s'] >= 60 :
        result['s'] -= 60
        result['m'] +=1
    if result['m'] >= 60:
        result['m'] -= 60 
        result['h'] += 1
    if result['h'] >= 24:
        result['h'] -= 24
    return result

def taf(t1 , t2):
    result = {}
    result['h'] = t2['h'] - t1['h']
    result['m'] = t2['m'] - t1['m']
    result['s'] = t2['s'] - t1['s']

    if result['s'] < 0:
        result['m'] -= 1
        result['s'] += 60
    if result['m'] < 0 :
        result['h'] -= 1
        result['m'] += 60
    if result['h'] >= 24:
        result['h'] -= 24
    return result

def show(time):
    print(time['h'], ':', time['m'], ':', time['s'])

while True:
    time1_h = int(input("enter h for time1 : "))
    time1_m = int(input("enter m for time1 : "))
    time1_s = int(input("enter s for time1 : "))
    time2_h = int(input("enter h for time2 : "))
    time2_m = int(input("enter m for time2 : "))
    time2_s = int(input("enter s for time2 : "))

    time1 = {'h':time1_h, 'm':time1_m, 's':time1_s}
    time2 = {'h':time2_h, 'm':time2_m, 's':time2_s}
    show(time1)
    show(time2)
    right = input("right?? ok/no : ")
    if right == "ok":
        op = input("+ or - ? :")
        if op == "+":
            sum_result = sum(time1, time2)
            show(sum_result)
        if op == "-":
            taf_result = taf(time1, time2)
            show(taf_result)
        
        exit = input("continue(c) or exit(e)?? :")
        if exit == "c":
            continue
        if exit == "e":
            break
    if right == "no":
        continue