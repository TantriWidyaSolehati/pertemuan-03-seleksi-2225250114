a = float (input("sisi a: "))
b = float (input("sisi b: "))
c = float (input("sisi c: "))   

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Segitiga sama sisi")
    elif a == b or a == c or b == c:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")
else:
    print("Tiga sisi tersebut tidak dapat membentuk segitiga.")