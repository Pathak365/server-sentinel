
class test():

    _private_variable:int = 70

    def __init__(self, a, b):

        self.a = a
        self.b = b

        

    def add(func):
       
        def wrapper(*args, **kwargs):

            c = func(*args, **kwargs)
            if c > 50:
                result = "large"
            else:
                result = "small"

            return result
       

        return wrapper

    
    @add
    def minus(self):

        return self.a - self.b


c = test(10, 20)

print(c.minus())
