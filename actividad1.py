a = input("Elige: ")

if a == 1: print("Hola")
elif a == 2: print("Adios")
elif a==3: print("Hola dev")
else: print("Tas we, chao")

for i in range(int(a)):
    for j in range(int(a)):
        if j <=i: print(" * ", end="")
    print("\n")

print("Fin")