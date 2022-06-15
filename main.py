def poserQuestion(titre):
    question = titre[0]
    r=titre[1]
    bonneReponse=titre[2]
    print()
    print(f"Question : {question}")
    print()
    for i in range(len(r)):
        print(f"{i+1} - {r[i]}")
    print()
    reponse = input(f"Quel est votre réponse ? (entre 1 et {i+1}) ")
    reponseint = int(reponse)
    if r[reponseint-1].lower() == bonneReponse.lower():
        print("Bonne réponse !!")
    else:
        print("Mauvaise réponse !! ")

question1=("Quel est la capital de France ?",("Bordeaux","Marseille","Paris","Nice"),"paris")
question2=("Quel est la capital de l'Italie?",("Florntin","Venise","Pise","Rome"), "rome")

poserQuestion(question1)
poserQuestion(question2)