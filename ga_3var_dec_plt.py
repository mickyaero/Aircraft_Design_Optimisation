from __future__ import division
import math
import copy
import random
import matplotlib.pyplot as plt
import numpy as np

def equation_calc(x1, x2, x3):
    #w1 = 1+(x1-1)/4
    #w2 = 1+(x2-1)/4
    #w3 = 1+(x3-1)/4
    

    expr =x1**2+x2**2+x3**2 
    return expr

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
    
    bits = bits + 2 + 10
    
    gene = []
    
    for i in range(bits):
        gene.append(0)
 
    return gene
no_of_variables = 3
array_var = variable_generator(no_of_variables)
variable1min = -8
variable1max = 8
variable2min = -8
variable2max = 8
variable3min = -8
variable3max = 8
total_value = 1

array_var[0] = generating_gene_size(variable1min, variable1max)

array_var[1] = generating_gene_size(variable2min, variable2max)

array_var[2] = generating_gene_size(variable3min, variable3max)

x1 = 0
x2 = 0
x3 = 0


#generating the population size = n
n= 250
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
fitness = [[1 for x in range(4)] for y in range(n)]
no_of_iterations = 5000
fitness_print = [0 for x in range(n)]
fitness_final = [1 for i in range(n)]
result_array = [[0 for i in range(no_of_variables+1)]for j in range(no_of_iterations)]

plt.ion()
fig, ax=plt.subplots()
plot = ax.scatter([],[])
ax.set_xlim(0, no_of_iterations)
ax.set_ylim(-5,5)

for k in range(no_of_iterations):
        
	#calculating the overall fitness

	total_value = sum(eq_value)
	if total_value == 0:
	   if max(eq_value) != 0:
               total_value = max(eq_value)
           else:
               total_value = 1
 

	for i in range(n):
	    fitness[i][3] =1-(eq_value[i]/total_value)**0.5 
	    
	
	#fitness after penalties
	for i in range(n):
	    fitness_final[i]=(fitness[i][0]*fitness[i][1]*fitness[i][2]*fitness[i][3])

     
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

	    for i in range(len(global_array[gene_case1][1])):
		d =  random.uniform(0,1)
		if d >=0.3:
		    global_array[gene_case2][1][i] = global_array[gene_case1][1][i]
		else:
		    pass


	    for i in range(len(global_array[gene_case1][2])):
		d =  random.uniform(0,1)
		if d >=0.3:
		    global_array[gene_case2][2][i] = global_array[gene_case1][2][i]
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
		
		e3 = random.randint(0, len(global_array[e2][1])-1)
		if global_array[e2][1][e3] == 1:
		   global_array[e2][1][e3] =0
	       
		else:
		   global_array[e2][1][e3] =1
		
		e3 = random.randint(0, len(global_array[e2][2])-1)
		if global_array[e2][2][e3] == 1:
		   global_array[e2][2][e3] =0
	       
		else:
		   global_array[e2][2][e3] =1
        
        for i in range(n):
	#variable 1 penality and calculation
	    x1 = 0
	    x2 = 0
	    x3 = 0
            len_array_i_var_1 = len(global_array[i][0])-10
            len_array_i_var_2 = len(global_array[i][1])-10
            len_array_i_var_3 = len(global_array[i][2])-10
	    for j in range(len_array_i_var_1-1):
		x1 = x1 + global_array[i][0][len_array_i_var_1-1-j] * 2**j
	    
            for l in range(10):
                x1 = x1 +global_array[i][0][len_array_i_var_1+l]*2**l/1024
	    
            if global_array[i][0][0] == 0:
		x1 = x1*(-1)
	    
            #print(x1, variable1min)
            #print(float(variable1min - x1)/abs(2*variable1min))
	      
	    if x1 < variable1min:
		fitness[i][0] = 1 -float(variable1min-x1)/abs(variable1min)**0.5
	    
	    if x1 > variable1max:
		fitness[i][0] = 1 -float(x1-variable1max)/abs(variable1max)**0.5
            #print(fitness[i][0])
	#variable 2 penality and calculation
	    for j in range(len_array_i_var_2-1):
		x2 = x2 + global_array[i][1][len_array_i_var_2-1-j] * 2**j
	    
	    for l in range(10):
                x2 =x2 +global_array[i][1][len_array_i_var_2+l]*2**l/1024

	    if global_array[i][1][0] == 0:
	       x2 = x2 * (-1)
	    
	    #print(x2)
	    if x2 < variable2min:
		fitness[i][1] = 1 -float(variable2min-x2)/abs(variable2min)**0.5
		   
		
	     
	    if x2 > variable1max:
		fitness[i][1] = 1 -float(x2-variable2max)/abs(variable2max)**0.5

	#variable 3 penality and calculation

	    for j in range(len_array_i_var_3-1):
		x3 = x3 + global_array[i][2][len_array_i_var_3-1-j] * 2**j
	    for l in range(10):
                x3 = x3 + global_array[i][2][len_array_i_var_3+l]*2**l/1024
	    
	    if global_array[i][2][0] == 0:
	       x3 = x3 * (-1)
	    
	   
	    if x3 < variable3min:
		fitness[i][2] = 1 -float(variable3min-x3)/abs(variable3min)**0.5
		   
	       
	     
	    if x3 > variable3max:
		fitness[i][2] = 1 - float(x3-variable3max)/abs(variable3max)**0.5
	    
            eq = equation_calc(x1, x2, x3)
            #print(eq)	    
	    if eq < 0:
	       eq_value[i]=(abs(1/eq))
	    else:
	       eq_value[i]=(eq)
            eq_final[i] = eq


        check = 0
        x1=0
        x2=0
        x3=0
        just = 0
        minima = min(eq_final)
        for i in range(n):
            if minima == eq_final[i]:
                check = i
                break  
        len_check_i_var_1 = len(global_array[just][0])-10
        len_check_i_var_2 = len(global_array[just][1])-10
        len_check_i_var_3 = len(global_array[just][2])-10
	
        for j in range(len_check_i_var_1-1):
            x1 = x1 + global_array[check][0][len_check_i_var_1-1-j] * 2**j

        for l in range(10):
            x1 = x1 + global_array[i][0][len_check_i_var_1+l]*2**l/1024
        if global_array[check][0][0] == 0:
            x1 = x1 * (-1)

        for j in range(len_check_i_var_2-1):
            x2 = x2 + global_array[check][1][len_check_i_var_2-1-j] * 2**j
        for l in range(10):
            x2 = x2 + global_array[i][1][len_array_i_var_2+l]*2**l/1024
           
        
        if global_array[check][1][0] == 0:
            x2 = x2 * (-1)

        for j in range(len_check_i_var_3-1):
            x3 = x3 + global_array[check][2][len_check_i_var_3-1-j] * 2**j

        for l in range(10):
            x3 = x3 + global_array[check][2][len_check_i_var_3+l]*2**l/1024
        if global_array[check][2][0] == 0:
            x3 = x3 * (-1)

        result_array[k][0] = minima
        result_array[k][1] = x1
        result_array[k][2] = x2
        result_array[k][3] = x3

        point = [k, result_array[k][0]]
        array_ran = plot.get_offsets()
        array_ran = np.append(array_ran, point)
        plot.set_offsets(array_ran)
        ax.set_ylim(array_ran[:, 1].min() -0.5, array_ran[:,1].max()+0.5)
        fig.canvas.draw()
#post processing
eq_check = [1 for i in range(no_of_iterations)]
check2 = 0
x1 = 0
x2 = 0
x3 = 0
for i in range(no_of_iterations):
    eq_check[i] = result_array[i][0]

minima_overall = min(eq_check)
for i in range(no_of_iterations):
    if minima_overall == eq_check[i]:
        check2 = i
        break

x1 = result_array[check2][1]
x2 = result_array[check2][2]
x3 = result_array[check2][3]
#print(result_array[check2])
print(result_array[check2][0],'', 'x1', x1, '','x2', x2, '','x3',x3)


q = equation_calc(x1, x2, x3) 

print(q)
