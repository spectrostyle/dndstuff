yes_variants = ['yes', 'y', 'sure', 'ofc', 'please', 'definitely']
no_variants = ['no', 'n', 'nope', 'i love them', 'never']
def terminal_spaces():
    print("\n" * 11)


def empty_line():
    print()


def clean_input(prompt):    # to rid of punctuation etc
    user_input = input(prompt).lower()
    cleaned_input = ""
    for typed in user_input:
        if typed.isalpha():
            cleaned_input += typed
    return cleaned_input


"""
custom_prompt = "(Y)es/(N)o: "
cleaned = clean_input(custom_prompt)
print("Cleaned input:", cleaned)
"""
