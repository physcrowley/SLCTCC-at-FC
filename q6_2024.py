"""Solution valide à SLC 2024 Q6

Exemple fait par David Crowley, EAO en mai 2026

Cette solution met la grande partie de la logique
dans des méthodes d'une classe Cipher représentant chaque cas.
L'extraction des données vers cette structure et l'analyse des cas
individuels est alors très simple en fin de programme.
"""

TESTING = False
INPUT_PATH = "test6.txt" if TESTING else "SLC 2024 Materials/Input/DATA61.txt"

# PLACER LES DONNÉES DU FICHIER EN MÉMOIRE
data = []
with open(INPUT_PATH, "r") as file:
    data = file.readlines()

# TRAITER LES DONNÉES


## Définir les éléments individuels de l'algorithme dans une classe
class Cipher:
    def __init__(self, S: str, M: str):
        self.S = S.strip()
        self.M = M.strip()

    def _get_s_prime(self) -> str:
        result = ""
        for c in range(len(self.S) - 1, -1, -1):
            result += self.S[c]
        return result

    def _sub_S_for_S_prime(self) -> tuple[int, str]:
        search_text = self.M
        S_prime = self._get_s_prime()
        result = ""
        count = 0
        while True:
            # cas de sortie : text restant est trop court
            if len(search_text) < len(self.S):
                result += search_text
                break
            pos = search_text.find(self.S)
            # cas de sortie : aucune autre substitution
            if pos == -1:
                result += search_text
                break
            # cas itératif : substitution trouvée
            count += 1
            result += search_text[:pos] + S_prime
            next_pos = pos + len(S_prime)
            search_text = search_text[next_pos:]
        return (count, result)

    def _find_spaces(self, text: str) -> list[int]:
        here = []
        pos = 0
        for pos in range(len(text)):
            if text[pos] == " ":
                here.append(pos)
        return here

    def _compact(self, text: str) -> str:
        return text.replace(" ", "")

    def _expand(self, text: str, space_positions: list[int]) -> str:
        for pos in space_positions:
            text = text[:pos] + " " + text[pos:]
        return text

    def _shift(self, count: int, text: str) -> str:
        # gérer les espaces dans le texte
        space_positions = self._find_spaces(text)
        compact = self._compact(text)

        if count % 2 == 0:
            shift = count * count
            # forward shift brings back to the front
            result = compact[-shift:] + compact[:-shift]
        else:
            shift = 2 * count
            # backward shift puts front at the back
            result = compact[shift:] + compact[:shift]

        return self._expand(result, space_positions)

    def encrypt(self) -> tuple[int, str]:
        count, M_subbed = self._sub_S_for_S_prime()
        shifted = self._shift(count, M_subbed)
        return (count, shifted)


## Structurer les données comme une liste de type Cipher
cases = []
for i in range(0, len(data), 2):
    cases.append(Cipher(data[i], data[i + 1]))


## Itérer sur la liste avec la méthode encrypt
for c in cases:
    n, text = c.encrypt()
    print(n)
    print(text)

## tests
# c = Cipher(data[0], data[1])
# print(c.S, c._S_prime)
# compact = c._compact(c.M)
# print(c.M, compact)
# print(c._expand(compact, c._find_spaces(c.M)))
# print(c.encrypt())
