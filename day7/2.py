import operator as op

ops =   {None   : lambda x: x,
        "NOT"   : op.invert,
        "OR"    : op.or_,
        "AND"   : op.and_,
        "RSHIFT": op.rshift,
        "LSHIFT": op.lshift
        }

gates = {}


class Gate:

    def __init__(self, oper=None, *inwire):
        self.oper = oper
        self.inv = [int(x) if x.isdigit() else x for x in inwire]
        self.out = 0

    def calc(self):
        if not self.out:
            self.out = ops[self.oper](*[x if isinstance(x, int) else gates[x].calc() for x in self.inv]) & 0xFFFF
        return self.out


with open('input.txt') as f:
    for line in f:
        in_d, out_d = line.strip().split('-> ')
        in_d = in_d.split()

        if len(in_d) == 1: gates[out_d] = Gate(None, in_d[0])
        else: gates[out_d] = Gate(in_d.pop(-2), *in_d)

    tmp = gates['a'].calc()

    for _, gate in gates.items():
        gate.out = 0
        gates['b'].out = tmp

    ans = gates['a'].calc()


with open('output2.txt', 'w') as f:
    print(str(ans), file=f)
