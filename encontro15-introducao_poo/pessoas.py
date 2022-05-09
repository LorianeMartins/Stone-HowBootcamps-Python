class Funcionario: 

    aumento_percentual: float = 0.1

    def __init__(self, nome: str, sobrenome: str, salario_inicial: int):
        self.nome = nome
        self.sobrenome = sobrenome 
        self.salario_inicial = salario_inicial
        self.email = f"{self.nome.lower()}.{self.sobrenome.lower().split()[-1]}"

    def dar_aumento(self) -> None: 
        if hasattr(self, "salario_atual"):
            self.salario_atual = self.salario_atual * (1 + Funcionario.aumento_percentual)
        else: 
            self.salario_atual = self._salario_inicial * (1 + Funcionario.aumento_percentual)