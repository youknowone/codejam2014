#!/usr/bin/env python

import util
# util.DEBUG = True
from util import *


class MineSweeper(object):
    def __init__(self, R, C, M):
        self.R = R
        self.C = C
        self.M = M
        self.map = None

    def generate(self):
        self.map = Plain((self.R, self.C), '.')
        mines = self.M
        safearea = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 2), (1, 2)]
        skipped = False
        if mines > 0:
            for r in xrange(self.R - 1, -1, -1):
                for c in xrange(self.C -1, -1, -1):
                    if (r, c) not in safearea:
                        if c == 1 and mines == 1:
                            skipped = True
                            continue
                        if skipped:
                            skipped = False
                            continue
                        self.map[r, c] = '*'
                        mines -= 1
                        if mines == 0:
                            break
                if mines == 0:
                    break

        assert mines >= 0
        if mines > 0:
            if self.R > 1 and self.C > 2 and mines > 2:
                self.map[0, 2] = '*'
                self.map[1, 2] = '*'
                mines -= 2
            elif self.R == 1 and self.C > 2 and mines > 1:
                self.map[0, 2] = '*'
                mines -= 1
            if mines == 3 and self.R > 1 and self.C > 1:
                self.map[0, 1] = '*'
                self.map[1, 0] = '*'
                self.map[1, 1] = '*'
                mines -= 3
            if self.R == 1:
                self.map[0, 1] = '*'
                mines -= 1
            if self.C == 1:
                self.map[1, 0] = '*'
                mines -= 1
            if mines != 0:
                print 'mines:', mines
                self.draw()
            assert mines == 0

        self.map[0, 0] = 'c'

    def decide(self):
        safe_spots = self.R * self.C - self.M
        if safe_spots == 1:
            return True
        if 1 in [self.R, self.C]:
            return True
        if 2 in [self.R, self.C] and safe_spots % 2 == 1:
            return False
        if safe_spots not in [5, 7] and safe_spots > 4:
            return True
        return False

    def draw(self):
        if self.map is None:
            self.generate()
        for r in xrange(0, self.map.size[0]):
            row = ''.join([self.map[r, c] for c in xrange(0, self.map.size[1])])
            print row

def solution(count):
    R, C, M = intlist_input()
    sweeper = MineSweeper(R, C, M)
    possible = sweeper.decide()
    print 'Case #{}:'.format(count + 1)
    if possible:
        sweeper.draw()
    else:
        print 'Impossible'

if __name__ == '__main__':
    count = int_input()
    loop(count, solution)