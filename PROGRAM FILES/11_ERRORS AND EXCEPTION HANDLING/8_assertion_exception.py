try:
    a=10
    b=20
    assert a==b, "Value mismatch"
except AssertionError as e:
    print(e)
