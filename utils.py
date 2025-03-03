def sort_valid_words():
    # Sort valid word list
    with open("project-words.txt", encoding="utf-8") as f:
        words = f.read().splitlines()

    words.sort(key=lambda x: x.lower())

    with open("project-words.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(words))

    print("Words sorted!")


# remove TS7053
def clean_ts_errors():
    # Clean TS error output
    with open("type-errors.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()

    original_error_count = len(lines)

    banned_folders = ["build/", "  ", "examples/jsm/libs/opentype.module.js"]
    banned_ts_errors = [
        "TS2304",  # "Cannot find name 'x'."
        "TS2584",  # "Cannot find name 'x'. Do you need to install type definitions for node? Try `npm i @types/node` and then add `node` to the types field in your tsconfig."
        "TS7005",  # "Parameter 'x' implicitly has an 'any[]' type."
        "TS7006",  # "Parameter 'x' implicitly has an 'any' type."
        "TS7034",  # "Variable 'x' implicitly has an 'any' type."
    ]
    banned_text_errors = [
        "remove errors like does not exist on type '{}'.",
        "does not exist on type 'Object'."
    ]


    accepted_lines = []
    for line in lines:
        for ban_word in banned_ts_errors:
            if ban_word in line:
                break
        else:
            for ban_folder in banned_folders:
                if ban_folder in line:
                    break
            else:
                for ban_text in banned_text_errors:
                    if ban_text in line:
                        break
                else:
                    accepted_lines.append(line)

    with open("type-errors.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(accepted_lines))

    print(f"Errors cleaned! (error count: {original_error_count} => {len(accepted_lines)})")


sort_valid_words()
clean_ts_errors()
