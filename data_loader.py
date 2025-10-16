import pandas as pd
import os

#ruta de donde sacaremos los csv, pq amuñuñado se ve feo
DATA_FOLDER = 'data/' 

def load_all_data():
    #Carga todos los archivos CSV en la carpeta 'data/' en un diccionario de DataFrames.

    #archivos que se usaran
    files = {
        'races': 'races.csv',
        'drivers': 'drivers.csv',
        'standings': 'driver_standings.csv'
    }
    
    dataframes = {}
    print("Cargando DataFrames...")
    for name, filename in files.items():
        # Usamos os.path.join para crear la ruta completa de forma segura
        # Esto resultará en 'data/races.csv', 'data/drivers.csv', etc.
        full_path = os.path.join(DATA_FOLDER, filename) 
        
        try:
            # Ahora Pandas busca en la nueva subcarpeta
            dataframes[name] = pd.read_csv(full_path) 
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {full_path}. Asegúrate de que la carpeta 'data/' exista y contenga el archivo.")
            return None
            
    return dataframes

def get_2007_data(dataframes):
    """
    Filtra y une los datos para la temporada 2007.
    """
    if dataframes is None:
        return None

    df_races = dataframes['races']
    df_standings = dataframes['standings']
    df_drivers = dataframes['drivers']

    # 1. Unir 'driver_standings' con 'races' para obtener el año y la ronda
    df_merged = pd.merge(
        df_standings, 
        df_races[['raceId', 'year', 'round']], 
        on='raceId')

    # 2. Filtrar por el año 2007
    df_2007_standings = df_merged[df_merged['year'] == 2007]

    # 3. Unir con 'drivers' para obtener los nombres
    df_2007_standings = pd.merge(
        df_2007_standings,
        df_drivers[['driverId', 'forename', 'surname', 'code']],
        on='driverId'
    )
    
    df_2007_standings['full_name'] = df_2007_standings['forename'] + ' ' + df_2007_standings['surname']

    print(f"\nDatos de 2007 listos. Total de filas: {len(df_2007_standings)}")
    return df_2007_standings

if __name__ == '__main__':
    # Esto es solo para probar la carga de datos
    data = load_all_data()
    if data:
        df_2007 = get_2007_data(data)
        if df_2007 is not None:
            print("\nPrimeras filas del DataFrame de 2007:")
            print(df_2007.head())