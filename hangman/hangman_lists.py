# p138 challeange

# hanngmanの文字列をリストに格納してrandomでchoiceされる

# p120
import random

hangman_lists = ["blue","green","apple","freedom"]

def show_test():
    for show in hangman_lists: 
        print(show)

def random_choice(show):
    show = random.choice(hangman_lists)
    return show

# test display
if __name__ == "__main__":
    result = random_choice(0)
    print(result)
