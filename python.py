import json

a= [1,2,3,4,5,6,7,8,9,10]
print(a)

b=[el*2 for el in a] # double everything
print(b)
print([el*10 for el in a]) # 10X everything

print([el for el in a if el%2 ==0])  # filter even nums
print([el for el in a if el%2 !=0])  # filter odd nums
print([el for el in a if el%5 ==0])  # filter multiples of 5


c= [['a','b','c'],[1,2,3]]

d= [[el for el in lst if isinstance(el, str)] for lst in c] # filter strings
print(d)

e= [[el for el in lst if isinstance(el, int)] for lst in c] # filter ints
print(e)


def multiplesOf(n,a):
    return [el for el in a if el%n==0]


print(multiplesOf(3,a))


import json

print (json.dumps({'a':2, 'b':{'x':3, 'y':{'t1': 4, 't2':5}}}, indent=4))


x = [0] * 10
print x 
y = [i+1 for i in xrange(10)]
print y