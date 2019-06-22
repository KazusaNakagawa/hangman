# hangman word input
# player1

def input_word(word):
    print("player1")
    print("Please enter the words with 3 to 7 letters")
    
    try:
        while True:
            word = input("word Please input : ")
            if len(word) < 8 and len(word) > 2:
                print("could enter it")
                return word
            elif len(word) >= 8:
                print("8 letter or less")
                continue
            elif len(word) <=2 :
                print("3 letter or more")
                continue
            else:
                print("input error")
                print("Please re-input")
                continue
            break
    except TypeError as e:
        print("TypeError : " + str(e)) 
        
    
# test display
if __name__ == "__main__":
    result = input_word(0)
    print(result)
