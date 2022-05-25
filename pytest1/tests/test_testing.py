#remember to use python3 -m pytest <file name> to test code in a file
from programs.debug import mult
#testing to see if 5 times 2 is equal to 10
def test_mult():
    var = mult(5)
    assert var == 10
    assert mult(12) == 24

#testing to see if 6 times 2 is equal to 11
def test_mult2():
    var = mult(6)
    assert var == 12