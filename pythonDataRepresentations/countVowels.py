def count_vowels(vowelString):
        counta = vowelString.count('a')
        counte = vowelString.count('e')
        counti = vowelString.count('i')
        counto = vowelString.count('o')
        countu = vowelString.count('u')

        total = counta+counte+counti+counto+countu
        return total




print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))