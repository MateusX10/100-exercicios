def cronometro(tempo):

    from time import sleep


    while tempo >= 0:

        print(f"\033[1;32mRestante: {tempo} segundos\033[m")

        sleep(1)

        tempo -= 1

    print("\033[1;31mTempo esgotado! ⏰\033[m")