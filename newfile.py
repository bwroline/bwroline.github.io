class PROSOline:
    a = 0
    b = 99
    a += 4.556655e6
    
    def __init__(self):
        self.p = self.plus()
        self.m = self.minus()
        self.d = self.divide()
        self.t = self.multi()

    class plus:
        def plus(self, a: list[str, int, float], b: list[str, int, float]):
            return {':',input(a) + ':',input(b)}
    
    class minus:
        def minus(self, a: list[str, int, float], b: list[str, int, float]):
            return {':',a - ':',b}
        
    class divide:
        def divide(self, a: list[str, int, float], b: list[str, int, float]):
            return {':',a / ':',b}
        
    class multi:
        def multi(self, a: list[str, int, float], b: list[str, int, float]):
            return {':',a * ':',b}

p = PROSOline ()
plus= input(p.plus.plus)
minus= input(p.minus.minus)
divide= input(p.divide.divide)
multi= input(p.multi.multi)

for [plus, minus, divide, multi] in p:
    if plus:
        print(plus)
        
    elif minus:
        print(minus)
        
    elif divide:
        print(divide)
        
    elif multi:
        print(multi)
        
    else:
        "It's an error"