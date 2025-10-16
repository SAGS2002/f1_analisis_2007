import pandas as pd

def get_champions_and_report(df_2007_standings):
    """
    Identifica al campeón de la temporada 2007 y genera un reporte
    de la clasificación final.
    """
    if df_2007_standings is None or df_2007_standings.empty:
        print("El DataFrame de 2007 está vacío o es nulo.")
        return None

    # 1. Encontrar la ronda final del año (última carrera)
    final_round = df_2007_standings['round'].max()
    df_final_standings = df_2007_standings[
        df_2007_standings['round'] == final_round
    ].sort_values(by='points', ascending=False)

    # 2. Generar Reporte Final
    top_5_report = df_final_standings[['full_name', 'points', 'wins', 'position']].head(5)
    
    # 3. Identificar al Campeón
    champion = df_final_standings.iloc[0]
    
    print("\n" + "="*50)
    print("       🏆 REPORTE FINAL DE PILOTOS F1 2007 🏆")
    print("="*50)
    print(top_5_report.to_markdown(index=False))
    print(f"\nINSIGHT CLAVE:")
    print(f"El campeón de 2007 fue {champion['full_name']} con {champion['points']} puntos.")
    print(f"El campeonato se definió en la última carrera con una diferencia mínima.")
    print("="*50)
    
    return df_final_standings.head(2) # Devuelve campeón y subcampeón para visualización

if __name__ == '__main__':
    # Crear un DataFrame dummy para probar la función si no se ejecuta main.py
    data = {
        'raceId': [1, 2, 1, 2], 'driverId': [1, 1, 2, 2], 'points': [10, 20, 8, 18],
        'year': [2007, 2007, 2007, 2007], 'round': [1, 2, 1, 2], 
        'forename': ['Kimi', 'Kimi', 'Lewis', 'Lewis'], 'surname': ['Räikkönen', 'Räikkönen', 'Hamilton', 'Hamilton'],
        'code': ['RAI', 'RAI', 'HAM', 'HAM'], 'full_name': ['Kimi Räikkönen', 'Kimi Räikkönen', 'Lewis Hamilton', 'Lewis Hamilton']
    }
    df_dummy = pd.DataFrame(data)
    get_champions_and_report(df_dummy)