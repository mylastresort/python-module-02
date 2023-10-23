def ft_map(fn, iterable):
    for arg in iter(iterable):
        yield fn(arg)
