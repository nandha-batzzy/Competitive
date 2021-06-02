num = 28
lst =[]
i = 2
c = 1
lst.append(1)
while num%i == 0:
    c = c*i
    lst= [c]+lst
    num = num//2
    lst.append(num)
i = i+1

if sum(lst) == num:
    print(False)
else:
    print(True)