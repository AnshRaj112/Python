x = "Gone" 
if x == "Go": 
    print('Go') 
else: 
    print('Stop') 
print('Mike')

x = 1 
x = x > 5
print(x)

x = 0 
while x < 2: 
    print(x) 
    x = x + 1

class Points(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y 


    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 


p1 = Points("A", "B") 
p1.print_point()
for i, x in enumerate(['A', 'B', 'C']): 
    print(i + 1, x)
    
class Points(object): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 


p2 = Points(1, 2) 
p2.x = 2 
p2.print_point()

a = 1 


def do(x): 
    return x + a 


print(do(1))
