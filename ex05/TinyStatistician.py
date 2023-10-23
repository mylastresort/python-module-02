from math import sqrt


class TinyStatistician:
    def mean(self, x):
        return None if not x else float(sum(x) / len(x))

    def median(self, x):
        if not x:
            return None
        x = sorted(x)
        m = len(x)
        return float(x[int(m / 2)] if m % 2 != 0 else x[(int(m / 2) + int((m - 1) / 2)) / 2])

    def quartiles(self, x):
        if not x:
            return None
        x = sorted(x)
        m = len(x)
        k = 4 / m
        return [float(x[int(1 / k)]), float(x[int(3 / k)])]

    def var(self, x):
        if not x:
            return None
        m = len(x)
        mean = self.mean(x)
        return float(sum([(v - mean) ** 2 for v in x])) / m

    def std(self, x):
        return sqrt(self.var(x))
