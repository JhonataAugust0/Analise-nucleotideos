cont_bac = dict()
cont_human = dict()
lista_bac = list()
lista_human = list()

entrada_bac = open("bacteria.fasta").read()
saida_bac = open("bacteria.html","w")
entrada_human = open("human.fasta").read()
saida_human = open("human.html","w")
entrada_bac = entrada_bac.replace("\n","")
entrada_human = entrada_human.replace("\n","")
        
        
def formacao_nucleotideos(codificacao):
    """
        Essa função realiza as operações 
        de codificação e atribuição dos 
        pares de nucleotídeos existentes 
        no DNA humano e bacterial para 
        dicionários, que serão de suma 
        importância para a geração das 
        páginas HTML.    
    """
    
    for i in codificacao:
        for j in codificacao:
            cont_bac[i+j] = 0
            cont_human[i+j] = 0
    #Ciclos de repetição que contam a quantia de pares de nucleotídeos nos DNA's.
    
    for a in range(len(entrada_bac)-1):
        cont_bac[entrada_bac[a]+entrada_bac[a+1]] += 1

    for b in range(len(entrada_human )-1):
        cont_human[entrada_human [b]+entrada_human[b+1]] += 1
    #Ciclos de repetição que atribuem os pares ao dicionário
    return cont_bac, cont_human    
    

def formacao_html():
    """
        Essa função realiza as operações que 
        constroem as páginas em html que permitem 
        a visualização da representação dos nucle-
        otídeos do DNA humano e bacterial.
    """
    i = 1
    for a in cont_bac:
        transparencia_bac = cont_bac[a]/max(cont_bac.values())
        saida_bac.write("<div style='width:100px; border:1px solid #111; color:#fff; heigth:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia_bac)+"')>"+a+"</div>")
        if i % 4 == 0:
            saida_bac.write("<div style='clear:both'></div>")
        i+=1
    
    for b in cont_human:
        transparencia_human = cont_human[b]/max(cont_human.values())
        saida_human.write("<div style='width:100px; border:1px solid #111; color:#fff; heigth:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia_human)+"')>"+b+"</div>")
        if i % 4 == 0:
            saida_human.write("<div style='clear:both'></div>")
        i+=1
        
    lista_bac.append(cont_bac.values())  
    lista_human.append(cont_human.values())   
        
    return lista_bac, lista_human
    saida_bac.close()    
    saida_human.close()