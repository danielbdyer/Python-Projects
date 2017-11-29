class Calculator(object):

    def __init__(self):
        pass

    def add(self,x,y):
        return x + y

    def sub(self,x,y):
        return x - y

    def mult(self,x,y):
        return x * y

    def div(self,x,y):
        solution = x / y
        solution_int = int(solution)
        remainder = int(x % y)
        if remainder == 0: return solution
        else: return repr(solution_int) + "R" + repr(remainder)

    def fact(self,x):
        if x <= 1:
            return x
        else:
            return x * self.fact(x - 1)
