# Creation de clases

class Personne:
    def __init__(self, nom, prenom, sexe):

        self.nom = nom
        self. prenom =  prenom
        self.sexe = sexe

class Client(Personne):
    compter_id = 0
    def __init__(self, nom, prenom, sexe, date_inscription, courriel, mot_de_passe):
        super().__init__(nom, prenom, sexe)
        self.id = Client.compter_id
        Client.compter_id += 1
        self.date_inscriptionn = date_inscription
        self.courriel = courriel
        self.mot_de_passe = mot_de_passe


class Acteur(Personne):
    def __init__(self, nom, prenom, sexe, nom_personnage, date_debut_emploi, date_fin_emploi, cachet):
        super().__init__(nom, prenom, sexe)
        self.nom_personnage = nom_personnage
        self.date_debut_emploi = date_debut_emploi
        self.date_fin_emploi = date_fin_emploi
        self.cachet = cachet

class Employe(Personne):

    def __init__(self, nom, prenom, sexe, date_embacuhe, code_utilisateur, mot_de_passe, type_acces):
        super().__init__(nom, prenom, sexe)
        self.date_embacuhe = date_embacuhe
        self.code_utilisateur = code_utilisateur
        self.mot_de_passe = mot_de_passe
        self.type_acces = type_acces

class Cartecredit:
    def __init__(self, numero, date_expiration, code_secret):
        self.numero = numero
        self.date_expiration = date_expiration
        self.code_secret = code_secret


class Film:
    def __init__(self, nom, duree, description, acteurs):
        self.nom = nom
        self.duree = duree
        self.description = description
        self.acteurs = acteurs


class Categorie:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description



clients = [
        Client("Achury", "Angelica", "F", "2021-04-24", "aachury@gmail.com", "motdepasse1"),
        Client("Langlais", "Alain", "M", "2022-11-25", "alainlanglois15@hotmail.com", "motdepasse2"),
        Client("Pauline", "Bellanda", "F", "2023-01-15", "bpaul@hotmail.com", "motdepasse3"),
        Client("Gagnon", "Benoita", "M", "2024-03-07", "gbenoit@gmail.com", "motdepasse4")

    ]

acteurs = [
        Acteur("Pitt", "Brad", "M", "Tyler Durden", "1999-01-01", "2000-12-31", 1000000),
        Acteur("Jolie", "Angelina", "F", "Lara Croft", "2001-01-01", "2002-12-31", 1500000),
        Acteur("Bonham", "Helena", "F", "Marla Singer", "1999-02-15", "2001-12-31", 1300000),
        Acteur("Elgort", "Ansel", "M", "Augustus Waters", "2013-01-18", "2014-11-27", 1800000)
    ]

employes = [
        Employe("Calixto", "Victor", "M", "2019-09-06", "vaco1985", "cle123", "admin"),
        Employe("Rodriguez", "Carol", "F", "2021-02-07", "carola87", "cle456", "lecture")

    ]

cartecredits = [

        Cartecredit(45130256987, "2025-05-31", 523),
        Cartecredit(19425683216, "2027-01-31", 712),
        Cartecredit(45192412061, "2024-09-31", 972),
        Cartecredit(28091407194, "2026-07-31", 824)
    ]

films = [
        Film("Fight Club", 139,"Un employe de bureau insomniaque et un fabricant de savons diaboliques forment un club de lutte clandestin qui evolue beaucoup.",["Brad Pitt", "Edward Norton", "Helena Bonhamt"]),
        Film("Lara Croft: Tomb Raider", 100,"Laventuriere des jeux video Lara Croft prend vie dans un film ou elle court contre le temps et les mechants pour recuperer de puissants artefacts anciens",["Angelina Jolie", "Alicia Vikander", "Daniel Craig"]),
        Film("Sous la meme etoile", 120,"Depuis son enfance, Hazel a des problemes respiratoires, lobligeant a porter un tube a oxygene en permanence. Sur les conseils de sa mere, elle participe a un groupe de soutien, ou elle fait la connaissance dAugustus, qui a perdu une jambe a cause dun cancer..",["Shailene Woodley", "Ansel Elgort", "Nat Wolff"]),
        Film("Le secret de ses yeux", 153,"Buenos Aires. Benjamin Esposito enquete sur le meurtre violent dune jeune femme. Vingt cinq ans plus tard, il decide decrire un roman base sur cette affaire classee dont il a ete témoin et protagoniste. Benjamin replonge ainsi dans cette periode sombre de lArgentine où lambiance etait etouffante et les apparences trompeuses.",["Ricardo Darin", "ESoledad Villamil", "Guillermo Francella"])
    ]

categories = [
        Categorie("Action", "Des films pleins de scenes daction passionnantes."),
        Categorie("Aventure", "Des films qui vous menent a des voyages passionnants et des decouvertes."),
        Categorie("Romantique", "Films qui vous font reflechir sur les choses vraiment importantes dans la vie."),
        Categorie("Drame", "Des films qui traversent lintrigue et la recherche pour decouvrir la verite.")
    ]