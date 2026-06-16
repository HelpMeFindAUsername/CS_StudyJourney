accAnswers = ["42", "forty two", "forty-two"]

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

if answer in accAnswers:
    print("Yes")

else:
    print("No")
