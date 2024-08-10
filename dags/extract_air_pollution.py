import csv

def extract_air_pollution():
    data = []
    try:
        with open('air_pollution_data.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print("Le fichier 'air_pollution_data.csv' est introuvable. Assurez-vous qu'il est bien dans le même dossier que ce script.")
    return data
