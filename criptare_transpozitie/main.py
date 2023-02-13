import math
'''
Aceasta metoda de criptare presupune schimbarea pozitiilor caracterelor dintr-un text. Caracterele sunt mutate cu o anumita pozitie
care este data de o cheie. Va rezulta un text permutat, cifrat.
'''

def main() -> None:
    mesaj = input('Introduceti mesajul dorit')
    cheie = int(input(f"Introdu cheia [2-{len(mesaj) - 1}]: "))
    mod = input("Criptare/Decriptare [C/D]: ")

    if mod.lower().startswith("c"):
        prompt = criptare_mesaj(cheie, mesaj)
    elif mod.lower().startswith("d"):
        prompt = decriptare_mesaj(cheie, mesaj)

    #folosim | pentru a identifica spatiile de la sfarsit
    print(f"Mesaj:\n{prompt + '|'}")
def criptare_mesaj(cheie: int, mesaj: str) -> str:
    text_cifrat = [""] * cheie
    for col in range(cheie):
        pointer = col
        while pointer <len(mesaj):
            text_cifrat[col] += mesaj[pointer]
            pointer += cheie

    return  "".join(text_cifrat)

def decriptare_mesaj(cheie: int, mesaj: str) -> str:
    cifru_text = [""] * cheie
    nr_randuri = cheie
    nr_coloane = math.ceil(len(mesaj) / cheie)
    nr_urme = (nr_coloane * nr_randuri) - len(mesaj)
    text_plan = [""] * nr_coloane
    col = 0
    rnd = 0

    for simbol in mesaj:
        text_plan[col] += simbol
        col += 1

        if(
            (col == nr_coloane)
            or (col == nr_coloane - 1)
            and (rnd >= nr_randuri - nr_urme)
        ):
            col = 0
            rnd +=1

    return "".join(text_plan)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

