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

        if funds + ((-1)*value) <= 0:
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
        for item in self.ledger:
            description = item['description'] if len(item['description']) < 23 else item['description'][:22]
            curr_line = f"{description:23s}{float(item['amount']):>7.2f}\n"
            content += curr_line
        return title + content


def create_spend_chart(categories):
    """
        Recebe uma lista de categorias como um argumento. 
        Retorna uma string, que é um gráfico de barras.
    """
    pass