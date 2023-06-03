import json


# Dictionaries Relative frequency in the English language in dictionaries order
d_freq = "esiarntolcdugpmkhbyfvwzxqj"

# Dictionaries Relative frequency in the English language in dictionaries order
t_freq = "etaoinshrdlcumwfgypbvkxjqz"


# Add incorrect letters in list
incorrect_letters = []

# Add correct letters in list
correct_letters = []

# Enter correct letters in correct place
correct_place = {1: "", 2: "", 3: "", 4: "", 5: ""}

# Open wordlist file
# with open("words") as f:
#     words = [w.strip() for w in f.readlines()]

fp = open('nywordle.json', "r")
words = json.load(fp)
fp.close()


true_list = []
value = {}


# wrong letters
def f_wl(wl, i):
    for j in wl:
        if j in i:
            return False
    return True

# correct letters
def f_cl(cl, i):
    for j in cl:
        if j not in i:
            return False

    return True

# correct place
def f_cp(l1, l2, l3, l4, l5, i):

    if l1 and (i[0] != l1):
        return False
    elif l2 and (i[1] != l2):
        return False
    elif l3 and (i[2] != l3):
        return False
    elif l4 and (i[3] != l4):
        return False
    elif l5 and (i[4] != l5):
        return False

    else:
        return True


def f_ncp(nl1, nl2, nl3, nl4, nl5, i):

    for j in nl1:
        if i[0] == j:
            return False
    for j in nl2:
        if i[1] == j:
            return False
    for j in nl3:
        if i[2] == j:
            return False
    for j in nl4:
        if i[3] == j:
            return False
    for j in nl5:
        if i[4] == j:
            return False


    return True






def main():
    wl = input("Wrong letter(s) at all (ex. abcd): ")  # wrong letters
    cl = input("Correct letter(s) at all (ex. abcd): ")  # correct letters
    l1 = input("First letter: ")  # first letter
    l2 = input("Second letter: ")  # second letter
    l3 = input("Third letter: ")  # third letter
    l4 = input("Fourth letter: ")  # fourth letter
    l5 = input("Fifth letter: ")  # fifth letter
    nl1 = input("Not First letter: ")  # not first letter
    nl2 = input("Not Second letter: ")  # not second letter
    nl3 = input("Not Third letter: ")  # not third letter
    nl4 = input("Not Fourth letter: ")  # not fourth letter
    nl5 = input("Not Fifth letter: ")  # not fifth letter


    for i in words:
        if f_wl(wl, i) and f_cl(cl, i) and f_cp(l1, l2, l3, l4, l5, i) and f_ncp(nl1, nl2, nl3, nl4, nl5, i):
            true_list.append(i)

    if len(true_list):
        for i in true_list:
            value[i] = 0
            for j in i:
                value[i] += d_freq.index(j)

        sorted_value = sorted(value.items(), key=lambda kv: kv[1])
        print("\n\nanswers: ")
        if len(sorted_value) >= 5:
            for i in range(5):
                print(sorted_value[i][0], sorted_value[i][1])
        else:
            for i in sorted_value:
                print(i[0], i[1])


    else:
        print("\n\nNothing!!!\n Check inputs.")

main()








