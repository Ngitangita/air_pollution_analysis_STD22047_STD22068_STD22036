def transform_data(data):
    transformed_data = []
    for row in data:
        # Remplacez les valeurs nulles ou incorrectes par des valeurs par défaut
        if row['Average Income (USD)'] == '0.0':
            row['Average Income (USD)'] = 'Unknown'

        if row['Urbanization (%)'] == '':
            row['Urbanization (%)'] = 'Unknown'
        
        # Ajouter d'autres transformations selon les besoins
        transformed_data.append(row)
    
    return transformed_data
