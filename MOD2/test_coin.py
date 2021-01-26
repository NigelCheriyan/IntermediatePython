#coin =[5,10,25,100,200] #cents any values outside of these should raise value error
import vend
import pytest
def test_coin_five():
      assert vend.coin(5) == 5

def test_coin_ten():
    assert vend.coin(10) == 10

def test_coin_not_thirty():
     with pytest.raises(ValueError):
        vend.coin(30)
