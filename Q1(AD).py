'''
DMS PRACTICAL QUESTION 1
'''

import numpy as np

class SET:
    def __init__(self,ar,size):
        self.arr = ar
        self.size = size


    #CHECKING WHETHER THE GIVEN ELEMENT IS PRESENT IN THE SET
    def ismember(self):
        arr1 = self.arr
        x = int(input('Enter an element: '))

        for i in arr1:
            if i == x:
                print('TRUE')
                break
        else:
            print('FALSE')

    #FINDING POWER SET   
    def powerset(self):
        ps = []
        n1 = self.size
        arr1 = self.arr
        
        for i in range(2**n1):
            bi = ''     #store binary equivalent of i
            ss = []     #store subsets of power set
            
            while i > 0:
                rem = i%2
                
                bi = bi + str(rem)
                i = i//2
            bi = bi[::-1] 

            while len(bi) != n1:
                bi = '0' + bi
            
            for j in range(n1):
                if bi[j] == '1':
                    ss.append(arr1[j])

            ps.append(ss)
            
        print('Power Set of the Given Array:  ', ps)

    #CHECKING WHETHER THE GIVEN SET IS THE SUBSET OF THE MAIN SET
    def subset(self,arr2):
        arr1 = self.arr
        check = 0

        for i in arr2:
            for j in arr1:
                if i == j:
                    check = 1
                    break
                else:
                    check = 0
            
            if check == 0:
                print('Arr2 is not subset of Arr1')
                break

        if check == 1:
            print('Arr2 is a subset of Arr1')
            if n1 != n2:
                print('Arr2 is proper subset of Arr1')




    #FINDING UNION OF THE 2 SETS
    def union(self,ar2):
        arr1 = self.arr
        arr3 = arr1
        l = []

        for i in ar2:
            if i not in arr3:
                l.append(i)
        
        arr3 = list(arr1) + l
        print('Union : ' , arr3)
        return arr3

    #FINDING SET DIFFERENCE OF THE 2 SETS
    def difference(self,ar2):
        arr1 = self.arr
        print(arr1)
        arr3=[]
        for i in arr1:
            if i not in ar2:
                arr3 = arr3 + [i]
        print('Difference : ', np.array(arr3) , "\n")

    #FINDING COMPLEMENT OF THE SET
    def complement(self):
        uni = eval(input("Enter the universal set: "))
        comp = []
        
        for i in uni:
            if i not in self.arr:
                comp.append(i)
        
        print("Complement Of The Given Set is: " , comp)


    #FINDING SYMMETRIC DIFFERENCE OF THE 2 SETS
    def symmetric(self,uni,inter):
        arr3=[]
        uni = array1.union(ar2)
        inter = array1.intersection(ar2)
        for i in uni:
            if i not in inter:
                arr3 = arr3 + [i]
        print('Symmetric Difference: ', np.array(arr3))


    #FINDING CARTESIAN PRODUCT OF THE 2 SETS
    def cartprod(self,arr2):
        arr1 = self.arr
        arr3 = []

        for i in arr1:
            for j in arr2:
                ele = [i,j]
                arr3.append(ele)

        print('Cartesian Product - Arr1 X Arr2 : ',np.array(arr3))



        
l1 = eval(input("Enter the first set: "))
l2 = eval(input("Enter the second set: "))

#INITIALIZNG SETS
ar1 = np.array(list(l1))
ar2 = np.array(list(l2))

n1 = len(l1) # length of array1
n2 = len(l2) # length of array2

#CREATING OBJECTS
array1 = SET(ar1,n1)
array2 = SET(ar2,n2)

print("THE SETS ARE:")
print("SET1: " , array1)
print("SET2: " , array2)

while True:
    print('''\n
1) ismember: check whether an element belongs to the set or not and return value as true/false.
2) powerset: list all the elements of the power set of a set .
3) subset: Check whether one set is a subset of the other or not.
4) union and Intersection of two Sets.
5) complement: Assume Universal Set as per the input elements from the user.
6) set Difference and Symmetric Difference between two sets.
7) cartesian Product of Sets
8) Exit\n''')
    
    opt = int(input("Enter Your Chocie: "))
 
    if opt == 1:
        array1.membership()

    elif opt == 2:
        array1.powerset()
    
    elif opt == 3:
        array1.subset(ar2)
    
    elif opt == 4:
        uni = array1.union(ar2)
    
    elif opt == 5:
        array1.complement()
    
    elif opt == 6:   
        array1.difference(ar2)
        array1.symmetric(uni,inter)
    
    elif opt == 7:
        array1.cartprod(ar2)

    elif opt == 8:
        break

    print()
