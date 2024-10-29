"""dict={}
for item in range(4):
    key=input("enter key here:")
    value=input("enter value here:")
    dict[key]=value
    print(dict)"""

"""x={"a":200,"b":300,"c":400}
print(sum(x.values()))"""

"""def congrats(name):
 print("hi hello congratulations",name)
congrats("siva")
congrats("kamal")
"""

"""def add(x,y):
 print(x+y)
 print(x*y)
add(10,20)
add(3.2,7.8)
add(3.5,7.6)
add(7.8,2.5)
"""
"""def result(m,p,c,e,h):
    totalmarks =m+p+c+e+h
    print(totalmarks)
    print((totalmarks/tm)*100)
    m=23
    p=34
    c=46
    e=87
    h=97
    tm=500
    result(m,p,c,e,h)"""

"""l= [1,2,3,4,5,6,7,8,9]
count=0
for i in l:
    count=count+1
    print(count)
print(len(l))

l=lambda x,y: x if x>y else y
print(l(100,20))"""

"""def get_odd(l):
    if l%2==1 :
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9]
f=filter (get_odd,l)
print(list(f))"""

l = [1,2,3,4,5,6,7,8,9]
rs=reduce (lambda x,y:x+y,l)
print(rs)





