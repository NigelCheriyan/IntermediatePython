#
import vend
import pytest

#coin  function may only have values of [5,10,25,100,200] cents,
#any values outside of these should raise value error
def test_coin_five(): #test  if coin functionrecognizes five coins
      assert vend.coin(5) == 5

def test_coin_not_thirty():#test if coin function raises error for 30 coins
     with pytest.raises(ValueError):
        vend.coin(30)
#insert_coin function should append number value into inserted_coin list fif it passes
# the coin function outlined above
def test_insert_five():#test insert a value of 5 to inserted_coin list
    inserted_coins =[5,10]
    assert  vend.insert_coin(5,inserted_coins=inserted_coins) == [5,10,5]


def test_insert_ten_and_five():#test insert multiple values to inserted_coin list
    inserted_coins =[1,2,3]
    assert vend.insert_coin(10,5,inserted_coins=inserted_coins) ==[1,2,3,10,5]

def test_insert_thirty():#test insert a value  which should be rejected by function
    inserted_coins =[]
    with pytest.raises(ValueError):
         vend.insert_coin(30,inserted_coins=inserted_coins)
# testing the buy_product function  which should consult if
#is one of the available products and if it is, find a balance, if the balance is negative,
#it should then raise a custom error. if the item is not in dictionary, it should return ValueError
# products available for purchase are {'candy':315,'drink':275,'chips':225}
def test_buy_drink():# testing a purchase that should be approved ('drink') and
                     # the balance is zero
    assert vend.buy_product(275,'drink') == 0

def test_buy_banana():#test buying an illegal object
    with pytest.raises(ValueError):
         vend.buy_product(220,'banana')

def test_buy_insuficient(): #testing a purchase where the item is present
                            # but the balance is less than zero
     with pytest.raises(vend.InsufficientFunds):
              vend.buy_product(200,'candy')
def test_buy_toomuch():#test is
    assert vend.buy_product(300,'drink') == 25

#Return change if 'balance' is larger than zero,return in values of [5,10,25,100,200],
#ordered from highest to lowest value, rounding down

def test_return_change():#test  one coin worth of change
    assert vend.return_change(200)==[200]

def test_return_mul_coin():#test multiple coins worth of return_change
    assert vend.return_change(150)==[100,25,25]

def test_return_non5mult():#test change machine for a non multiple of five
    assert vend.return_change(126)==[100,25]

def test_return_large():#test arbitarily large number to see rigor
    assert vend.return_change(937)==[200,200,200,200,100,25,10]
