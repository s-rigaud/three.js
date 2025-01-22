
def sort_valid_words():
    # Sort valid word list
    with open('project-words.txt', encoding="utf-8") as f:
        words = f.read().splitlines()

    words.sort(key=lambda x: x.lower())

    with open('project-words.txt', 'w', encoding="utf-8") as f:
        f.write('\n'.join(words))

    print('Words sorted!')

def clean_ts_errors():
    # Clean TS error output
    with open('errors.txt', encoding="utf-8") as f:
        lines = f.read().splitlines()

    banned_errors = [
        "TS7006",  # "Parameter 'x' implicitly has an 'any' type."
    ]

    lines = [l for l in lines for ban_word in banned_errors if ban_word not in l]

    with open('errors.txt', 'w', encoding="utf-8") as f:
        f.write('\n'.join(lines))

    print('Errors cleaned!')

# sort_valid_words()
clean_ts_errors()
