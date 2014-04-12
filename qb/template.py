#!/usr/bin/env python

import util
# util.DEBUG = True
from util import *


class CookieClicker(object):
    def __init__(self, C, F, X):
        self.C = C
        self.F = F
        self.X = X
        self.cookies = 0.0
        self.farms = 0.0
        self.seconds = 0.0
        self.debug_env()

    def debug_env(self):
        debug('C {} F {} X {}'.format(self.C, self.F, self.X))

    def debug_status(self):
        debug('cookies {} farms {} seconds {}'.format(self.cookies, self.farms, self.seconds))

    def cookies_per_second(self, farms=None):
        if farms is None:
            farms = self.farms
        return 2 + farms * self.F

    def estimate_buying(self):
        required = self.C - self.cookies
        production = self.cookies_per_second()
        seconds = required / production
        return seconds

    def estimate(self):
        target = self.X - self.cookies
        production1 = self.cookies_per_second()
        production2 = self.cookies_per_second(self.farms + 1)
        seconds1 = target / production1
        seconds2 = self.estimate_buying() + target / production2
        needs_buy = seconds1 > seconds2
        debug('estimation: not buy {} / buy {}'.format(seconds1, seconds2))
        return needs_buy

    def buy(self):
        seconds = self.estimate_buying()
        self.farms += 1
        self.seconds += seconds
        debug('buy cost:', seconds)
        return seconds

    def wait(self):
        required = self.X - self.cookies
        production = self.cookies_per_second()
        seconds = required / production
        self.cookies += required
        self.seconds += seconds
        debug('wait cost:', seconds)
        return seconds

    def decide(self):
        needs_buy = self.estimate()
        debug('needs buy?', needs_buy)
        if needs_buy:
            self.buy()
        else:
            self.wait()
            raise StopIteration

    def loop(self):
        try:
            while True:
                self.debug_status()
                self.decide()
        except StopIteration:
            pass
        self.debug_status()
        return self.seconds

def solution(count):
    C, F, X = floatlist_input()
    clicker = CookieClicker(C, F, X)
    seconds = clicker.loop()
    print_case(count, round(seconds, 7))
    debug()

if __name__ == '__main__':
    count = int_input()
    loop(count, solution)
