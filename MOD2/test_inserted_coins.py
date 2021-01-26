import vend
import pytest
def test_insert_five():
    inserted_coins =[5,10]
    assert  vend.insert_coin(5,inserted_coins=inserted_coins) == [5,10,5]

def test_insert_ten():
    inserted_coins =[]
    assert vend.insert_coin(10,inserted_coins=inserted_coins) == [10]

def test_insert_ten_and_five():
    inserted_coins =[1,2,3]
    assert vend.insert_coin(10,5,inserted_coins=inserted_coins) ==[1,2,3,10,5]

def test_insert_thirty():
    inserted_coins =[]
    with pytest.raises(ValueError):
         vend.insert_coin(30,inserted_coins=inserted_coins)
