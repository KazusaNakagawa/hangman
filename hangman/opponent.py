# Opponent choice

import hangman_lists
import word_input

def choice(word):
    print("Opponent choices")

    try:
        while True:
            choice = input("1:cpu 2:player1\n ")
            if choice == "1":
                # word = listからchoiceされた単語
                # cpu
                word = hangman_lists.random_choice(0)
                return word
            elif choice == "2":
                # word_input
                # player1
                word = word_input.input_word(0)
                return word
            else:
                print("input error")
                print("Please re-input")
                continue
            break
    except TypeError as e:
        print("TypeError" + str(e))


# test display
if __name__ == "__main__":
    result = choice(0)
    print(result)

