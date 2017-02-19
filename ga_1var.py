from __future__ import division
import math
import copy
import random

def variable_generator(num):
    var_array = [] 
    for i in range(num):
        var_array.append('x%s'%(i+1))

    return var_array

def generating_gene_size(mini, maxi):
    
    gene_order_decide = max(abs(mini), abs(maxi))
    bits = 20

    while gene_order_decide <= 2 ** bits :
        bits-=1
    
    bits = bits + 2
    
    gene = []
    
    for i in range(bits):
        gene.append(0)
 
    return gene
no_of_variables = 1
array_var = variable_generator(no_of_variables)
variable1min = -32
variable1max = 32


array_var[0] = generating_gene_size(variable1min, variable1max)





x1 = 0



#generating the population size = n
n= 5
global_array = []
for k in range(n):
    #random initialization of array_var
    for i in range(no_of_variables):
        for j in range(len(array_var[i])):
            c = random.randint(0, 10000)
            if c>=5000:
                array_var[i][j] = 1
            else:
                array_var[i][j] = 0
    l = copy.deepcopy(array_var)
    global_array.append(l)

eq_value = [0 for x in range(n)]
eq_final = [0 for x in range(n)]
fitness = [[1 for x in range(2)] for y in range(n)]
no_of_iterations = 100
fitness_print = [0 for x in range(n)]
fitness_final = [1 for i in range(n)]
for k in range(no_of_iterations):
        
	for i in range(n):
	#variable 1 penality and calculation
	    x1 = 0
	    
	    
	    for j in range(len(global_array[i][0])-1):
		x1 = x1 + global_array[i][0][len(global_array[i][0])-1-j] * 2**j
	    x1 = x1-1
	    if global_array[i][0][0] == 0:
		x1 = x1*(-1)
	    
            #print(x1, variable1min)
            #print(float(variable1min - x1)/abs(2*variable1min))
	      
	    if x1 < variable1min:
		fitness[i][0] = 1 -float(variable1min-x1)/abs(2*variable1min)
	    
	    if x1 > variable1max:
		fitness[i][0] = 1 -float(x1-variable1max)/abs(2*variable1max)
            #print(fitness[i][0])
		 
            eq = -20
            print(eq)	    
	    if eq < 0:
	       eq_value[i]=(abs(15*eq))
	    else:
	       eq_value[i]=(eq)
            eq_final[i] = eq

	#calculating the overall fitness

	total_value = sum(eq_value)
	if total_value == 0:
	   total_value = max(eq_value) 

	for i in range(n):
	    fitness[i][1] =1-(eq_value[i]/total_value)**0.5 
	    
	
	#fitness after penalties
	for i in range(n):
	    fitness_final[i]=(fitness[i][0]*fitness[i][1])

     
	total_fitness = sum(fitness_final)

	if total_fitness == 0:
	   total_fitness = 1
	   for i in range(n):
	       fitness_final[i] = 1/n

	else:
	    for i in range(n):   
	        fitness_final[i] = fitness_final[i]/total_fitness

        fitness_print = fitness_final
	#Roulette Wheel And Cross Over


	array_roulette = [[1 for i in range(2)]for j in range(n)]
	for i in range(n):

	    if i == 0:
		array_roulette[0][0] = 0
		array_roulette[0][1] =100* fitness_final[0]
	    
	    else:
		for j in range(2):
		    array_roulette[i][0] = array_roulette[i-1][1]
		    array_roulette[i][1] =100* fitness_final[i] + array_roulette[i][0] 
	#print(array_roulette)    
	for z in range(n):
	    c1 = random.uniform(0,100)
	    gene_case1 = 0
	    gene_case2 = 0
	    for j in range(n):  
		if c1<array_roulette[j][1] and c1 >= array_roulette[j][0]:
		    gene_case1 = j
		else:
		    pass
	    
	    c2 = random.uniform(0,100)
	    for j in range(n):  
		if c2<array_roulette[j][1] and c2 >= array_roulette[j][0]:
		    gene_case2 = j
		else:
		    pass
	   #print(gene_case1, gene_case2)
	   #cross over
	   
	    dummy_array2 = global_array[gene_case2]
	    for i in range(len(global_array[gene_case1][0])):
		d =  random.uniform(0,1)
		if d >=0.3:
		    global_array[gene_case2][0][i] = global_array[gene_case1][0][i]
		else:
	            pass

	    	    
		
		    

	#print(global_array[1])
	#mutation
	#mutation needs to be improved
	e1 = random.uniform(0,100) 
	if e1 <= 2: 
	    mutation_no = random.randint(1,n)
	    for i in range(mutation_no):
		e2 = random.randint(0,n-1)
		e3 = random.randint(0, len(global_array[e2][0])-1)
		if global_array[e2][0][e3] == 1:
		   global_array[e2][0][e3] =0
	       
		else:
		   global_array[e2][0][e3] =1
		
		
		
          


#post processing
check = 0
x1=0

for i in range(n):
    if min(eq_final) == eq_final[i]:
         check = i
         break  

for j in range(len(global_array[check][0])-1):
    x1 = x1 + global_array[check][0][len(global_array[check][0])-1-j] * 2**j

x1 = x1 -1
if global_array[check][0][0] == 0:
    x1 = x1 * (-1)
print(x1)


print(min(eq_final),'', 'x1', x1)
#this is not the overall minima , this is the minima of the last iteration...its a drawback, may not work always

q = -20

print(q)
