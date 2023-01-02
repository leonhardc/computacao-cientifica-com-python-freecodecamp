# **Solução do problema do formatador aritmético**

Assim como fiz para descrever o passo a passo do [problema proposto](./../README.md), também me dediquei a descrever as partes da codificação que eu julgo mais importantes para a solução deste problema.

No arquivo [arithmetic_arranger.py](./arithmetic_arranger.py) temos a codificação de fato da solução do problema proposto neste projeto. Em resumo, **arithmetic_arranger.py** contem um unico método com a assinatura mostrada abaixo:

```python  
    
    arithmetic_arranger(problems, resolve=False)

```
O método **arithmetic_arranger(...)** recebe dois parametros, o primeiro **problems** se trata de uma lista de problemas matemáticos, escritos de maneira linear, que devem ser posteriormente escritos numa forma mais amigavel aos olhos humanos, assim como é ensinado na escola.

Por exemplo, a chamada da função abaixo:

```python

    arithmetic_arranger(['3801 - 2', '123 + 49'])

```

deve retornar a string que conhenha a seguinte representação, seguindo os padrões descritos anteriormente na problemática:

```

    3801      123
  -    2    +  49
  ------    -----

```

**resolve** é um paramtro opcional, que, quando especificado (True) informa a função que deve retornar a representação dos problemas mateméticos mais sua solução. Assim, a chamada da função:

```python

    arithmetic_arranger(['3801 - 2', '123 + 49'], resolve=True)

```

deve retornar 

```

    3801      123
  -    2    +  49
  ------    -----
    3799      172

```

## **O código**

A solução começa com quatro declarações importantes:

```python

    line_one = []
    line_two = []
    line_three = []
    line_four = []

```

As quatro variaveis mostradas acima representam as linhas que preencherão nossa solução, **line_one** é lista  onde ficará o primeiro operando de cada operação passada como parametro, **line_two** é onde ficam o operador e o segundo operando de cada operação, **line_three** é onde estão as divisões entre operação e solução e **line_four** é onde ficam as soluções de cada operação, caso o parametro **resolve** seja especificado.

```python

    if len(problems) > 5:
        return "Error: Too many problems."

```

O trecho acima trata de uma verificação simples, para garantir que a função não receba mais do que cinco problemas para serem formatados.

No trecho de código abaixo é onde a mágica realmente acontece

```python

    for problem in problems:
        problem = problem.split(" ")
        frst_operator, operation, sec_operator = problem
        # Se os operadores forem diferentes de adição ou subtração,
        # retornar:
        # Error: Operator must be '+' or '-'.
        if operation not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        # Qualquer operando deve conter apenas algarismos, se não o
        # seguinte erro deve ser retornado
        # Error: Numbers must only contain digits.
        for digit in frst_operator + sec_operator:
            if not digit.isdigit():
                return "Error: Numbers must only contain digits."
        # Cada operando deve conter no máximo quatro digitos, caso
        # contrário, o erro abaixo deve ser retornado
        # Error: Numbers cannot be more than four digits.
        if len(frst_operator) > 4 or len(sec_operator) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Caso passe em todos os testes
        space_block = 0
        if len(frst_operator) >= len(sec_operator):
        space_block = len(frst_operator) + 2
        else:
        space_block = len(sec_operator) + 2

        line_one.append(" " * (space_block - len(frst_operator)) + frst_operator)
        line_two.append(operation + " " * (space_block - len(sec_operator) - 1) +
                        sec_operator)
        line_three.append("-" * space_block)

        if resolve:
        if operation == "+":
            soluction = int(frst_operator) + int(sec_operator)
            line_four.append(" " * (space_block - len(str(soluction))) +
                            str(soluction))
        else:
            soluction = int(frst_operator) - int(sec_operator)
            line_four.append(" " * (space_block - len(str(soluction))) +
                            str(soluction))


```

Para evitar redundancia, vou explicar somente o que esse trecho de código faz. Lembra da forma do nosso parametro **problems**? O codigo primeiro divide cada problema em tres variaveis referentes ao primeiro operando, ao operador e ao segundo operando, respectivamente. A partir daí ele vai acrescentar cada variável em seu devido lugar e acrescentar um espaço necessário em cada string, para que depois possamos concatená-las da maneira correta. Por ultimo, cerificamos se o parametro resolve foi especificado, se sim, calculamos a solução do problema e acresentamos o resultado na variável referente a ultima linha da nossa representação.

```python

    line_one = "    ".join(line_one)
    line_two = "    ".join(line_two)
    line_three = "    ".join(line_three)
    line_four = "    ".join(line_four)

    if resolve:
        return line_one + "\n" + line_two + "\n" + line_three + "\n" + line_four
    return line_one + "\n" + line_two + "\n" + line_three

```

Por ultimo, juntamos convertemos cada lista em uma string que representa parte da nossa solução e fazemos o retorno adequado de acordo com os parametros passados.