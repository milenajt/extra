a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
x1 = (-b-(d**0.5))/(2*a)
x2 = (-b+(d**0.5))/(2*a)
if d>0:
    print(min(x1,x2))
    print(max(x1,x2))
elif d==0:
    print(-(b/(2*a)))