

#coin  function may only have values of [5,10,25,100,200] cents,
#any values outside of these should raise value error
accoin = (200,100,25,10,5)
def coin(n):
    if n in accoin :# check if n is one of the values t
      return n
    else:
      raise ValueError #raise error

#insert_coin function should append number value into inserted_coin list fif it passes
# the coin function outlined above
def insert_coin(*numbers,inserted_coins):
    for number in numbers:# sequentially append numbers into the 'inserted_coins' list
        inserted_coins.append(coin(number))

    return inserted_coins

# testing the buy_product function  which should consult if 'drink' function
#is one of the available products and if it is, find a balance, if the balance is negative,
#it should then raise a custom error.
# products available for purchase are {'candy':315,'drink':275,'chips':225}
class InsufficientFunds(Exception):
    "Insufficient funds for purchase :.("
    pass
def buy_product(price,item):

    products = {'candy':315,'drink':275,'chips':225}
    if item in products.keys():#check if item is valid, ie is a key in products dictionary
          balance = price-products.get(item)# get price of item and subtract with the 'price'
          if balance >= 0:#if balance is positive  return the balance
              return(balance)
          else:# if balance is negative raise error
              raise InsufficientFunds
    else:#if object isn't in dictionary
        raise ValueError
#Return change if 'balance' is larger than zero,return in values of [5,10,25,100,200],
#ordered from highest to lowest value, rounding down
def return_change(balance):
    change =[]
    for n in accoin:#check through all coin values
        if isinstance(balance//n,int):   # check if the balance is an integer of the coin value
            for x in range(0,balance//n):# if the function is an integer (of coin n),
                change.append(n)         # then add coin into change
            balance= balance-n*(balance//n) #subtract change given from balance

    return change
