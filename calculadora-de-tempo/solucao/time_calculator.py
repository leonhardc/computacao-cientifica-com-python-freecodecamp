def add_time(start, duration):
  days_count = 0
  hr, period = start.split(" ")
  hr_start, mnt_start = hr.split(":")
  hr_duration, mnt_duration = duration.split(":")

  # Operações com horas e minutos inteiros
  hr_end = int(hr_start) + int(hr_duration)  # hora final
  mnt_end = int(mnt_start) + int(mnt_duration)  # minutos final

  # Verificar de a soma dos minutos passou de 60
  if mnt_end >= 60:
    mnt_end = mnt_end - 60
    hr_end = hr_end + 1

  # Verificar se a soma das horas está entre 12 e 13hrs
  if hr_end == 12:
    period = "PM"
    time = hr_end + ":" + mnt_end + " " + period
    return time

  # Verificar se a soma das horas está entre 13 e 23hrs
  if hr_end > 12 and hr_end < 23:
    period = "PM"
    time = hr_end + ":" + mnt_end + " " + period
    return time
