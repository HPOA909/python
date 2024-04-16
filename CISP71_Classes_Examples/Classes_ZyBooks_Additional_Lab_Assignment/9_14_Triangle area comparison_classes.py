#9.14 LAB: Triangle area comparison (classes) from zybooks
class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print('Base: {:.2f}'.format(self.base))
        print('Height: {:.2f}'.format(self.height))
        print('Area: {:.2f}'.format(self.get_area()))

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()
      
    # Read and set base and height for triangle1 (use set_base() and set_height())
    user_base = float(input("Base: "))
    user_height = float(input("Height: "))
    triangle1.set_base(user_base)
    triangle1.set_height(user_height)

    # Read and set base and height for triangle2 (use set_base() and set_height())
    user_base = float(input("Base: "))
    user_height = float(input("Height: "))
    triangle2.set_base(user_base)
    triangle2.set_height(user_height)

    # Determine larger triangle (use get_area())
    print('Triangle with larger area:')
      
    if triangle1.get_area() > triangle2.get_area():
        # Output larger triangle's info (use print_info())
        triangle1.print_info()
      
    else:
        # Output larger triangle's info (use print_info())
        triangle2.print_info()