import calculator

def test_two_plus_two():
    assert calculator.add(2,2) == 4

def test_eight_plus_two():
      assert calculator.add(8,2) == 10

def test_with_three_arguments():
    assert calculator.add(3,4,3) == 10

def test_with_five_arguments():
      assert calculator.add(3,8,2,1,2) == 16
