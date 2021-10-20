#iterator is an object that contains a countable number of values
"""
l=['ram',24,True,'Krish']
it=iter(l)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
"""
#iteration for strings
"""
s="Hello World"
it=iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
"""
#iterating using for loop
"""
l=['ram',24,True,'Krish']
for i in l:
    print(i)
"""
#Iterating in class using __iter__ __next__
"""
class MyClass:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
m=MyClass()
it=iter(m)
print(next(it))
print(next(it))
print(next(it))
"""
#Iterating in class using __iter__ __next__ and StopIteration to stop iterations
class MyClass:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if(self.a<=4):
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
m=MyClass()
it=iter(m)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))