#method-1 slicing
'''
a='Praveen'
print(a[::-1])'''

#method-2 for loop
'''
a="Praveen"
c=""
for i in a:
    c=i+c
print(c)'''

#method-3 while loop
'''
a="Praveen"
c=''
l=len(a)-1
while l>=0:
    c=c+a[l]
    l=l-1
print(c)'''

#method-4 using list
'''
a='Praveen'
c_list=list(a)
c_list.reverse()
print(''.join(c_list))'''

#method-5 reversed()
a='Praveen'
reverse_str=reversed(a)
print(''.join(reverse_str))