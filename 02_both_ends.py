"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""

def both_ends(s):
  # +++ SUA SOLUÇÃO 1 +++
#    if len(s)>=2:
#       newS = s[0] + s[1] + s[-2] + s[-1]
#    else:
#       newS = ''
    # +++ SUA SOLUÇÃO 2: usando slice +++
    #    if len(s)>=2:
    #       newS = s[:2] + s[-2:]
    #    else:
    #       newS = ''

    # +++ SUA SOLUÇÃO 3: usando o while +++
    # count = 0
    # quantCar = len(s)
    # newS= ''
    # if quantCar >= 2:
    #     while count < quantCar:
    #         if count < 2:
    #             newS += s[count]
    #         elif count > quantCar - 2:
    #             if quantCar > 2:
    #                 newS += s[count-1]
    #                 newS += s[count]
    #             else:
    #                 newS += s[count-1]
    #                 newS += s[count-2]

 #           else: continue
 #            count += 1
 #    else:
 #        newS = ''
 #    return newS
    # +++ SUA SOLUÇÃO 4: usando uma linha +++

    return s[:2]+s[-2:] if len(s) >= 2 else ''


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')
