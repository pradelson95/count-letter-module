from typing import Optional


def countLetter(word: str, char: str, countUpperCase: Optional[bool] = False) -> int:
    if not isinstance(word, str):
        raise TypeError("El parámetro 'word' debe ser de tipo str")
    if not isinstance(char, str) or len(char) != 1:
        raise TypeError("El parámetro 'char' debe ser una cadena de un solo carácter")
    if not isinstance(countUpperCase, bool):
        raise TypeError("El parámetro 'countUpperCase' es opcional y debe ser de tipo bool")

    count = 0
    for letter in word:
        if letter == char:
            count += 1
        elif countUpperCase and letter.lower() == char.lower():
            count += 1
    return count
