

DOPER = {3: "ˆ", 2: "*/", 1: "+-"}


def play(rpn, oper):
    b = rpn.pop()
    a = 0
    if len(rpn) != 0:
        a = rpn.pop()
    if oper == "+":
        rpn.append(a + b)
    elif oper == "-":
        rpn.append(a - b)
    elif oper == "*":
        rpn.append(a * b)
    elif oper == "/":
        rpn.append(a / b)
    elif oper == "ˆ":
        rpn.append(a ** b)
    return rpn


def priority(s):
    for k, v in DOPER.items():
        if s in v:
            return k


def compose(lvalue):
    p = 0
    if "." in lvalue:
        p = -lvalue.index(".")
    v = 0
    while len(lvalue) > 0:
        c = lvalue.pop()
        if c != ".":
            v += (ord(c) - 48) * 10 ** p
            p += 1
    return v


def calculate(sentence):
    lvalue = []
    lrpn = []
    loper = []

    for i in range(len(sentence)):

        s = sentence[i]
        if s not in "0123456789.+-*/ˆ() ":
            raise Exception("posicao ", i)

        if s in "0123456789.":
            lvalue.append(s)
            continue

        if len(lvalue) != 0:
            lrpn.append(compose(lvalue))

        if s == "(":
            loper.append(s)
            continue
        elif s == ")":
            if len(loper) == 0:
                raise Exception("posicao ", i)

            while loper[-1] != "(":
                lrpn = play(lrpn, loper.pop())
                if len(loper) == 0:
                    raise Exception("posicao ", i)

            loper.pop()
            continue

        elif s == " ":
            pass
        else:

            while len(loper) != 0:
                previous = loper[-1]
                if previous not in "()" and priority(previous) >= priority(s):
                    lrpn = play(lrpn, loper.pop())
                else:
                    break

            loper.append(s)

    if len(lvalue) != 0:
        lrpn.append(compose(lvalue))

    while len(loper) > 0:
        lrpn = play(lrpn, loper.pop())

    return lrpn.pop()


sentence = "(-10+(10ˆ2-4*2*2)ˆ(2))/(2+3.5)"
print(calculate(sentence))

