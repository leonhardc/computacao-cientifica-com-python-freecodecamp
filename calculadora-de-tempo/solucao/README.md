# **O problema da calculadora de tempo**

O modulo [time_calculator.py](./time_calculator.py) contem uma unica função chamada **add_time(...)** com a assinatura

```python

    add_time(start, duration, week_day=None)

```
a função add_time(...) contem três parametros:

* **start**: Uma string no formato 'hh:mm AM' ou 'hh:mm PM' que trata basicamente da hora e do minuto onde será iniciada a contagem. 
* **duration**: Uma string tambem no formato 'hh:mm' que trata da quantidade de tempo que será somada a hora inicial passada como primeiro parametro.
* **week_day**(opcional): Uma string que representa o dia da semana onde será iniciada a contagem. Se especificado, o retorno da função deverá especificar também, que dia da semana terminou a contagem.

A chamada da função abaixo

```python

    add_time("11:59 PM", "24:05", "Wednesday")

```

deve retornar a string 

```python

    "12:04 AM, Friday (2 days later)"

```

## **O código**

Começamos a codificação declarando algumas variáveis que nos serão uteis posteriormente para nossos calculos

```python


  days_week = [
    "sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
    "saturday"
  ]

  # Contagem de dias que se passaram depois de period ser adicionado
  days_count = 0  

  hr, period = start.split(" ")
  hr_start, mnt_start = hr.split(":")
  hr_duration, mnt_duration = duration.split(":")

  # Casting dos valores para que possamos operar sobre eles
  hr_start = int(hr_start)
  mnt_start = int(mnt_start)
  hr_duration = int(hr_duration)
  mnt_duration = int(mnt_duration)

```

A solução proposta trata quatro possibilidades:

1. Quando não houve salto de um dia para o outro e a contagem de horas ainda é menor que 12
2. Quando não houve salto de um dia para o outro e a contagem de horas é maior ou igual a 12 e menor que 24(por isso não houve salto de um dia para o outro)
3. Quando houve somente um salto de um dia para o outro
4. Quando houve mais de um salto de um dia para o outro

Os quatro casos acima são codificados nos seguintes trechos de código:

### Caso 1:

Retorna a contagem de horas, de minutos, o periodo, que no caso é "AM" (manhã) e o dia da semana, se for especificado na chamada da função.

```python

    if hr_count < 12:
        hr_final = hr_count
        period_final = "AM"
        # Se for passado o dia da semana como parametro opcional
        if week_day:
            return f"{hr_final}:{mnt_count:02} {period_final}, {week_day}"
        return f"{hr_final}:{mnt_count:02} {period_final}"

```
### Caso 2:

Retorna a hora final (já convertida para representação de 12hrs), os minutos finais, o periodo que no caso é "PM" e o dia da semana, se for especificado.

```python

    # Caso 2: Quando a contagem de dias é zero mas já é tarde ou noite
    if hr_count >= 12 and hr_count < 24:
        hr_final = hr_count if hr_count == 12 else (hr_count - 12)
        period_final = "PM"
        # Se for passado o dia da semana como parametro opcional
        if week_day:
            return f"{hr_final}:{mnt_count:02} {period_final}, {week_day}"
        return f"{hr_final}:{mnt_count:02} {period_final}"

```

### Caso 3:

Retorna devidamente formatada a hora final, já no formato de 12hrs, o minuto final, o periodo do dia, o dia da semana, se for especificado na chamada da função, e a string "(next day)" representando que se passaram um dia depois após da contagem de tempo.

```python

    if days_count == 1:
        hr_final = hr_count % 24
        period_final = "AM" if hr_final < 12 else "PM"
        hr_final = hr_final if period == "AM" else hr_final - 12 if hr_final > 12 else hr_final
        # Se for passado o dia da semana como parametro opcional
        if week_day:
            index_curr_day = days_week.index(week_day.lower())
            # Se week_day for o ultimo dia da semana
            if index_curr_day == len(days_week) - 1:
            index_next_day = 0
            # Se week_day for um dia de meio de semana
            else:
            index_next_day = index_curr_day + 1
            next_day = days_week[index_next_day]
            return f"{hr_final}:{mnt_count:02} {period_final}, {next_day.title()} (next day)"
        return f"{hr_final}:{mnt_count:02} {period_final} (next day)"

```

### Caso 4:

Retorna devidamente formatada a hora final, já no formato de 12hrs, o minuto final, o periodo do dia, o dia da semana, se for especificado na chamada da função, e a string "(n days later)" com 'n' sendo o numero de dias que se passaram depois da contagem de tempo.

```python

    else:
        hr_final = hr_count % 24
        period_final = "AM" if hr_final < 12 else "PM"
        hr_final = hr_final if period == "AM" else hr_final - 12 if hr_final > 12 else hr_final
        hr_final = hr_final + 12 if (hr_final == 0
                                        and period_final == "AM") else hr_final
        # Se for passado o dia da semana como parametro opcional
        if week_day:
            index_curr_day = days_week.index(week_day.lower())
            count_week_day = days_count % 7
            # Se week_day for o ultimo dia da semana
            if index_curr_day == len(days_week) - 1:
            index_next_day = count_week_day - 1
            # Se week_day for um dia de meio de semana
            else:
            index_next_day = index_curr_day + count_week_day
            if index_next_day > len(days_week) - 1:
                index_next_day -= 7
            next_day = days_week[index_next_day]
            return f"{hr_final}:{mnt_count:02} {period_final}, {next_day.title()} ({days_count} days later)"
        return f"{hr_final}:{mnt_count:02} {period_final} ({days_count} days later)"

```

Os casos acima mostram os casos que vi necessários para sobrir os possíveis fluxos do programa. Cada um tem suas particularidades que podem ser vistos com mais detalhes no [código](./time_calculator.py).





