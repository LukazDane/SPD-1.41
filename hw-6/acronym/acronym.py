def abbreviate(words):
    s_words = words.replace("_", "").replace("-", " ").split()
    letters = [s_word[0] for s_word in s_words]
    return "".join(letters).upper()


print(abbreviate("You ain't slick"))
print(abbreviate("Quiet Under Etherial Eternal Night"))
print(abbreviate("Death Releives A God"))
print(abbreviate("He Eagerly Ran"))
print(abbreviate("She Looks At You"))
print(abbreviate("Holy Eastern River"))
