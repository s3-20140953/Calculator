from graphic import *
#Control Data

class Calculator(Graphic):

    def __init__(self):
        self.result = 0

    def sum_num(self,num1,num2):
        self.result = num1 + num2
        return self.result

    def minus_num(self,num1,num2):
        self.result = num1 - num2
        return self.result

    def multi_num(self,num1,num2):
        self.result = num1 * num2
        return self.result

    def div_num(self,num1,num2):
        self.result = num1 / num2
        return self.result

    def pow_num(self,num1,num2):
        self.result = num1 ** num2
        return self.result
