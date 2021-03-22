class Pessoa:
    olhos = 2

    def __init__(self,*filhos,nome=None,idade=23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hi! {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 5

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
     pass

if __name__ == '__main__':
    julia = Pessoa(nome='Julia')
    leo = Pessoa(julia, nome='Leo')
    print(Pessoa.cumprimentar(julia))
    print(julia.cumprimentar())
    print(julia.nome)
    print(julia.idade)
    julia.olhos = 1
    print(julia.olhos)
    print(Pessoa.nome_e_atributos_de_classe(), julia.metodo_estatico())

    for filho in leo.filhos:
        print(filho.nome)

    julia.sobrenome = 'Santos'
    print(julia.__dict__)
    print(leo.__dict__)
    pessoa = Pessoa('Anonimo')
    # Pergunta se é uma instância
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))

