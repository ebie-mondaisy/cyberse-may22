from programs.budget import Budget

def test_budget_1():
    testobj = Budget(500)
    assert testobj.balance == 500

def test_budget_2():
    testobj = Budget(500)
    assert testobj.withdraw(50) == 50
    assert testobj.balance == 450 

def test_budget_3():
    testobj = Budget(500)
    assert testobj.deposit(50) == 50
    assert testobj.balance == 550

def test_budget_4():
    testobj = Budget(500)
    assert f"{testobj}" == "The current balance of this budget is: 500"   