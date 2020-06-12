from pytest import raises
from libplf import plf
from libplf import piece
from libplf import point
from libplf import vector


class Test:
    def test(self):
        f = plf(*self.args())
        for x, y in self.rets():
            assert f(*x) == y

    def args(self):
        return [
            piece(
                point(vector(0), vector(0)),
                point(vector(1), vector(1)),
            )
        ]

    def rets(self):
        return []


class Test_1_1(Test):
    def args(self):
        return [
            piece(
                point(vector(ax), vector(ay)),
                point(vector(bx), vector(by)),
            )
            for (ax, ay), (bx, by) in self.defs()
        ]

    def defs(self):
        return [
            [(0, 0), (1, 1)],
        ]

    def rets(self):
        return [
            [
                (0.5,),
                vector(0.5),
            ]
        ]

class Test_1_2(Test):
    def args(self):
        return [
            piece(
                point(vector(ax), vector(ay, az)),
                point(vector(bx), vector(by, bz)),
            )
            for (ax, ay, az), (bx, by, bz) in self.defs()
        ]

    def defs(self):
        return [
            [(0, 0, 0), (1, 1, 1)],
            [(1, 1, 1), (2, 2, 3)],
        ]
    def rets(self):
        return [
            [
                (1.5,),
                vector(1.5,2),
            ]
        ]

class Test_2_1(Test):
    def args(self):
        return [
            piece(
                point(vector(ax, ay), vector(az)),
                point(vector(bx, by), vector(bz)),
                point(vector(cx, cy), vector(cz)),
            )
            for
            (ax, ay, az),
            (bx, by, bz),
            (cx, cy, cz),
            in self.defs()
        ]

    def defs(self):
        return [
            [
                (0, 0, 0),
                (1, 0, 1),
                (0, 1, 2),
            ],
            [
                (1, 1, -2),
                (1, 2, -3),
                (2, 1, -3),
            ]
        ]
    def rets(self):
        return [
            [
                (1, 0),
                vector(1),
            ]
        ]


class Test_2_2(Test):
    def args(self):
        return [
            piece(
                point(vector(ax, ay), vector(az, au)),
                point(vector(bx, by), vector(bz, bu)),
                point(vector(cx, cy), vector(cz, cu)),
            )
            for
            (ax, ay, az, au),
            (bx, by, bz, bu),
            (cx, cy, cz, cu),
            in self.defs()
        ]

    def defs(self):
        return [
            [
                (0, 0, 0, 1),
                (1, 0, 1, 1),
                (0, 1, 2, 1),
            ],
            [
                (1, 1, -2, 1),
                (1, 2, -3, 1),
                (2, 1, -3, 1),
            ]
        ]

    def rets(self):
        return [
            [
                (1.5, 1),
                vector(-2.5, 1),
            ]
        ]