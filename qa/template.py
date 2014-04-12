#!/usr/bin/env python

from util import *

def solution(count):
    answer1 = int_input()
    table1 = [intlist_input() for x in xrange(0, 4)]
    answer2 = int_input()
    table2 = [intlist_input() for x in xrange(0, 4)]
    candidates1 = set(table1[answer1 - 1])
    candidates2 = set(table2[answer2 - 1])
    candidates = candidates1.intersection(candidates2)

    if len(candidates) == 1:
        print_case(count, candidates.pop())
    elif len(candidates) == 0:
        print_case(count, 'Volunteer cheated!')
    elif len(candidates) > 1:
        print_case(count, 'Bad magician!')

if __name__ == '__main__':
    count = int_input()
    loop(count, solution)