# **Aplicação de orçamento**

Neste projeto abordaremos uma implementação simples de uma aplicação de orçamento. No arquivo [budget.py](./budget.py) está a implementação da solução desse problema. Nele, temos os seguintes componentes fundamentais. 

1. A classe **Category** que é a abstração do que podemos entender como uma categoria de gastos que se possa ter (comida, roupas, entretenimento etc). Nela, estão contidos alguns métodos, como métodos de deposito, retirada e de transferencia, que serão úteis para implementarmos a nossa aplicação. 
2. Um método chamado **create_spend_chart()** que recebe uma lista de objetos do tipo **Category** e cria uma gráfico de barras, mostrando a porcentagem dos nossos gastos em cada categoria. 

## **O código**

Ao instanciar uma categoria devemos passar o nome da categoria que estamos instanciando. Assim como é feito abaixo:

```python

    food = Category("food")

```

O objeto instanciado logo acima terá a sua disposição os seguintes atributos.

* **category_name**: O nome da categoria, que é o nome que passamos ao instanciar um objeto.
* **ledger**: Uma lista de objetos na forma "{"amount": amount, "description": description}". A chave amount é o valor do deposito ou da retirada que se está fazendo em determinada categoria. A chave description é a descrição daquele deposito ou gasto em particular. 

Os dois atributos acima, especialmente o atributo **ledger** serão processados pelos seguintes métodos de classe:

* **.check_funds()**: Checa se temos fundos disponíveis na nossa categoria, para que possamos fazer uma transferencia ou uma retirada. Este método recebe como parametro um valor que será comparado com os o objeto ledger, para que se possa saber se temos fundos suficientes na categoria.
* **.deposit()**: Normalmente o primeiro método usado logo após o objeto ser instanciado. Este método recebe como parametro uma quantia que será depositada da nossa categoria. 
* **.withdraw()**: Este método pode ser considerado como uma retirada ou um gasto que tivemos com determinada categoria de gastos que temos disponíveis. Assim como o método deposit(), este método também recebe um valor, mas que será armazenado no objeto ledger como um numero negativo.
* **.get_balance()**: Este método não recebe parametros. get_balance() retorna o saldo atual com base em depositos e retiradas que ocorreram nesta categoria.
* **.transfer()**: Recebe como parametros um valor e uma outra categoria. Se for houverem fundos suficientes, faz a transferencia do valor para outra categoria passada como argumento.


## **O código**

Neste projeto eu me preocupei em comentar devidamente cada trecho e código e descrever o que cada trecho faz. Então, neste ponto, para evitar redundancia, prefiro deixar que você cheque a solução e entenda passo a passo a lógica por trás da codificação. O código é simples e de fácil compreenção.


