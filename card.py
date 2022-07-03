class Var:
    ZINDEX = 0
    def get_zindex():
        Var.ZINDEX += 1
        return Var.ZINDEX


class Block:
    def __init__(self, x, y, *other):
        self.pos = x + y * 1j
        self.z = 0
        self.per = other

    def __str__(self):
        return '{' + f'x: {self.pos.real}, y: {self.pos.imag}, z: {self.z}' + '}'

    def print(self):
        print('- position: {' + f'x: {self.pos.real}, y: {self.pos.imag}, z: 0' + '}')
        print('  dependancy:')
        if len(self.per) == 0:
            print('  - dependancy: {' + f'x: 0, y: 0, z: {Var.get_zindex()}' + '}')
        else:
            for i in self.per:
                print('  - dependancy: ' + str(i))
        print('''    isfull: 0
  isDepended: 0
  currentShape: {fileID: 0}
  sortingOrder: 0''')


class Level:
    def __init__(self):
        self.blocks = []

    def print(self):
        for i in self.blocks:
            i.print()

def main():
    lev = Level()
    a = Block(1,2)
    b = Block(0,2)
    c = Block(1,1)
    d = Block(0,1)
    e = Block(1.5, 1.5, a, b, c, d)
    lev.blocks = [a,b,c,d,e]
    lev.print()


main()
