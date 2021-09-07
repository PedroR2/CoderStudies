# **kwargs

def resultado_f1(primeiro, segundo, terceiro):
    print(f'1 -> {primeiro} \n'
          f'2 -> {segundo} \n'
          f'3 -> {terceiro}')


if __name__ == '__main__':
    podium = {'primeiro': 'ham', 'segundo': 'lamb', 'terceiro': 'tam'}
    resultado_f1(**podium)
