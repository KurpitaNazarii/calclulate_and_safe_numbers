def check(n1, do, n2):
    divide = "What"
    fl = '.'
    if n1.isnumeric() and n2.isnumeric():
            if calculate(n1, do, n2) is divide:
                return divide
            if not calculate(n1, do, n2):
                return False
            else:
                calculate(n1, do, n2)
    elif fl in n1 and fl in n2:
        if calculate(n1, do, n2) is divide:
            return divide
        else:
            calculate(n1, do, n2)
        if not calculate(n1, do, n2):
            return False
        if calculate(n1, do, n2):
            return True
    elif fl in n1:
        if calculate(n1, do, n2) is divide:
            return divide
        else:
            calculate(n1, do, n2)
        if not calculate(n1, do, n2):
            return False
        elif calculate(n1, do, n2):
            return True
    elif fl in n2:
        if calculate(n1, do, n2) is divide:
            return divide
        else:
            calculate(n1, do, n2)
        if not calculate(n1, do, n2):
            return False
        elif calculate(n1, do, n2):
            return True
    else:
        return True


def calculate(r1, od, r2):
    divide = "What"
    try:
        r1 = float(r1)
        r2 = float(r2)
    except ValueError:
        return True
    else:
        prov(r1, r2, od)
        calc = ('+', '-', '/', '*')
        if od in calc:
            if od == calc[0]:
                result = r1 + r2
                print(result)
                store(result)
            elif od == calc[1]:
                result = r1 - r2
                print(result)
                store(result)
            elif od == calc[2]:
                if r2 != 0:
                    result = (r1 / r2)
                    print(result)
                    store(result)
                else:
                    return divide
            else:
                result = r1 * r2
                print(result)
                store(result)
        else:
            return False


def ret():
    while True:
        mem = memory
        x, oper, y = input("Enter an equation\n").split()
        if x == 'M':
            x = mem
        if y == 'M':
            y = mem
        divide = "What"
        if check(x, oper, y) is divide:
            print("Yeah... division by zero. Smart move...")
            continue
        if not check(x, oper, y):
            print("Yes '" + oper + "' an interesting math operation. You've slept through all classes, haven't you?")
            continue
        if check(x, oper, y):
            print("Do you even know what numbers are? Stay focused!")
            continue

def store(res):
    global memory
    while True:
        answer = input("Do you want to store the result? (y / n):\n")
        if answer == 'y':
            if is_one_digit(res):
                if repeat(memory):
                    memory = str(res)
            else:
                memory = str(res)
            answer = input("Do you want to continue calculations? (y / n):\n")
            if answer == 'y':
                ret()
            elif answer == 'n':
                exit()
        elif answer == 'n':
            answer = input("Do you want to continue calculations? (y / n):\n")
            if answer == 'y':
                ret()
            elif answer == 'n':
                exit()


def prov(v1, v2, v3):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


def is_one_digit(v):
    if float(v).is_integer() and -10 < float(v) < 10:
        output = True
    else:
        output = False
    return output


def repeat(result):
    msg_ = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            "Are you sure? It is only one digit! (y / n)\n",
            "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
            "Last chance! Do you really want to embarrass yourself? (y / n)\n")
    msg_indx = 10
    while True:
        answear = input(msg_[msg_indx])
        if answear == 'y':
            if msg_indx < 12:
                msg_indx += 1
                continue
            else:
                return True
        if answear == 'n':
            return False


memory = int(0)
ret()
