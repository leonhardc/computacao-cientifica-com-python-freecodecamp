import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.arguments = kwargs
    self.contents = []
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)

  def draw(self, num_of_balls):

    if num_of_balls >= len(self.contents):
      # Se o numero de retiradas exceder a quantidades de bolas disponiveis
      return self.contents

    list_of_choices = copy.deepcopy(self.contents)
    choices = []
    for _ in range(num_of_balls):
      choice = random.choice(list_of_choices)
      list_of_choices = list_of_choices.remove(choice)
      choices.append(choice)
    return choices

  def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


if __name__ == "__main__":
  pass
