'''#METODO APPEND QUE SIGNIFICA ADICIONAR
#AS LISTAS SÃO MUTÁVEIS,OU SEJA,PODEMOS ADIONAR ELEMNTOS COM METODO APPEND,NA TUPLA NÃO PODE
#QUANDO DA ESSE COMANDO,IRÁ ADICONAR SEMPRE NO FINAL DA LISTA'''
lanche=['pizza','pão','hamburguer','hot dog','sorvete','pamonha']
'''lanche.append('salada')
print(lanche)'''



'''O METODO APPEND IRÁ INSERIR SEMPRE NA ULTIMA POSIÇÃO,AGORA PRA VOCÊ ADICIONAR UM LANCHE,NA POSIÇÃO
#DESEJADAS IREMOS USAR O METODO INSERT.
lanche.insert(1,'esfiha')
# o numero 3 é a posição que você quer,0 é a pizza,1 é o pão,o 2 será o hamburguer e a esfiha sera 3,assim sucessivamente
print(lanche)'''


'''O METODO DEL IRÁ REMOVER ELEMENTOS
SÃO TRÊS FORMAS DE REMOVER
del lanche [3]# básico esse metodo,tenta eliminar na posição 3,que será hot dog.
print(lanche)
lanche.pop(3)#normalmente metodo pop elimina o ultimo elemento,mais você pode passar o parametro indicie que voce quer eliminar.
print(lanche)
lanche.remove('sorvete')#esse método ele elimina por centeudo,não por indice,vai idicar o valor.
print(lanche)
#o metodo REMOVE irá ser removido quando tiver na lista,então utilizamos 
if 'pizza' in lanche:
    lanche.remove('pizza') é uma maneira bem interessante e válido de utilizar esse metodo.
#EM TODOS ESSES CASOS IRÁ ELIMINAR.,todos foram testados e funciono perfeitamente.'''

lanche[2]='cardapio'
#se eu colocar o indice numero 6,ele da erro,portanto só vale o que esta nos indice,de 0 a 5 no exemplo do lanche
lanche.insert(4,'cama')
#pra inserir um item em alguma posição,devemos colocar Insert e nao append
#Metodo append é só pra adicionar um item no final.
lanche.sort()
#fiz o teste em palavras,eele retorno com ordem alfabetica,assim serve para números também
lanche.sort(reverse=True)
#ordem alfabetica de traz pra frente,funciono também.
if 'pizza' in lanche:#quando colocar string,deve-se sempre colocar entre aspas,senão da erro
    lanche.pop() #sempre em aspas
else:
    print('Não achei o desejado.')
print(lanche)





