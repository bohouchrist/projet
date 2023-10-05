# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:04:56 2023

@author: christ
"""



clients= [{'name': 'Tony Stark', 'item_bought': 'Orange', 'price': 1, 'payment_method': 'Debit Card'}, 
{'name': 'Mary Jane Watson', 'item_bought': 'Bread', 'price': 7, 'payment_method': 'Credit Card'}, 
{'name': 'Pepper Potts', 'item_bought': 'Eggs', 'price': 10, 'payment_method': 'Debit Card'}, 
{'name': 'Lois Lane', 'item_bought': 'Banana', 'price': 3, 'payment_method': 'Debit Card'}, 
{'name': 'Tony Stark', 'item_bought': 'Milk', 'price': 8, 'payment_method': 'Debit Card'}, 
{'name': 'Thor', 'item_bought': 'Butter', 'price': 1, 'payment_method': 'Credit Card'}, 
{'name': 'Bruce Wayne', 'item_bought': 'Grape', 'price': 3, 'payment_method': 'Cash'}, 
{'name': 'Mary Jane Watson', 'item_bought': 'Orange', 'price': 1, 'payment_method': 'Cash'}, 
{'name': 'Peggy Carter', 'item_bought': 'Sugar', 'price': 6, 'payment_method': 'Credit Card'}, 
{'name': 'Peggy Carter', 'item_bought': 'Bread', 'price': 3, 'payment_method': 'Debit Card'}, 
{'name': 'Lois Lane', 'item_bought': 'Coffee', 'price': 5, 'payment_method': 'Credit Card'}, 
{'name': 'Peter Parker', 'item_bought': 'Pepper', 'price': 1, 'payment_method': 'Cash'}, 
{'name': 'Peter Parker', 'item_bought': 'Eggs', 'price': 9, 'payment_method': 'Credit Card'}, 
{'name': 'Lois Lane', 'item_bought': 'Eggs', 'price': 7, 'payment_method': 'Credit Card'}]


# 2. Définition de la fonction pour ajouter de nouveaux clients
def add_client(name, item_bought, price, payment_method):
    """
    Ajoute un nouveau client à la liste des clients.

    Args:
        name (str): Le nom du nouveau client.
        item_bought (str): L'article acheté par le nouveau client.
        price (float): Le montant dépensé par le nouveau client.
        payment_method (str): La méthode de paiement utilisée par le nouveau client.

    Returns:
        None

    Cette fonction crée un dictionnaire représentant un nouveau client avec les informations fournies
    et l'ajoute à la liste 'clients'. La liste 'clients' stocke les informations sur tous les clients.
    """
    new_client = {
        'name': name,
        'item_bought': item_bought,
        'price': price,
        'payment_method': payment_method
    }
    clients.append(new_client)

# Ajout de quatre nouveaux clients à la liste
add_client(name='Tina Turner', item_bought='Banana', price=3, payment_method='Credit Card')
add_client(name='Thérèse Raquin', item_bought='Sugar', price=6, payment_method='Debit Card')
add_client(name='Tony Stark', item_bought='Milk', price=1, payment_method='Cash')
add_client(name='Lois Lane', item_bought='Banana', price=2, payment_method='Cash')

# 3. Calcul du revenu total généré par tous les clients
total_revenue = 0
for client in clients:
    total_revenue += client['price']

# 4. Calcul du montant d'achat moyen par client
# Compter le nombre de clients distincts
distinct_clients = set(client['name'] for client in clients)
nb_clients = len(distinct_clients)

# Calculer le montant d'achat moyen par client
average_amount_per_client = total_revenue / nb_clients

# 5. Trouver l'article le plus populaire acheté
items_count = {}
for client in clients:
    item_name = client['item_bought']
    if item_name in items_count:
        items_count[item_name] += 1
    else:
        items_count[item_name] = 1

# Trouver l'article le plus populaire (celui avec le nombre le plus élevé d'achats)
most_popular_item = max(items_count, key=items_count.get)

# 6. Trouver le client qui a dépensé le plus d'argent
max_spending = 0
most_spending_client = None

for client in clients:
    # Calculer la somme des dépenses pour ce client en particulier
    total_spending = sum(client['price'] for client in clients if client['name'] == client['name'])
    
    # Comparer avec la dépense maximale trouvée jusqu'à présent
    if total_spending > max_spending:
        max_spending = total_spending
        most_spending_client = client['name']

# Afficher les résultats
print("Total revenue generated from all clients:", total_revenue)
print("Average purchase amount per client:", average_amount_per_client)
print("Most popular item purchased:", most_popular_item)
print("Client who spent the most money:", most_spending_client)




# Exercice 1 : Calcul de la somme des éléments d'une matrice

# Définition d'une matrice sous forme de liste de listes
tab = [[1, 2, 3, 4], [4, 5, 6], [7, 8, 9], [111, 222, 333]]

# Initialisation de la variable 'somme' pour stocker la somme des éléments
somme = 0

# Parcours de chaque élément de la matrice en utilisant des boucles for imbriquées
for i in range(len(tab)):  # Parcourt les lignes de la matrice
    for j in range(len(tab[i])):  # Parcourt les éléments de chaque ligne
        somme += tab[i][j]  # Ajoute chaque élément à la somme

# Affichage du résultat de la somme
print(somme)


# Exercice 2 : Transposition d'une matrice

# Définition d'une matrice sous forme de liste de listes
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Détermination du nombre de lignes et de colonnes de la matrice
nb_lignes = len(matrice)
nb_colonnes = len(matrice[0])

# Création d'une nouvelle matrice transposée
matrice_trans = [[matrice[i][j] for i in range(nb_lignes)] for j in range(nb_colonnes)]

# Affichage de la matrice transposée
print(matrice_trans)

# avec des fonctions 

def sum_matrix(matrix):
    """
    Calculate the sum of all elements in a 2D matrix.

    Args:
    matrix (list of list of int or float): The input matrix.

    Returns:
    int or float: The sum of all elements in the matrix.

    Examples:
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> sum_matrix(matrix)
    45

    >>> matrix = [[1.5, 2.5], [3.5, 4.5]]
    >>> sum_matrix(matrix)
    12.0
    """
    # Calculate the sum of elements in the matrix
    total_sum = sum(sum(row) for row in matrix)
    return total_sum

def transpose_matrix(matrix):
    """
    Transpose a 2D matrix.

    Args:
    matrix (list of list of int or float): The input matrix.

    Returns:
    list of list of int or float: The transposed matrix.

    Examples:
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> transpose_matrix(matrix)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    >>> matrix = [[1.5, 2.5], [3.5, 4.5]]
    >>> transpose_matrix(matrix)
    [[1.5, 3.5], [2.5, 4.5]]
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transposed_matrix = [[matrix[i][j] for i in range(num_rows)] for j in range(num_cols)]
    return transposed_matrix








