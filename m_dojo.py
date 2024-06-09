class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        result = self.result + num
        for n in nums:
            result += n
        new_instance = MathDojo()
        new_instance.result = result
        return new_instance

    def subtract(self, num, *nums):
        result = self.result - num
        for n in nums:
            result -= n
        new_instance = MathDojo()
        new_instance.result = result
        return new_instance

md = MathDojo()
md.add(2)
print(md.result)
md.add(2,5,1)
print(md.result)
md.subtract(3,2).add(10)
print(md.result)
md.subtract(5)
print(md.result)
md.subtract(2,3)
print(md.result)
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)
