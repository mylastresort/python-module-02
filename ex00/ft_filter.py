def ft_filter(fn, iterable):
    for arg in iter(iterable):
        if fn(arg):
            yield arg
