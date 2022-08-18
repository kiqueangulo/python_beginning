def hello():
    print('Hello my friend!')

hello()

def pack(a, b, c):
    return [a, b, c]

print(pack(3, "hola", False))

def eatLunch(food):
    if not bool(len(food)):
        print("My lunchbox is empty")

    elif len(food) == 1:
        print(f"I will only eat {food[0]}")
        
    else:
        print(f"First, I eat {food[0]}.")

        for i in range(1, len(food)):
            print(f"Next, I eat {food[i]}")

eatLunch([])
eatLunch(['arepa'])
eatLunch(['pasta', 'steak', 'sweet plantains'])