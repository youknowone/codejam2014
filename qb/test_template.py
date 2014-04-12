
from template import *

def test_something():
    clicker = CookieClicker(500.0, 4.0, 2000.0)
    assert clicker.C == 500.0

    assert True == clicker.estimate()
    clicker.buy()
    assert clicker.cookies == 0
    assert clicker.cookies_per_second() == 6
    assert clicker.seconds == 250

    assert True == clicker.estimate()
    seconds = clicker.buy()
    assert str(seconds).startswith('83.333333')
    assert clicker.cookies_per_second() == 10

    assert True == clicker.estimate()
    seconds = clicker.buy()
    assert seconds == 50
    assert clicker.cookies_per_second() == 14

    assert False == clicker.estimate()
    seconds = clicker.wait()
    assert str(seconds).startswith('142.8571429')
