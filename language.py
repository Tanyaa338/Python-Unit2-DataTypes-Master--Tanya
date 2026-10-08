""" def language(sentence):
        y = sentence.split("S")
        y = sentence.split("s")
        z = y[0]
        x = sentence.split("T")
        x = sentence.split("t")
        w = x[0]
        if z > w:
            print("English")
        elif z == w:
            print("French")
        else:
            print("French")

sentence = input("pick a sentence")
language(sentence) """


""" def language(sentence):
        for i in range(sentence)
        if z > w:
            print("English")
        elif w > z:
             print ("French")
        else:
            print("French")

sentence = input("pick a sentence")
language(sentence) """

def language(sentence):
    num_Tt = 0
    num_Ss = 0
    for i in range(sentence):
        if sentence[i] == "T" or "t":
            num_Tt += 1
        if sentence[i] == "S" or "s":
            num_Ss += 1
    if num_Tt > num_Ss:
        print("English")
    elif  num_Ss > num_Tt:
        print("French")
    else:
        print("French")

sentence = input("Pick a sentence.")
language(sentence)

""" x = 6
while True:
    print("Running")
    if x == 5:
    break
while guess != number: """

#index card: loop example, sample function, how to access individual items in string
