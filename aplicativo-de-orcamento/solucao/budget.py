class Category:
    
    """

        Ela deve ser capaz de instanciar objetos com base em diferentes categorias 
        de orçamento, como alimentos (food), vestuário (clothing) e entretenimento 
        (entertainment). Quando os objetos são criados, eles são passados com o 
        nome da categoria. 

    """

    def __init__(self, category_name) -> None:
        self.ledger = []
        self.category_name = category_name
    
    def check_funds(self, value):
        
        """

            Checa se a categoria tem fundos suficientes para fazer uma retirada
            ou uma transferencia.

            Retorna True se houver fundos, caso contrário, retorna False

        """

        funds = sum([item["amount"] for item in self.ledger])

        if funds - value < 0:
            return False
        
        return True

    def deposit(self, amount, description=""):
        """

            O método acrescenta um objeto à lista ledger na forma de 
            {"amount": amount, "description": description}.

        """
        self.ledger.append(
            {
                "amount": amount, 
                "description": description
            }
        )
    
    def withdraw(self, amount, description=""):
        """

            Semelhante ao método deposit, mas a quantia passada deve ser 
            armazenada no ledger como um número negativo. Se não houver 
            fundos suficientes, nada deve ser adicionado ao ledger.

            Este método deve retornar True se a retirada acontecer e, 
            caso contrário, False.
        """

        if not self.check_funds(amount):
            return False

        self.ledger.append(
            {
                "amount": (-1)*amount, 
                "description": description
            }
        )

        return True
        
    def get_balance(self):
        """
            Retorna o saldo atual da categoria de orçamento com base nos 
            depósitos e retiradas que ocorreram.

        """
        balance = sum([item["amount"] for item in self.ledger])
        return balance
    
    def transfer(self, value, category):
        """
        
            Um método transfer, que aceita um valor e outra categoria de orçamento 
            como argumentos.

            O método deverá adicionar uma retirada com o valor e a descrição 
            "Transfer to [categoria de destino no orçamento]". O método deve, 
            então, adicionar um depósito à outra categoria do orçamento, com o 
            valor e a descrição "Transfer from [categoria de origem no orçamento]".

            Se não houver fundos suficientes, nada deve ser adicionado ao ledger. 
            
            Este método deve retornar True se a transferência acontecer e, 
            caso contrário, False.

        """

        if not self.check_funds(value):
            return False

        self.withdraw(value, f"Transfer to {category.category_name}")
        category.deposit(value, f"Transfer from {self.category_name}")
        return True

    def __str__(self) -> str:
        title = f"{self.category_name:*^30}\n"
        content = f""
        sum = 0
        for item in self.ledger:
            sum += item['amount']
            description = item['description'] if len(item['description']) < 23 else item['description'][:23]
            curr_line = f"{description:23s}{float(item['amount']):>7.2f}\n"
            content += curr_line
        total = f"Total: {sum:.2f}"
        return title + content + total


def create_spend_chart(categories):
    """
        Recebe uma lista de categorias como um argumento. 
        Retorna uma string, que é um gráfico de barras.
    """
    title = "Percentage spent by category\n"
    category_names = [category.category_name for category in categories]
    len_bigger = len(category_names[0])
    line = " "*4 + "---"*len(category_names) + "-\n"
    graph = ""
    percents = []

    # Calculo das porcentagens
    total_spending = 0
    spending_per_category = []
    for category in categories:
        spending = 0 # somatorio de gastos da categoria
        for value in category.ledger:
            if value['amount'] < 0: # é gasto?
                spending += value['amount']
        total_spending += spending
        spending_per_category.append(spending)

    for value in spending_per_category:
        percent = value/total_spending
        percents.append(percent*100)

    # formatando o gráfico
    for curr_percent in range(100, -10, -10):
        label = f"{curr_percent:3d}|"
        for percent in percents:
            if percent >= curr_percent:
                label += " o "
            else:
                label += " "*3
        graph += label + " \n"

    # Achar a categoria com maior tamanho
    for category in category_names:
        if len(category) > len_bigger:
            len_bigger = len(category) 
    # label-x, category names
    label_x = ""
    for i in range(len_bigger):
        label = " "*4
        for category in category_names:
            try:
                label += f" {category[i]} "
            except IndexError:
                label += " "*3 # três espaços
        # atualiza o estado de label_x
        if i < len_bigger-1:
            label_x += label + " \n"
        else:
            label_x += label + " "

    return title + graph + line + label_x

# testes
if __name__ == "__main__":

    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")

    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")

    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)

    print(
        create_spend_chart(
            [
                business,
                food,
                entertainment,
            ]
        )
    )
    atual = create_spend_chart(
                [
                    business,
                    food,
                    entertainment,
                ]
            )
    expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    print(expected)
    print(len(atual))
    print(len(expected))
    print(len(expected) - len(atual))