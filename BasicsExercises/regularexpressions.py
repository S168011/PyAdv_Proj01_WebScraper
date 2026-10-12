import re

def test01() -> None:
    text = "apple, banana, avocado, cherry, apricot"
    regular_expression = r"^a" #Any word that starts with an "a"

    words = text.split(", ")
    filtered_words = [word for word in words if re.match(regular_expression, word)]

    print(filtered_words)


def test02() -> None:
    text = "Er zijn 12 maanden in een jaar, 24 uur in een dag."
    regular_expression = r"[0-9]" #All characters within this range

    words = text.split(" ")
    filtered_words = [word for word in words if re.match(regular_expression, word)]

    print(filtered_words)

def test03() -> None:
    text = "I am walking while singing and eating."
    regular_expression = r"ing\b"

    words = text.split(" ")
    filtered_words = [word for word in words if re.search(regular_expression, word)]

    print(filtered_words)


def test04() -> None:
    text = "Alice wonders everywhere under the sky."
    regular_expression = r"^[^aeiouAEIOU]"

    words = text.split(" ")
    filtered_words = [word for word in words if re.match(regular_expression, word)]

    print(filtered_words)

def test05() -> None:
    text = "Mijn email is voorbeeld@voorbeeld.com en info@test.be."
    regular_expression = r"\w+@\w+\.\w+"

    words = text.split(" ")
    filtered_words = [word for word in words if re.match(regular_expression, word)]

    print(filtered_words)

def main() -> None:
    test01()
    test02()
    test03()
    test04()
    test05()

main()