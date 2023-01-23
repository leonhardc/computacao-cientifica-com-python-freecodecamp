# **Calculadora de probabilidade**

Como foi proposto na descrição do projeto, foi implementado um meio de calcular a probabilidade aproximada de se retirar um conjuntos de bolas de determinadas cores de um chapeu (classe Hat). 

O módulo [prob_calculator.py](./prob_calculator.py) é o módulo que contem a implementação da solução deste projeto. Ele conta com as seguintes classes e métodos:

* Classe **Hat**: Esta é a classe que abstrai o nosso "chapeu" onde ficarão as bolas das cores determinadas na sua declaração. É daqui de onde serão retirados os conjuntos de bolas que serão usadas para os calculos das probabilidades. 
  * **draw(self, num_of_balls)**: um método da classe ball. É aqui onde pode ser retirado um conjunto de n (num_of_balls) bolas para nossa experiencia. Se o numero de bolas solicitada na chamada da função for maior que o numero de bolas disponiveis para o experimento, este método retorna o conjunto disponivel no objeto Hat.
* O método **experiment()**: é aqui onde será calculado a probabilidade de fato. O método conta com os seguintes atributos:
  * **hat**: é o objeto do tipo Hat que será usado para fazer as experimentações.
  * **expected_balls**: Um objeto na forma {red: 2, blue:4, green: 6, ...} que representa o conjunto experado de bolas que deve ser retirado do chapeu. É a partir dele que calcularemos quantas vezes cada retorno do método draw() pode ser contabilizado e usado para o calculo da nossa probabilidade.
  * **num_balls_drawn**: Quantidade de bolas que deve ser retirada em cada experimento.
  * **num_experiments**: Quantidade de experimentos que será feito ao final da nossa chamada.
* Métodos auxiliares:
  * **list_to_dict(list)**: Recebe uma lista que representa as bolas que estão contidas no chapeu e retorna um dicionário na forma {color1: amount1, color2: amount2,  ...} onde color a cor das bolas presentes na lista e amount é a quantidade de cada bola dessa cor.
  * **is_sub_dict(first_dict, sec_dict)**: Analisa se o primeiro dicionário (conjunto de bolas) está contigo no segundo dicionário.


# **O Código**

O modulo que está sendo apresentado tem uma implementação breve e de fácil compreensão. Então, para mais detalhes vide o [código](./prob_calculator.py)