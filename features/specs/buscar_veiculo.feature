# language: pt
Funcionalidade: Buscar Carro para Comprar

 Cenário: Buscar Veículo
   Dado que eu precise buscar um veículo
   | Fabricante | Modelo | Ano  | Estado    | Cidade    |
   | Honda      | Civic  | 2014 | São Paulo | São Paulo |
   Quando realizo a busca de carros usados
   Então devo ver a lista de anúncios