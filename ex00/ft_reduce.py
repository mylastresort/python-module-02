def ft_reduce(fn, iterable):
    iterable = iter(iterable)
    acc = next(iterable)
    for cur in iterable:
        acc = fn(acc, cur)
    return acc
