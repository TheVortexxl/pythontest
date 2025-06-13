"""
Test de Competențe Python
Nume: ..................................
Data: ..................................

Instrucțiuni: Completați codul de mai jos pentru a rezolva fiecare exercițiu.
"""

# ==============================================================================
# Exercițiul 1: Corectarea erorilor de sintaxă
# ==============================================================================
"""
Problemă: Codul de mai jos ar trebui să afișeze "Salut, Lume!", dar conține o eroare de sintaxă. Corectați linia de cod.
"""
# Scrieți codul corectat aici:
print("Salut, Lume!"


# ==============================================================================
# Exercițiul 2: Corectarea erorilor de logică
# ==============================================================================
"""
Problemă: Acest cod ar trebui să adune două numere, dar rezultatul este incorect din cauza tipului de date greșit. Corectați eroarea de logică pentru a obține suma matematică.
"""
numar1 = "5"
numar2 = "10"
# Scrieți codul corectat aici:
suma = numar1 + numar2
print(f"Suma este: {suma}")


# ==============================================================================
# Exercițiul 3: Funcție simplă
# ==============================================================================
"""
Problemă: Scrieți o funcție numită `salut` care primește un nume ca argument și afișează un mesaj de salut personalizat.
Exemplu de utilizare: `salut("Ana")` ar trebui să afișeze "Salut, Ana!".
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# salut("Ana")


# ==============================================================================
# Exercițiul 4: Funcție cu returnare de valoare
# ==============================================================================
"""
Problemă: Scrieți o funcție numită `calcul_arie_dreptunghi` care primește lungimea și lățimea unui dreptunghi și returnează aria acestuia.
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# aria = calcul_arie_dreptunghi(5, 10)
# print(f"Aria dreptunghiului este: {aria}") # Ar trebui să afișeze 50


# ==============================================================================
# Exercițiul 5: Lucrul cu liste
# ==============================================================================
"""
Problemă: Scrieți o funcție numită `gaseste_numar_maxim` care primește o listă de numere și returnează cel mai mare număr din listă. Nu folosiți funcția încorporată `max()`.
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# numere = [1, 7, 3, 9, 2]
# print(f"Numărul maxim din listă este: {gaseste_numar_maxim(numere)}") # Ar trebui să afișeze 9


# ==============================================================================
# Exercițiul 6: Filtrarea unei liste
# ==============================================================================
"""
Problemă: Scrieți o funcție numită `filtreaza_numere_pare` care primește o listă de numere și returnează o nouă listă care conține doar numerele pare.
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# numere = [1, 2, 3, 4, 5, 6]
# print(f"Numerele pare sunt: {filtreaza_numere_pare(numere)}") # Ar trebui să afișeze [2, 4, 6]


# ==============================================================================
# Exercițiul 7: Lucrul cu dicționare
# ==============================================================================
"""
Problemă: Scrieți o funcție numită `afiseaza_informatii_student` care primește un dicționar ce reprezintă un student și afișează informațiile acestuia într-un format lizibil (ex: "Nume: Ion Popescu").
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# student_exemplu = {
#     "nume": "Ion Popescu",
#     "varsta": 21,
#     "specializare": "Informatică"
# }
# afiseaza_informatii_student(student_exemplu)


# ==============================================================================
# Exercițiul 8: Actualizarea unui dicționar
# ==============================================================================
"""
Problemă: Scrieți o funcție numită `adauga_nota` care primește un dicționar de student și o notă nouă. Funcția trebuie să adauge nota la o listă de note din dicționar. Dacă cheia "note" nu există, trebuie să o creați. Funcția trebuie să returneze dicționarul actualizat.
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# student1 = {"nume": "Maria Ionescu"}
# student1 = adauga_nota(student1, 10)
# student1 = adauga_nota(student1, 9)
# print(student1) # Ar trebui să afișeze {'nume': 'Maria Ionescu', 'note': [10, 9]}


# ==============================================================================
# Exercițiul 9: Combinarea listelor și condițiilor
# ==============================================================================
"""
Problemă: Scrieți o funcție numită `numara_studenti_promovati` care primește o listă de dicționare (studenți) și returnează numărul de studenți cu o medie mai mare sau egală cu 5.
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# lista_studenti_exemplu = [
#     {"nume": "Alex", "medie": 8.5},
#     {"nume": "Dana", "medie": 4.2},
#     {"nume": "Mihai", "medie": 9.1},
#     {"nume": "Laura", "medie": 4.9}
# ]
# print(f"Numărul de studenți promovați: {numara_studenti_promovati(lista_studenti_exemplu)}") # Ar trebui să afișeze 2


# ==============================================================================
# Exercițiul 10: Procesare de text
# ==============================================================================
"""
Problemă: Scrieți o funcție numită `frecventa_cuvinte` care primește un text și returnează un dicționar cu frecvența fiecărui cuvânt. Ignorați majusculele și punctuația de bază (virgulă, punct).
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# text_exemplu = "Salut, acesta este un test. Salut din nou!"
# print(f"Frecvența cuvintelor: {frecventa_cuvinte(text_exemplu)}")


# ==============================================================================
# Exercițiul 11: Simulare coș de cumpărături
# ==============================================================================
"""
Problemă: Scrieți o funcție `calculeaza_total_cos` care primește un dicționar cu produse disponibile (nume: preț) și o listă cu produse din coș. Returnează costul total. Ignoră produsele din coș care nu sunt disponibile.
"""
# Scrieți funcția aici:



# Exemplu de utilizare (decomentați pentru a testa):
# produse_magazin = {
#     "lapte": 5.5,
#     "paine": 3.0,
#     "oua": 12.0,
#     "ciocolata": 7.8
# }
# cosul_meu = ["lapte", "paine", "paine", "bomboane"]
# print(f"Totalul coșului este: {calculeaza_total_cos(produse_magazin, cosul_meu):.2f} RON") # Ar trebui să afișeze 11.50 RON


# ==============================================================================
# Exercițiul 12: Mini-agendă telefonică
# ==============================================================================
"""
Problemă: Creați funcționalitățile pentru o mini-agendă telefonică. Completați corpul fiecărei funcții de mai jos pentru a îndeplini sarcina specificată în numele ei.
"""
# Scrieți funcțiile aici:
def adauga_contact(agenda, nume, numar):
  pass # Șterge 'pass' și scrie codul tău

def cauta_contact(agenda, nume):
  pass # Șterge 'pass' și scrie codul tău

def sterge_contact(agenda, nume):
  pass # Șterge 'pass' și scrie codul tău

def afiseaza_toate_contactele(agenda):
  pass # Șterge 'pass' și scrie codul tău


# Exemplu de utilizare (decomentați pentru a testa):
# agenda_mea = {}
# adauga_contact(agenda_mea, "Ana", "0722111222")
# adauga_contact(agenda_mea, "Mihai", "0744333444")
# afiseaza_toate_contactele(agenda_mea)
# cauta_contact(agenda_mea, "Ana")
# sterge_contact(agenda_mea, "Mihai")
# afiseaza_toate_contactele(agenda_mea)