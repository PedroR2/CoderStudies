# **kwargs

def resultado_f1(**podium):
    print(type(podium))
    for pos, pilot in podium.items():
        print(f'{pos} -> {pilot}')

if __name__ == '__main__':
    resultado_f1(primeiro='ham', segundo='lamb', terceiro='tam')
