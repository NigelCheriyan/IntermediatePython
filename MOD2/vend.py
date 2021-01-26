
def coin(n):
    if n in (5,10,25,100,200) :
      return n
    else:
      raise ValueError

def insert_coin(*numbers,inserted_coins):
    for number in numbers:
        inserted_coins.append(coin(number))

    return inserted_coins
