import  pandas as pd


#1

mydataset = {
  'cars': ["Banana", "Apple"],
  'passings': [21,30]
}

myvar = pd.DataFrame(mydataset)
print(myvar, end="\n")

myvar.index=['2017 sales','2018 sales']

print(myvar, end="\n")

#2
#מדובר על שורה עמודה בתוך ה DF
#myvar2 = pd.Series(['b','g'])
# print(myvar2, end="\n")
# myvar['color']=myvar2
# print(myvar, end="\n ##################\n")



#3

mydataset_1 = {
  'products': ["Flower", "Milk","Eggs","Spam"],
  'how_much': [4,1,2,1],
  'size':["cups","cup","large","can"]
}

myvar = pd.DataFrame(mydataset_1)
print(myvar, end="\n  -----------------")


#4

mydataset_2 = {
  'products': ["Flower", "Milk","Eggs","Spam"],
  'how_much': [100,60,37,100],
  'size':["1","2","1","4"]
}

myvar = pd.DataFrame(mydataset_2)
print(myvar, end="\n  -----------------")

#5

myvar3=pd.DataFrame()
print(myvar3)