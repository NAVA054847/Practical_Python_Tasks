import matplotlib .pyplot as m
#1

x=[1,2,3,5]
y=[1,8,125,27]

m.plot(x,y,'red')
#2
print(m.style.available)

#3
m.plot(x,y,'red','classic')

#4
m.xlabel("title X")
m.ylabel("title Y")

#5
m.plot(x,y,'green',linewidth=3)
#6
y1=[0.33,0.67,1.67,1]
m.plot(x,y,'red')
m.plot(x,y1,'blue')
m.show()