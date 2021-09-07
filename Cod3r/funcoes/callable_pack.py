def calc_prec_fina(pbruto, impost, *params):
    return pbruto+(pbruto*impost(*params))

def impost1(importado):
    return 0.22 if importado else 0.13

def impost2(explosivo, nivel=1):
    return 0.11*nivel if explosivo else 0

if __name__=='__main__':
    pbruto = 134.98
    pfinal = calc_prec_fina(pbruto, impost1, True)
    pfinal2 = calc_prec_fina(pfinal, impost2, True, 1.5)
    print('Preco final = {:.2f}'.format(pfinal2))
