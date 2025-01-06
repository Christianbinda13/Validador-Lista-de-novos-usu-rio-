class UsuarioTelefone:
    def __init__(self, nome, numero_telefone, plano):
        self._nome = nome  # Atributo privado para o nome
        self._numero_telefone = numero_telefone  # Atributo privado para o número de telefone
        self._plano = plano  # Atributo privado para o plano
        self._validar_plano()  # Valida se o plano informado é um dos planos válidos

    def _validar_plano(self):
        planos_validos = ["Plano Essencial Fibra", "Plano Prata Fibra", "Plano Premium Fibra"]
        if self._plano not in planos_validos:
            raise ValueError("Plano inválido. Os planos válidos são: 'Plano Essencial Fibra', 'Plano Prata Fibra', 'Plano Premium Fibra'.")

    def __str__(self):
        # Método especial para gerar a mensagem de saída
        return f"Usuário {self._nome} criado com sucesso."

    # Métodos para acessar os atributos (encapsulamento)
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def numero_telefone(self):
        return self._numero_telefone

    @numero_telefone.setter
    def numero_telefone(self, valor):
        self._numero_telefone = valor

    @property
    def plano(self):
        return self._plano

    @plano.setter
    def plano(self, valor):
        self._plano = valor
        self._validar_plano()  # Revalidando o plano após alteração

# Função para entrada e saída
def main():
    # Recebendo dados de entrada
    nome = input().strip()
    numero_telefone = input().strip()
    plano = input().strip()

    # Criando o usuário
    try:
        usuario = UsuarioTelefone(nome, numero_telefone, plano)
        print(usuario)  # Imprimindo a mensagem de sucesso
    except ValueError as e:
        print(e)  # Caso o plano seja inválido

# Chamada da função principal
if __name__ == "__main__":
    main()
