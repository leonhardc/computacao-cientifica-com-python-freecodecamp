# **Calculadora de área de um poligono**

Este projeto é um exemplo simples do uso de programação orientada a objetos e herança em python. Aqui, trabalhamos com duas classes, uma classe Rectangle (Retangulo) e uma classe Square (quadrado). 

Este é um exemplo interessante para trabalharmos com heranção, pois, pela geometria relacionada, temos que todo quadrado é um retangulo, mas nem todo retangulo é um quadrado. Fazendo assim sentido que todo quadrado herde certas propriedades de um retangulo. E é exatamente isso que eu fiz, uma implementação onde a classe Square herda propriedades da classe Rectangle tornando mais fácil e rápida a implementação desse problema. 

Pois bem, pordemos usar a implementação dessas duas classes fazendo a importação abaixo:

```python

    from shape_calculator import Rectangle, Square

```

Depois da importação acima podemos instanciar nossos objetos já definindo a altura e a largura, para o caso do retangulo, e definindo o tamanho do lado, para o caso do quadrado.

```python

    rect = Rectangle(width=5, height=7)
    # rect = Rectangle(5, 7) também é válido
    sqr = Square(side=10)
    # sqr = Square(10) também é válido

```

Abaixo são exemplificados as chamadas de cada método e como deve ser o retorno de cada um para os objetos instanciados acima.

Para o objeto Rectangle, temos:

```python

    # Os métodos getters
    rect.get_area() # 35
    rect.get_perimeter() # 24
    rect.get_diagonal() # ~ 8.60
    rect.get_picture() 
    """
        *****
        *****
        *****
        *****
        *****
        *****
        *****
        *****

    """

    rect.get_amount_inside() # retorna quantas vezes uma outra figura cabe dentro
                             # de rect

    # Métodos setters

    rect.set_width(10) # seta a largura para 10
    rect.set_height(4) # seta a altura para 4


```

A classe Square, por ser filha de Rectangle, herda todos os métodos da classe pai. Entretanto, métodos como set_width e set_heigth tiveram que ser reescritos para se encaixar na realidade dos objetos quadrados.

Abaixo, temos alguns exemplos de uso do dos objetos do tipo Square

```python

    # metodos getter herdados de Rectangle
    sqr.get_area() # 100
    sqr.get_perimeter() # 40
    sqr.get_diagonal() # ~14.14
    sqr.get_picture()

    """

        **********
        **********
        **********
        **********
        **********
        **********
        **********
        **********
        **********
        **********
        **********

    """

    # métodos setters
    sqr.set_side(7)  
    sqr.set_width(7)
    sqr.set_heigth(7)
    
    # Em suma, seja qual seja os valores passados, os métodos acima fazem a mesma coisa, setam o valor dos dois lados do quadrado como 7

    rect.get_amount_inside() # também é um método herdado e faz a mesma coisa do exemplo anterior

```

Cada objeto tem uma representação definida com o método '__srt__()', então, podemos mostrar os objetos como abaixo

```python

    print(rect) # mostra: Rectangle(width=5, heigth=7)
    print(sqr) # mostra: Square(side=10)

```

## **O código**

Bem, qualquer parte do código é facilmente compreensível e foi devidamente comentada. A lógica por trás se mantem nos principios da matemática e no calculo de propriedades de poligonos. Então, se quiser conferir a implementação, é só dar uma olhada [aqui](./shape_calculator.py).


