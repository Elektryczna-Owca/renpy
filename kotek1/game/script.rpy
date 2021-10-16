label start:
    scene bg desert

    "Na środku pustyni stał Kotek"
    show cat at right

    "i jadł ziemniaka."
    show potato at left

    "Kotek kochał rybki, ktore są w wodzie."
    show fish

    menu:
        "Zjedz ziemniaka":
            jump ziemniak

        "Zjedz rybkę":
            jump rybka

label ziemniak:
    "Ziemniak umarł!"
    hide potato
    "Po śmierci ziemniaka powstała nowa ziemia oraz farma ziemniakow i marchewek"
    scene bg farm
    "Kot" "Zmieniłem kolor na niebieski"
    show kot3 at right
    ""

    return

label rybka:
    "zlowił rybke"
    hide fish
    show fish1
    "nie mógł znaleźć drogi do domu, więc wziął koszyk i nazbierał zapasów na drogę w poszukiwaniu domu"
    "znalazł drogę do domu, po czym ją ugotował i zjadł"

    menu:
        "schowaj się w norze":
            jump nora

        "zmień się w syrenę":
            jump syrena

        "zatakuj pszczoły":
            jump pszczoly

label syrena:
    hide fish
    hide fish1
    hide potato
    hide cat
    show syrena
    "możesz zdobywać więcej pożywienia"
    "ale..."
    "masz trudniejsze warunki życia"

    return

label pszczoly:
    "duże obrażenia"

    return

label nora:
    "spotkał tam kolegę szympansa a on mu dał niebieskiego banana"

    return
