import csv


class Bullet:
    def __init__(self, calibr, mass):
        self.calibr = calibr
        self.mass = mass
        self.power = float(self.calibr) * self.mass


class ClipStack:
    def __init__(self):
        self.holder = []

    def add_item(self, n, calibr, mass):
        for i in range(n):
            self.holder.append(Bullet(calibr, mass))

    def delete_item(self):
        if len(self.holder > 0):
            self.holder.pop(-1)
        else:
            print("No bullets")


def writer():
    f = open("data.txt", "w")
    f.write("In clip " + str(len(first_clipstack.holder)) + " bullets:\n")
    for i in range(len(first_clipstack.holder)):
        f.write(
            f"Bullet{i}: {first_clipstack.holder[i].calibr} , {first_clipstack.holder[i].mass} , {first_clipstack.holder[i].power}\n")
    f.close()


if __name__ == "__main__":
    first_clipstack = ClipStack()
    first_clipstack.add_item(10, "5.56", 100)
    writer()


