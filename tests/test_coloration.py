from coloration.welsh_powell import welsh_powell
from coloration.dsatur import dsatur
from coloration.comparaison import comparer_algorithmes

graphe_test = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["C"]
}

print("Welsh-Powell")
print(welsh_powell(graphe_test))

print()

print("DSATUR")
print(dsatur(graphe_test))

print()

comparer_algorithmes(graphe_test)