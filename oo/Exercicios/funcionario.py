class funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def nome(self):
        return self._nome

    def salario(self):
        return self._salario

    def __str__(self):
        return f"{self._nome}, seu salário total é {self._salario}"

    def aumentar_salario(self, aumento):
        self._salario = self._salario + aumento

f1 = funcionario("Mateus", 1900.0)
print(f1)
f1.aumentar_salario(2300.0)
print(f"AUMENTO!! {f1}")
