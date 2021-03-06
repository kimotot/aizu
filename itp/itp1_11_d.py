class dice:

    def __init__(self, numlist):
        self._men = {"T": numlist[0],
                     "B": numlist[5],
                     "N": numlist[4],
                     "S": numlist[1],
                     "W": numlist[3],
                     "E": numlist[2]}

    def roll(self, direction):
        t = dict(self._men)

        if direction == "N":
            self._men["T"] = t["S"]
            self._men["B"] = t["N"]
            self._men["N"] = t["T"]
            self._men["S"] = t["B"]
        elif direction == "S":
            self._men["T"] = t["N"]
            self._men["B"] = t["S"]
            self._men["S"] = t["T"]
            self._men["N"] = t["B"]
        elif direction == "W":
            self._men["T"] = t["E"]
            self._men["B"] = t["W"]
            self._men["W"] = t["T"]
            self._men["E"] = t["B"]
        elif direction == "E":
            self._men["T"] = t["W"]
            self._men["B"] = t["E"]
            self._men["W"] = t["B"]
            self._men["E"] = t["T"]


    def clock(self):
        t = dict(self._men)
        self._men["E"] = t["N"]
        self._men["N"] = t["W"]
        self._men["W"] = t["S"]
        self._men["S"] = t["E"]


    def simpleequal(self, d2):
        if self._men == d2._men:
            return True
        else:
            return False


    def equal(self, d2):
        for _ in range(4):
            d2.roll("N")

            for _ in range(4):
                d2.clock()
                if self.simpleequal(d2):
                    return True

        d2.roll("E")
        for _ in range(4):
            d2.clock()
            if self.simpleequal(d2):
                return True


        d2.roll("E")
        d2.roll("E")
        for _ in range(4):
            d2.clock()
            if self.simpleequal(d2):
                return True



    def gettop(self):
        return self._men["T"]

def decode():
    n = int(input())
    nlists = []
    for _ in range(n):
        numlist = [int(x) for x in input().split()]
        nlists.append(numlist)

    return n, nlists


def isunique(dices):
    for i in range(n-1):
        for j in range(i+1, n):
            if dices[i].equal(dices[j]):
                return False
    return True


if __name__ == '__main__':

    n, nlists = decode()
    dices = []
    for numlist in nlists:
        dices.append(dice(numlist))

    if isunique(dices):
        print("Yes")
    else:
        print("No")