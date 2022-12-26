def arithmetic_arranger(problems, resolve=False):
  line_one = []
  line_two = []
  line_three = []
  line_four = []

  # Situações de erro:
  # Se houverem mais do que cinco problemas, retornar:
  # Error: Too many problems.
  if len(problems) > 5:
    return "Error: Too many problems."

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

  line_one = "    ".join(line_one)
  line_two = "    ".join(line_two)
  line_three = "    ".join(line_three)
  line_four = "    ".join(line_four)
  if resolve:
    return line_one + "\n" + line_two + "\n" + line_three + "\n" + line_four
  return line_one + "\n" + line_two + "\n" + line_three
