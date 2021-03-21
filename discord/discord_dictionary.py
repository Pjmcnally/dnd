import json, os


def main():
    """This function generates a dictionary of words for Discord. This is necessary
    because discord doesn't respect case when adding words to their dictionary.

    The words themselves are stored in text files in the words subfolder."""

    out_dict = {"enabled": True, "learnedWords": []}

    word_source = r"C:\Users\Patrick\Programming\dnd\discord\words"
    files = os.listdir(word_source)
    for file in files:
        full_path = os.path.join(word_source, file)
        with open(full_path, "r") as f:
            words = [x.strip() for x in f.readlines()]
            out_dict["learnedWords"].extend(words)

    print(json.dumps(out_dict))


main()
