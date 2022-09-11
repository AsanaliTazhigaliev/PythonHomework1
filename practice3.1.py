health=int(input('How much health does you character have ?'))

def is_alive(health):
    if health<=0:
        return False
    else:
        return True
print(is_alive(health))

