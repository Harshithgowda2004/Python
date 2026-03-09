def play():

    score = 0

    questions = {
        "Python was created by?": "guido",
        "2 + 2 = ?": "4",
        "Capital of India?": "delhi"
    }

    for q,a in questions.items():
        ans = input(q+" ").lower()
        if ans == a:
            print("Correct")
            score += 5
        else:
            print("Wrong")

    return score