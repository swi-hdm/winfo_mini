"""Tests für rechner.py – werden bei jedem Push und Pull Request automatisch
von GitHub Actions ausgeführt (siehe .github/workflows/ci.yml).
"""

from rechner import begruessung, addiere, durchschnitt


def test_begruessung():
    assert begruessung("Welt") == "Hallo Welt, willkommen zur GitHub-Demo!"


def test_addiere():
    assert addiere(2, 3) == 5


def test_addiere_negativ():
    assert addiere(-1, 1) == 0


def test_durchschnitt():
    assert durchschnitt([2, 4, 6]) == 4


def test_durchschnitt_leer():
    assert durchschnitt([]) == 0
