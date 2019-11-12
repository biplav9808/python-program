a={'name':['ram','shyam'],'no':[1,2] }
b={'caste':34}
a.update(b)
print(a)

dict1={'no1':10,'no2':20}
dict2={'no3':30,'no4':40}
dict4={}
for d in (dict1,dict2):dict4.update(d)
print(dict4)
del(dict4['no1'])
print(dict4)
if 'no1' in dict4:
    print('key is present')
else:
    print('key is not present')

