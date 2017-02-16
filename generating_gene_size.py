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
         


 
