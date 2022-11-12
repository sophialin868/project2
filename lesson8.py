def sayHello():
    print("hello")

def sayHello_withname(name):
    print(f"{name}哩賀")

def square_area(side):
    area=side**2
    return area

def rectangle (width,height):
    area=width*height
    return area

if __name__=="__main__":
   side=eval(input("叫你KEY方型邊長啦"))
   area=square_area(side)
print(f"方型,一邊為{side}面積是{area}")

area=rectangle(15.5,12)
print(f"矩形寛15.5,高12,面積{area}")
