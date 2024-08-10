import csv

def load_data(transformed_data):
    if not transformed_data:
        print("Aucune donnée à enregistrer.")
        return
    
    try:
        with open('transformed_air_pollution_data.csv', mode='w', newline='') as file:
            fieldnames = transformed_data[0].keys()  
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in transformed_data:
                writer.writerow(row)
        print("Données enregistrées avec succès dans 'transformed_air_pollution_data.csv'.")
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")
