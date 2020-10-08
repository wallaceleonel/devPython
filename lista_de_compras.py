frutas =['maça','banana','abacate','uva']
proteina =['frango','patinho moido','whey','whazymaze']
carbo =['arroz','feijao','legumes']
bebidas =['agua','sucao','laranja']

categorias =['fruta','proteina','carbo','bebidas']
compras =[frutas,proteina,carbo,bebidas]

for indice,categoria in enumerate(categorias):
    print('voce precisa comprar',len(compras[indice]), categoria+':')
    for compra in compras[indice]:
         print('-',compra)