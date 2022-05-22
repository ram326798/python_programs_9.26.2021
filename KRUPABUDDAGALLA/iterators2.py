"""class Mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <= 20:
            x =3 * self.a
            self.a=self.a + 1   
            return x
        else:
         raise StopIteration
myclass=Mynumbers()
myiter=iter(myclass)

for x in myiter:
    print(x)
    """



class Mynumbers:
    def __iter__(self):
        self.a=3
        return self
    def __next__(self):
        if self.a <= 10:
            x=3*self.a
            self.a = self.a +1
            return x
        else:
            raise StopIteratio
myclass=Mynumbers()
myiter=iter(myclass)           

for x in myiter:
    print(x)