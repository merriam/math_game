#!env python3

import random

secret_message = "DON'T FEED TIGERS"
alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    guessed = ""

    for real_letter in secret_message:
        if real_letter not in alphabet:
            guessed += real_letter  # space or punctuation
            continue

        # make question
        first = random.randint(1, 99)
        second = random.randint(1, 99)
        real_answer = first * second
        bluff0 = random.randint(1,9999)
        if bluff0 == real_answer:
            bluff0 += 8
        bluff1 = random.randint(1,9999)
        if bluff1 == real_answer:
            bluff1 += 10
        bluff2 = random.randint(1,9999)
        if bluff2 == real_answer:
            bluff2 += 13
        bluff3 = random.randint(1,9999)
        if bluff3 == real_answer:
            bluff3 += 18

        # print question
        print("What is {} x {}?".format(first, second))

        # make letters.
        bluff_letters = []
        for i in range(3):
            while True:
               bluff_letter = random.choice(alphabet)
               if (bluff_letter not in bluff_letters
                  and bluff_letter != real_letter):
                  break
            bluff_letters.append(bluff_letter)

        # make possible answers
        answers = [ (real_letter, real_answer),
                    (bluff_letters[0], bluff0),
                    (bluff_letters[1], bluff1),
                    (bluff_letters[2], bluff2) ]
        random.shuffle(answers)

        # ask question
        for answer in answers:
            print("{}.  {}".format(answer[0], answer[1]))
        guess = input("Your guess?")

        # show progress
        guessed += guess
        print("MESSAGE:", guessed)


main()
