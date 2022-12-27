def add_time(start, duration, week_day=None):

  days_week = [
    "sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
    "saturday"
  ]
  
  days_count = 0  # Contagem de dias que se passaram depois de period ser adicionado

  hr, period = start.split(" ")
  hr_start, mnt_start = hr.split(":")
  hr_duration, mnt_duration = duration.split(":")

  # Casting dos valores para que possamos operar sobre eles
  hr_start = int(hr_start)
  mnt_start = int(mnt_start)
  hr_duration = int(hr_duration)
  mnt_duration = int(mnt_duration)

  # Convertendo hora de inicio para o formato de 24hrs
  if period == "PM":
    hr_start += 12

  # Total de horas percorridos
  hr_count = hr_start + hr_duration
  
  # Total de minutos percorridos
  mnt_count = mnt_start + mnt_duration

  # Acrescenta mais uma hora se a contagem de minutos for maior que 60
  if mnt_count >= 60:
    mnt_count -= 60
    hr_count += 1

  # Caso 1: Quando a contagem de dias é zero e ainda é manhã
  if hr_count < 12:
    hr_final = hr_count
    period_final = "AM"
    # Se for passado o dia da semana como parametro opcional
    if week_day:
      return f"{hr_final}:{mnt_count:02} {period_final}, {week_day}"
    return f"{hr_final}:{mnt_count:02} {period_final}"

  # Caso 2: Quando a contagem de dias é zero mas já é tarde ou noite
  if hr_count >= 12 and hr_count < 24:
    hr_final = hr_count if hr_count == 12 else (hr_count - 12)
    period_final = "PM"
    # Se for passado o dia da semana como parametro opcional
    if week_day:
      return f"{hr_final}:{mnt_count:02} {period_final}, {week_day}"
    return f"{hr_final}:{mnt_count:02} {period_final}"

  # Se não houve retorno até agora é porque hr_count é maior que ou igual a 24,
  # ou seja, houve um ou mais saltos de um dia para o outro.
  days_count = int(hr_count / 24)

  # Caso 3: Houve um salto de um dia para o outro
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
  
  # Caso 4: Houve mais de um salto de um dia para o outro
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


# Testes
if __name__ == "__main__":
  print(
    add_time("3:30 PM", "2:12"), 
    "5:42 PM"
  )

  print(
    add_time("11:55 AM", "3:12"), 
    "3:07 PM"
    )

  print(
    add_time("9:15 PM", "5:30"), 
    "2:45 AM (next day)"
    )

  print(
    add_time("11:40 AM", "0:25"), 
    "12:05 PM"
    )

  print(
    add_time("2:59 AM", "24:00"), 
    "2:59 AM (next day)"
    )

  print(
    add_time("11:59 PM", "24:05"), 
    "12:04 AM (2 days later)"
    )

  print(
    add_time("8:16 PM", "466:02"), 
    "6:18 AM (20 days later)"
    )

  print(
    add_time("5:01 AM", "0:00"), 
    "5:01 AM"
    )

  print(
    add_time("3:30 PM", "2:12", "Monday"), 
    "5:42 PM, Monday"
    )
  print(
    add_time("2:59 AM", "24:00", "saturDay"), 
    "2:59 AM, Sunday (next day)")

  print(
    add_time("11:59 PM", "24:05", "Wednesday"),
    "12:04 AM, Friday (2 days later)"
    )

  print(
    add_time("8:16 PM", "466:02", "tuesday"),
    "6:18 AM, Monday (20 days later)"
    )
