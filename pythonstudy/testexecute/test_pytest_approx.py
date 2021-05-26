from  pytest import approx
def test_01():
    bool = (0.1 + 0.2, 0.4 + 0.2) == approx((0.3,0.6))

    assert bool == True