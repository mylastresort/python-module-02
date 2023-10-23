class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.header = header
        self.sep = sep
        if skip_top < 0 or skip_bottom < 0:
            raise Exception('Cannot accept negative numeric slicers')
        self.skip_bottom = skip_bottom
        self.skip_top = skip_top

    def __enter__(self):
        self.file = open(self.filename)
        if not self.file:
            return None
        lines = iter(self.file)
        self.header = None if not self.header else [
            cell.strip() for cell in next(lines).split(self.sep)]
        try:
            self.data = [
                [cell.strip() for cell in next(lines).split(self.sep)]]
        except:
            self.data = []
        if not self.header and not self.data:
            return self
        lengths = len(self.header or self.data[0])
        for ln in lines:
            if not ln.strip():
                continue
            row = [cell.strip() for cell in ln.split(self.sep)]
            if len(row) != lengths:
                return None
            self.data.append(row)
        if self.skip_bottom > len(self.data):
            self.skip_bottom = 0
        self.data = self.data[self.skip_top:-self.skip_bottom or None]
        return self

    def __exit__(self, *args):
        self.file.close()

    def getheader(self):
        return self.header

    def getdata(self):
        return self.data


if __name__ == '__main__':
    with CsvReader('good.csv', skip_bottom=20) as file:
        data = file.getdata()
        header = file.getheader()
        print('--------header-------')
        print(header)
        print('---------data--------')
        print(data)
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
