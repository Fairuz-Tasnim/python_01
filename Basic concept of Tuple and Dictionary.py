 
'''print("Input the heights of eight buildings:")

# List comprehension to take input for the heights of eight buildings
l = [int(input()) for i in range(8)]

# Print statement to display the heights of the top three buildings
print("Heights of the top three buildings:")

'''# Sorting the list of building heights in ascending order
'''l=[29,34, 38,63,22,80,2,12,25,76,44]
l = sorted(l)

# Printing the top three building heights in descending order using slicing and the 'sep' parameter for newlines
print(l)
List= l[8:-1]
print(List)'''
'''list1=["orange",[10,20,30],[5,15,25]]
index1=int(input("Enter index 1 of the slice: "))
index2=int(input("Enter index 2 of the slice: "))
print(list1[index1][index2])'''
'''Tuple1=(11,22)
Tuple2=(99,88)
temp =Tuple1
Tuple1=Tuple2
Tuple2= temp
print(Tuple1)
print(Tuple2)'''

'''Tuple= (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
element = 'yellow'
for i in Tuple:
   if(element in i):
      print("yes")
   else:
      print("No")
Dictionary= {1: 'A',2:'B',3:'C'}
print(Dictionary)
for index in Dictionary:
    value= Dictionary[index]
    print(value)
D = {'Name': 'AI', 1: [1, 2, 3, 4]}
print(D['AI'])

Dict = {'Dict1': {1: 'AB'},
        'Dict2': {'CD': 'DE'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['CD'])'''

'''input_dict = {'Math': 90, 'DSA': 80, 'Algo': 95, 'Python': 75}
acending = dict(sorted(input_dict.items()))
print(acending)
decending=dict(reversed(acending.items()))
print(decending)


test_dict = {'silver' : 4, 'gold' : 2, 'diamond' : 5} 
#print(str(test_dict)) 
res =dict(reversed(test_dict.items()))
print(res)

n= int(input("enter a number: "))
d=dict()
for i in range(1,n+1):
    d={i:i*i}
    print(d)
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d={}
for i,j in d1.items():
    d[i]=j
for i,j in d2.items():
   if i in d:
      d[i]+=j
   else:
      d[i]=j

print(d)

string= "Intilligence"
d={}
for i in string:
    d[i]=d.get(i,0)+1
print(d)'''
List = [1,2,'A','B',6.3]
print(List[-1])
print(List[-3])

