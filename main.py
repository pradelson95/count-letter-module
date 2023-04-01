from count_letter import countLetter

def test_if_function_works():
    result = countLetter(word="hello", char="o", countUpperCase=False)
    assert result == 1


"""from count_letter import countLetter

palabra = input("escribe la palabra: ")

cont_letter = countLetter(palabra, char="o", countUpperCase=False)

print(cont_letter)"""