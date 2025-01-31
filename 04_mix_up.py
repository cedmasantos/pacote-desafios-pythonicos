"""
04. mix_up

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Assuma que a e b tem tamanho 2 ou maior.
"""

def mix_up(a, b):
    # +++ SUA SOLUÇÃO 1 +++
    # newa = b[0] + b[1] + a[2:]
    #
    # newb = a[0] + a[1] + b[2:]
    # newS = newa + ' ' + newb

    # +++ SUA SOLUÇÃO 2 +++
 #   return b[0] + b[1] + a[2:] + ' ' + a[0] + a[1] + b[2:]

    # +++ SUA SOLUÇÃO 3: replace e join +++
    newa = a.replace(a[0], b[0]).replace(a[1], b[1])
    newb = b.replace(b[0], a[0]).replace(b[1], a[1])
#    return newa + ' ' + newb

    newS = ' '.join([newa, newb])
    return newS if len(a) > 2 and len(b)>2 else ""



# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
