
def int_input():
    text = raw_input()
    return int(text)

def intlist_input(size=None):
    text = raw_input()
    str_values = text.split(' ')
    values = map(int, str_values)
    if size is not None:
        assert len(values) == size
    return values

def loop(count, func):
    for x in xrange(0, count):
        func(x)

def print_case(count, fmt, *args):
    prefix = 'Case #{}:'.format(count + 1)
    if len(args):
        print prefix, fmt % args
    else:
        print prefix, fmt
