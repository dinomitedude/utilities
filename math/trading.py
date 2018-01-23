#!/anaconda2/bin/python

from units import Units

class Commodity( object):
    def __init__( self, price, units):
        self.price = price
        self.units = Units( units)

    def inverse( self):
        return 1.0/self.price, self.units.inverse()

class Triarb():
    def __init__( self, sideOne, sideTwo, sideThree):
        self.sideOne = sideOne
        self.sideTwo = sideTwo
        self.sideThree = sideThree

    @staticmethod
    def compute( sideOne, sideTwo, sideThree):
        t1 = Units.compute([sideOne.units,sideTwo.units])
        f = Units.compute([Units(t1),sideThree])
        if not f:
            print t1, f

if __name__=='__main__':
    main()
