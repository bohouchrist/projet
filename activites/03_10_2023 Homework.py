# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:04:56 2023

@author: akrac
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



