#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    n = dir(hidden_4)
    for s in n:
        if not s.startswith('__'):
            print('{:s}'.format(s))
