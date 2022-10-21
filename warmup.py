COEFFICIENT = (1/2) ** 6

def get_initial_height(h):
    return h / COEFFICIENT
print(get_initial_height(1))

def get_height(x,b):
    if b == 0:
        return 1
    else:
        return get_height(x/2,b-1)
print(get_height(64,1))

