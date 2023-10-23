def what_are_the_vars(*args, **kwargs):
    ins = ObjectC()
    for i, arg in enumerate(args):
        setattr(ins, 'var_%s' % i, arg)
    for key, val in kwargs.items():
        if hasattr(ins, key):
            return None
        setattr(ins, key, val)
    return ins


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("%s: %s" % (attr, value))
    print("end")


def main():
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)


if __name__ == "__main__":
    main()
