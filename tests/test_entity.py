import sys
sys.path.append('/Users/devin/Sandbox/AquaLife/entities/')

from entity import Entity


def test_EntityConstructor():
    a = Entity((-10,10))
    assert a.x == -10 and a.y == 10
    b = Entity()
    assert b.x == 0 and b.y == 0
