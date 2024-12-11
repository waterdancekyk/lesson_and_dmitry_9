from math import sin, cos


print('Введите Xstart, Xstop и Xstep')
Xstart = float(input('Xstart = '))
Xstop = float(input('Xstop = '))
Xstep = float(input('Xstep = '))


print("Xstart={0:7.2f} Xstop={1:7.2f}".format(Xstart, Xstop))
print(" Xstep = {0:7.2f}".format(Xstep))


xt = Xstart

print("+--------+--------+")
print("|    X   |    Y   |")
print("+--------+--------+")


while xt <= Xstop:
    if cos(xt) >= 0:
        y = sin(xt)**2 - sin(xt) + 1
    else:
        y = cos(xt)**2 - cos(xt) + 1
    
    print("|{0:7.2f} |{1:7.2f} |".format(xt, y))
    xt += Xstep

print("+--------+--------+")
