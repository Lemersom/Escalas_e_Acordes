def escalaMaior(nota):
    global e_maior
    e_maior = [campo[campo.index(nota)], campo[campo.index(nota) + 2],
               campo[campo.index(nota) + 4], campo[campo.index(nota) + 5],
               campo[campo.index(nota) + 7], campo[campo.index(nota) + 9],
               campo[campo.index(nota) + 11]]
    # Montar Escalas Maiores:
    # Sequência -> T T S T T T S           T = Tom ("pula uma nota")
    # Exemplo ->  C D E F G A B C          S = SemiTom ("proxima nota")
    


def escalaMenor(nota):
    global e_menor
    e_menor = [campo[campo.index(nota)], campo[campo.index(nota) + 2],
               campo[campo.index(nota) + 3], campo[campo.index(nota) + 5],
               campo[campo.index(nota) + 7], campo[campo.index(nota) + 8],
               campo[campo.index(nota) + 10]]
    # Montar Escalas Menores:
    # Sequência -> T S T T S T T           T = Tom ("pula uma nota")
    # Exemplo ->  A B C D E F G A          S = SemiTom ("proxima nota")
    


def criarTriade(nota):
    # Conjunto de 3 notas musicais que estruturam um acorde.
    # Acorde: conjunto harmônico de três ou mais notas musicais
    #         que se ouve simultanemente, mas não necessarimante juntas.
    global escolha_escala
    global triade
    if escolha_escala == 'M':
        global e_maior
        triade = [e_maior[e_maior.index(nota)],
                  e_maior[e_maior.index(nota) + 2],
                  e_maior[e_maior.index(nota) + 4]]
    elif escolha_escala == 'm':
        global e_menor
        triade = [e_menor[e_menor.index(nota)],
                  e_menor[e_menor.index(nota) + 2],
                  e_menor[e_menor.index(nota) + 4]]
    


def criarTetrade(nota):
    # Conjunto de 4 notas musicais que estruturam um acorde.
    global escolha_escala
    global tetrade
    if escolha_escala == 'M':
        global e_maior
        tetrade = [e_maior[e_maior.index(nota)],
                   e_maior[e_maior.index(nota) + 2],
                   e_maior[e_maior.index(nota) + 4],
                   e_maior[e_maior.index(nota) + 6]]
    elif escolha_escala == 'm':
        global e_menor
        tetrade = [e_menor[e_menor.index(nota)],
                   e_menor[e_menor.index(nota) + 2],
                   e_menor[e_menor.index(nota) + 4],
                   e_menor[e_menor.index(nota) + 6]]
    


campo = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
         'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E',
         'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')

e_maior = []      # Declarações vazias, para serem usadas dentro das funções.
e_menor = []      # Ao retornarem, elas estarão com as alterações que foram
                  # feitas dentro da função e serão exibidas na tela
triade = []
tetrade = []

escolha_escala = str(input('Escala Maior(M) ou Menor(m): ')).strip()
nota = str(input('De qual nota? ')).upper().strip()
if escolha_escala == 'M':
    escalaMaior(nota)   #chamada da função
    for c in e_maior:
        print(c, end=' ')
elif escolha_escala == 'm':
    escalaMenor(nota)   #chamada da função
    for c in e_menor:
        print(c, end=' ')


escala1 = e_maior[:]        # A escala original será copiada para uma outra
e_maior.extend(escala1)     # lista, para que possa ser realizado alterações
                            # e não perca a lista original.
escala2 = e_menor[:]        # A função "extend" está sendo usada para copiar
e_menor.extend(escala2)     # a lista para dentro de si mesma, como em "campo"


escolha_acorde = str(input('\nTríade(3) ou Tétrade(4): ')).upper().strip()
tonica = str(input('Digite a nota tônica: ')).upper().strip()
if escolha_acorde == '3':
    criarTriade(tonica)   #chamada da função
    for c in triade:
        print(c, end=' ')
elif escolha_acorde == '4':
    criarTetrade(tonica)  #chamada da função
    for c in tetrade:
        print(c, end=' ')
print("\n\n --Programa Finalizado--")
