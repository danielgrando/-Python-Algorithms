#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

data = {
    'processo': ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10'],
    'prioridade': [3,2,5,8,3,1,1,4,6,1],
    'tempo': [300, 250, 100, 200, 250, 150, 100, 200, 300, 200]
}

df = pd.DataFrame(data=data)
print("Ordenação padrão dos processos antes da execução",df)
df['processou'] = [0,0,0,0,0,0,0,0,0,0]

df = df.sort_values(by=['tempo','prioridade'], ascending=False)
df.index = [1,2,3,4,5,6,7,8,9,10]

# In[6]:


def escalonamento():
    global df
    
    print('Nesse exercício a cada quantum a atenção do processador será atribuída ao primeira do fila.')
    print('A cada time sharing a fila será atualizada dando a segunda chance ao processo.')
    print('Cada processo executará 3 quantuns')
        
    print(df)
    
 
    for chance in range(1,2):
        for x in range(1,11):                    
            a = df.loc[x].at['processo']
            print("****Executando Processo ", a,', na chance número ',chance)               
            df.at[x, 'processou'] = chance
            print(df)


# In[7]:


escalonamento()


# In[ ]:
