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


    def settopsouth(self, top, south):
        if self._men["T"] == top:
            pass
        elif self._men["S"] == top:
            self.roll("N")
        elif self._men["N"] == top:
            self.roll("S")
        elif self._men["W"] == top:
            self.roll("E")
        elif self._men["E"] == top:
            self.roll("W")
        elif self._men["B"] == top:
            self.roll("N")
            self.roll("N")

        if self._men["S"] == south:
            return self._men["E"]
        elif self._men["E"] == south:
            return self._men["N"]
        elif self._men["N"] == south:
            return self._men["W"]
        elif self._men["W"] == south:
            return self._men["S"]


    def gettop(self):
        return self._men["T"]

def decode():
    numlist = [int(x) for x in input().split()]
    n = int(input())
    qs = []
    for _ in range(n):
        al = [int(x) for x in input().split()]
        qs.append(al)

    return numlist, n, qs


if __name__ == '__main__':

    numlist, n, qs = decode()
    d1 = dice(numlist)
    for q in qs:
        print(d1.settopsouth(*q))


