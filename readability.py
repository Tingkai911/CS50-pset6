def main():
    text = input("Text: ")
    cl_index(text)

def cl_index(text):
    total_space = 0;
    total_words = 0;
    total_sentence = 0;
    total_length = len(text);
    inside_word = False;
    total_non_alpha = 0;

    for char in text:

        if char == " ":
            total_space += 1
            inside_word = False

        elif inside_word == False:
            inside_word = True
            total_words += 1

        if char == "." or char == "!" or char == "?":
            total_sentence += 1

        if char.isalpha() == False:
            total_non_alpha += 1

    total_length = total_length - total_non_alpha
    print(total_length)
    print(total_sentence)
    print(total_words)

    avg_length = total_length*100/total_words
    avg_sentence = total_sentence*100/total_words

    print(avg_length)
    print(avg_sentence)
    
    # bug with index
    index = round(0.0588 * avg_length - 0.296 * avg_sentence - 15.8)
    print(index)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {int(index)}")

main()