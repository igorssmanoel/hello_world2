values = input().split()
values = [float(x) for x in values]                                                                                                                                                                                   
values.sort(reverse=True)                             
A = values[0]                                                                                               
B = values[1]                                                                                               
C = values[2]                                                                                               
                                                                                          
if A >= B + C:                                                                                              
    print("NAO FORMA TRIANGULO")                                                                            
else:                                                                                                       
    if A**2 == B**2 + C**2:                                                                                 
        print("TRIANGULO RETANGULO")                                                                        
    if A**2 > B**2 + C**2:                                                                                  
        print("TRIANGULO OBTUSANGULO")                                                                      
    if A**2 < B**2 + C**2:                                                                                  
        print("TRIANGULO ACUTANGULO")                                                                       
                                                                                                            
    if A == B == C:                                                                                         
        print("TRIANGULO EQUILATERO")                                                                       
    elif A == B or B == C or A == C:                                                                        
        print("TRIANGULO ISOSCELES")  