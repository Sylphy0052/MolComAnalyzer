class Dat:
    def __init__(self):
        self.param = []
        self.index = 0

    def setParam(self, v):
        self.param[index] = v
        self.index += 1

    def printValues(self):
        print("{} - {} - {}".format(self.param[0], self.param[1], self.param[2]))

def recursiveFunction(dats, values, length, index, startPoint):
    if index < 0:
        return

    v = values[index]
    vLen = int(length / len(v))
    for x in range(len(v)):
        for y in range(vLen):
            buf = startPoint + y + x * vLen
            print("{} - {}: {}".format(index, x, buf))
            dats[buf] = v[x]
        recursiveFunction(dats, values, vLen, index - 1, startPoint)
        startPoint = x * vLen

def recursiveMethod(a, b, c):
    valNum = 3
    values = []
    values.append(a)
    values.append(b)
    values.append(c)
    length = len(a) * len(b) * len(c)
    dats = []
    for i in range(length):
        dats.append(Dat())

    print("length: ", length)

    recursiveFunction(dats, values, length, valNum - 1, 0)

    for j in range(length):
        dats[j].printValues()


def main():
    a = ["a1", "a2", "a3"]
    b = [1, 10, 20, 30, 40, 50]
    c = [0, 1, 2, 3]
    recursiveMethod(a, b, c)

if __name__ == "__main__":
    main()
