#!/anaconda2/bin/python

class Units( object):
    def __init__( self, unitstring, inverse=False, chars=3):
        self.top = unitstring[:chars] 
        self.bot = unitstring[chars:]
        self.inv = inverse
        if self.inv: self.inverse()
            
    def inverse( self):
        bot, top = self.top, self.bot
        self.top, self.bot = top, bot

    @staticmethod
    def compute( unitList):
        if not len(unitList):
            return unitList[0].top+unitList[0].bottom
        #move left to right
        unitString = ''
        for i in range( 1, len(unitList)):
            unitString+=Units.compare( unitList[i-1].top, unitList[i-1].bot, unitList[i].top, unitList[i].bot)
        return unitString

    @staticmethod
    def compare( top1,bot1,top2,bot2):
        if top1==bot2:
            units=''
        else:
            units=top1+bot2
        if bot1!=top2:
            units+=bot1+top2
        return units

def main():
    #create currency trading pairs
    one,two,three='btcusd','btceur','eurusd'
    #initialize units
    oneInst = Units(one,True)
    twoInst = Units(two)
    threeInst = Units(three)
    #convert units for one and two
    conversion = Units.compute([oneInst,twoInst])
    print 'one * two: {}'.format(conversion)
    #convert units for result of one/two and three
    final = Units.compute([Units(conversion),threeInst])
    #show final units after three moves
    print 'final {}:'.format( final), len(final)
    #proof of concept complete for units, cancellation works
    #len 0 result means we moved back to where we started

if __name__=='__main__':
    main()
    #pass
