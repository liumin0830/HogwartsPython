"""测试计算器(加、减、乘、除）"""

class Calculator:

    # 是否为float
    def hasFloat(self, num):
        strNum = str(num)
        if strNum.count(".") == 1:
            ind = strNum.index(".") + 1
            return len(strNum[ind:])
        else:
            return 0

    # 输入不为数字
    def isscalar(self, num):
        try:
            float(num)
        except Exception:
            return True
        else:
            return False

    def setup(self):
        # 输入都要判断是否float类型
        # 输入都要判断是否为非数字类型
        pass


    def add(self,num1,num2):
        # 非数字判断
        if self.isscalar(num1) or self.isscalar(num2) :
            return "输入类型错误"
        else:
            # float类型判断
            fn1 = self.hasFloat(num1)
            fn2 = self.hasFloat(num2)
            if fn1 == 0 and fn2 == 0:
                return num1 + num2
            else:
                return round(num1 + num2, fn1 if fn1 >= fn2 else fn2)

    def sub(self,num1,num2):
        # 非数字判断
        if self.isscalar(num1) or self.isscalar(num2):
            return "输入类型错误"
        else:
            # float类型判断
            fn1 = self.hasFloat(num1)
            fn2 = self.hasFloat(num2)
            if fn1 == 0 and fn2 == 0:
                return num1 - num2
            else:
                return round(num1 - num2, fn1 if fn1 >= fn2 else fn2)

    def mul(self,num1,num2):
        # 非数字判断
        if self.isscalar(num1) or self.isscalar(num2):
            return "输入类型错误"
        else:
            # float类型判断
            fn1 = self.hasFloat(num1)
            fn2 = self.hasFloat(num2)
            if fn1 == 0 and fn2 == 0:
                return num1 * num2
            else:
                return round(num1 * num2, (fn1 + 1) if fn1 >= fn2 else (fn2 + 1))

    def div(self,num1,num2):
        # 非数字判断
        if self.isscalar(num1) or self.isscalar(num2):
            return "输入类型错误"
        # 除数不能为0，如果是0.0000呢？？？
        elif num2 == 0:
            return "除数不能为0"
        else:
            # float类型判断
            fn1 = self.hasFloat(num1)
            fn2 = self.hasFloat(num2)
            if fn1 == 0 and fn2 == 0:
                return num1 / num2
            else:
                return round(num1 / num2, fn1 if fn1 >= fn2 else fn2)

# if __name__ == "__main__":
#     calc = Calculator()
#     print(calc.sub(0.35, 0.15))