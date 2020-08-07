# from nltk.stem.snowball import SnowballStemmer
import string


def parse_out_text(f):
    """Given an opened email file f, parse out all text below the
    metadata block at the top
    (in Part 2, you will also add stemming capabilities)
    and return a string that contains all the words
    in the email (space-separated)

    Example use case:
    >>> f = open("email_file_name.txt", "r")
    >>> text = parse_out_text(f)
    """

    f.seek(0)  # go back to beginning of file (annoying)
    all_text = f.read()

    # split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        # remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        # project part 2: comment out the line below
        words = text_string

        # split the text string into individual words, stem each word,
        # and append the stemmed word to words (make sure there's a single
        # space between each stemmed word)

    return words


def main():
    with open("../11-text-learning/test_email.txt", "r") as f:
        text = parse_out_text(f)
    print(text)


if __name__ == '__main__':
    main()
