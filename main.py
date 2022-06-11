nom=""
age=0

def demander():  
    age_str=0  
    while age_str==0:
        age_str = input("Quel est ton age? ")
        try:
            age_int = int(age_str)
        except:
            print("Erreur: Vous devez taper un nombre pour l'age ")
    return age_int

def name():
    nom=""
    while nom=="":
        nom= input("Quel est votre nom? ")
    return nom
    
def reponse(nom,age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age1) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")
    if age >=60:
        print("Vous êtes sénior.")
    elif age==17:
        print("Vous êtes presque majeur !")
    elif age==18:
        print("Vous êtes tous juste majeur") 
    elif age>=18:
        print("Vous êtes majeur")
    elif age<10:
        print("Vous êtes un enfant !!")
    else:
        print("vous êtes mineurs.")

nom1=name()
age1=demander()
reponse(nom1,age1)
