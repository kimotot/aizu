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


    def gettop(self):
        return self._men["T"]

def decode():
    numlist = [int(x) for x in input().split()]
    dlist = input()
    return numlist, dlist

if __name__ == '__main__':

    numlist, dlist = decode()
    d1 = dice(numlist)
    for c in dlist:
        d1.roll(c)
    print(d1.gettop())



