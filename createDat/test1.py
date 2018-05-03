class Dat:
    def __init__(self):
        self.dat = []

    def add(self, v):
        self.dat.append(v)

    def printValues(self):
        print("{} - {} - {}".format(self.dat[0], self.dat[1], self.dat[2]))

class Recursive:
    def __init__(self):
        self.dats = []
        self.dataValues = []
        self.dataNum = 1
        self.num = 0

    def addDat(self, dat):
        self.dataValues.append(dat)
        self.dataNum *= len(dat)
        self.num += 1

    def setFirst(self):
        self.index = 0
        self.currentLength = self.dataNum
        for i in range(self.dataNum):
            self.dats.append(Dat())

    def setParam(self):
        val = self.dataValues[self.index]
        length = int(self.currentLength / len(val))
        self.currentLength = length
        for i in range(self.dataNum):
            for j in range(len(val)):
                for k in range(length):
                    index = i * len(val) * length + j * length + k
                    print("{} - {}: {}".format(self.index, index, val[j]))
                    self.dats[index].add(val[j])
            if index + 1 == self.dataNum:
                print("fin")
                break
        self.index += 1
        if self.index == self.num:
            return
        else:
            self.setParam()

    def execute(self):
        self.setFirst()
        self.setParam()
        for i in range(self.dataNum):
            self.dats[i].printValues()


# def recursiveFunction(dats, values, length, index, startPoint):
#     if index < 0:
#         return
#
#     v = values[index]
#     vLen = int(length / len(v))
#     for x in range(len(v)):
#         for y in range(vLen):
#             buf = startPoint + y + x * vLen
#             print("{} - {}: {}".format(index, x, buf))
#             dats[buf] = v[x]
#         recursiveFunction(dats, values, vLen, index - 1, startPoint)
#         startPoint = x * vLen
#
# def recursiveMethod(a, b, c):
#     valNum = 3
#     values = []
#     values.append(a)
#     values.append(b)
#     values.append(c)
#     length = len(a) * len(b) * len(c)
#     dats = []
#     for i in range(length):
#         dats.append(Dat())
#
#     print("length: ", length)
#
#     recursiveFunction(dats, values, length, valNum - 1, 0)
#
#     for j in range(length):
#         dats[j].printValues()


def main():
    r = Recursive()
    a = ["a1", "a2", "a3"]
    b = ["b1", "b2", "b3"]
    c = ["c1", "c2", "c3"]
    r.addDat(a)
    r.addDat(b)
    r.addDat(c)
    r.execute()

if __name__ == "__main__":
    main()
