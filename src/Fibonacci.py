# app.py
def fibo(a):
    if a <= 1:
        return a
    return fibo(a - 1) + fibo(a - 2)

def test_fibo():
    assert fibo(5) == 5
    assert fibo(0) == 0
    assert fibo(1) == 1