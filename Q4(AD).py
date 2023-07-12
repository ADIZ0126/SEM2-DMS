'''
DMS QUESTION 4
'''

n=3
c=7
def fun(a,n):
    s=sum(a)
    
    if (n==1):
        print(a+[c-s])
    else:
        for i in range(0,c-s+1):
            fun(a+[i],n-1)
                       		    
fun([],n)					
	
	
