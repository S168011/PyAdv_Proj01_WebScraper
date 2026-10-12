from spellchecker import SpellChecker

while True:
    spell = SpellChecker()
    print("Geef het volgende woord.")
    word = input("> ")
    corrected_word = spell.correction(word)
    if word == corrected_word:
        print(f"\"{word}\" is een woord in het Engels.")
    else:
        print(f"\"{word}\" is geen woord in het Engels.")
