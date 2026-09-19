a = float (input("a: "))
b = float (input("b: "))
c = float (input("c: "))

if a == 0:
    print("Bukan persamaan kuadrat")    
else:
    D = b**2 - 4*a*c
    print(f"Diskriminan: {D:.2f}")
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)  
        print(f"Akar-akar persamaan kuadrat: x1 = {x1:.2f}, x2 = {x2:.2f}")
        print("Persamaan kuadrat memiliki dua akar real yang berbeda.")
    else:
        if D == 0:
            x = -b / (2*a)
            print(f"Akar-akar persamaan kuadrat: x = {x:.2f}")
            print("Persamaan kuadrat memiliki satu akar real (akar kembar).")
        else:
            print("Persamaan kuadrat tidak memiliki akar real.")