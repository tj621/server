import json
a='345436587600035'
print a
b=[]
v='''{
    "temp":%s
}'''% str(a)

c='''[[345436587600035,23],[345436587600035,234]]'''
d='''{
    "data":%s
}'''% c
print d

b.append(v)
print b
