def language(sentence):
        y = sentence.split("S", "s")
        z = y[0]
        x = sentence.split("T", "t")
        w = x[0]
        if z > w:
            print("French")
        elif z == w:
            print("French")
        else:
            print("English")

sentence = input("pick a sentence")