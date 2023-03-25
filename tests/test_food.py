import sys
sys.path.append('/Users/devin/Sandbox/AquaLife/entities/')

from food import Food


def test_FoodConstructor():
    a = Food((-10,10))
    assert a.x == -10 and a.y == 10
    b = Food()
    assert b.x == 0 and b.y == 0
