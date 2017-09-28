# 利用装饰函数property实现将函数作为属性来访问
# 属性.setter 装饰函数来实现对属性的赋值

class Screen():
    
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def resolution(self):
        return self.__width * self.__height
    
    @width.setter
    def width(self,value):
        self.__width = value

    @height.setter
    def height(self,value):
        self.__height = value
        
s = Screen()
s.width = 1024
s.height = 768

print (s.width)
print (s.height)

print(s.resolution)
