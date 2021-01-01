import  itertools

for i in itertools.combinations_with_replacement("srea", 3):
    print("".join(i))