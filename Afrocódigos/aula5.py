from operacoes import OperacoesMatematicas

instancia = OperacoesMatematicas()

primeiro_numero = int(input("Informe o primeiro número: "))
segundo_numero = int(input("Informe o segundo número: "))

print("Adição: ", instancia.soma(primeiro_numero, segundo_numero))
print("Subtração: ", instancia.subtracao(primeiro_numero, segundo_numero))
print("Multiplicação: ", instancia.multiplicacao(primeiro_numero, segundo_numero))
print("Divisão: ", instancia.divisao(primeiro_numero, segundo_numero))