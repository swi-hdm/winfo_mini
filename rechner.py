"""Ein bewusst einfaches Modul für die GitHub-Demo.

Der Code ist absichtlich trivial gehalten. Im Mittelpunkt der Übung
steht der *Workflow* (Branch, Pull Request, Review, CI) – nicht die
Logik selbst. Eine README- oder Code-Zeile zu ändern reicht völlig,
um den kompletten Ablauf einmal zu durchlaufen.
"""


def begruessung(name):
    """Gibt eine freundliche Begrüßung zurück."""
    return f"Hallo {name}, willkommen zur GitHub-Demo!"


def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b


def durchschnitt(zahlen):
    """Berechnet den Durchschnitt einer Liste von Zahlen."""
    if not zahlen:
        return 0
    return sum(zahlen) / len(zahlen)
