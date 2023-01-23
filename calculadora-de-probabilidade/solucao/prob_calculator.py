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

        choices = []

        for _ in range(num_of_balls):
            choice = random.choice(self.contents) # faz uma escolha aleatoria
            self.contents.remove(choice) # remove a escolha da lista
            choices.append(choice) # acrescenta a escolha na lista que será retornada

        return choices


def list_to_dict(list):
    my_dict = {}

    for key in set(list):
        value = list.count(key)
        my_dict[key] = value

    return my_dict

def is_sub_dict(first_dict, sec_dict):
    """
        Verifica se o primeiro conjunto de experimentos é subconjunto
        do segundo conjunto de experimentos
    """
    is_matching = True
    for key, value in first_dict.items():
        if not key in sec_dict:
            is_matching = False
            break
        else:
            if sec_dict[key] < value:
                is_matching = False
                break
    return is_matching

             


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    cont = 0

    # start experiments
    for _ in range(num_experiments):
        new_hat = Hat(**hat.arguments) 
        experiment = new_hat.draw(num_balls_drawn)
        # converter lista experiment para dicionario
        experiment = list_to_dict(experiment)
        # verificar se expected_balls está contido no experimento
        if is_sub_dict(expected_balls, experiment):
            cont += 1
    
    # retornar a probabilidade
    return (cont/num_experiments)




if __name__ == "__main__":
    hat = Hat(blue=3,red=2,green=6)
    probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
    print(probability)
