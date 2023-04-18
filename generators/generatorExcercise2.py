class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.i=2
    def __next__( self ):
        for num in range(self.i,self.stop):
            for j in range(2,num):
                if (num%j)==0:
                    break

            else:
                self.i=num+1
                return num
        raise StopIteration()


g=PrimeGenerator(10)
print(next(g))