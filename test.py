

with open('project-words.txt', encoding="utf-8") as f:
    words = f.read().splitlines()

words.sort(key=lambda x: x.lower())

with open('project-words.txt', 'w', encoding="utf-8") as f:
    f.write('\n'.join(words))

print('Words sorted!')