
import pandas as pd

processos_p4 = {
    'processo': ['p1', 'p2', 'p3', 'p4']
}

df4 = pd.DataFrame(data=processos_p4)
df4.index = [1,2,3,4]
df4['processou'] = [0,0,0,0]


processos_p2 = {
    'processo': ['p5', 'p6', 'p7']
}

df2 = pd.DataFrame(data=processos_p2)
df2.index = [1,2,3]
df2['processou'] = [0,0,0]
    
processos_p1 = {
    'processo': ['p9', 'p10']
}

df1 = pd.DataFrame(data=processos_p1)
df1.index = [1,2]
df1['processou'] = [0,0]


def escalona_PRIORD():
    
    global df4
    global df2
    global df1
    
    print("Fila Prioridade 4")
    print(df4)
    print("**********")
    
    print("Fila Prioridade 2")
    print(df2)
    print("**********")

    print("Fila Prioridade 1")
    print(df1)
    print("**********")
    
    
    print('na prioridade dinâmica, a prioridade será rebaixada temporariamente para evitar inanição. ')   
    print('para reduzir a prioridade, vamos usar o parâmetro processou')
        
    ciclo = 1
    
    p4_fila = 1
    p4_etapa = 1
    
    
    p2_fila = 1
    p2_etapa = 1
    
    p1_fila = 1
    p1_etapa = 1
    

    while ciclo <= 4:
        print('Ciclo: ',ciclo)
        x4 = 1
        while x4 <= 4:     
            
            a = df4.loc[p4_fila].at['processo']  
            prc = df4.loc[p4_fila].at['processou'] 

            print("****Executando Processo ", a,' de prioridade 4 no quantum  ',x4)                                
            
            novaetapa = prc + 1
            df4.at[p4_fila, 'processou'] = novaetapa    
            
            if novaetapa >= 3:
                p4_fila = p4_fila + 1
                p4_etapa = 1
                
            x4 = x4 + 1
        print(df4)

     
        x2 = 1
        while x2 <= 2:        
            a2 = df2.loc[p2_fila].at['processo'] 
            prc2 = df2.loc[p2_fila].at['processou'] 
            print("****Executando Processo ", a2,' de prioridade 2 no quantum  ',x2)          
            novaetapa2 = prc2 + 1
            df2.at[p2_fila, 'processou'] = novaetapa2    
            
             
            if novaetapa2 >= 3:
                p2_fila = p2_fila + 1
                p2_etapa = 1
            x2 = x2+1 
        print(df2)

        
        x1 = 1
        while x1 <= 1:        
            a1 = df1.loc[p1_fila].at['processo'] 
            prc1 = df1.loc[p1_fila].at['processou'] 
            print("****Executando Processo ", a1,' de prioridade 2 no quantum  ',x1)            
            novaetapa1 = prc1 + 1
            df1.at[p1_fila, 'processou'] = novaetapa          
            
            if novaetapa1 >= 3:                
                p1_fila = p1_fila + 1
                p1_etapa = 1
            
            x1 = x1+1
        print(df1)
        
        ciclo = ciclo + 1
        print("****************************************************")


escalona_PRIORD()
