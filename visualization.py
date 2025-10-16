import matplotlib.pyplot as plt
import pandas as pd

# Definimos el año objetivo para títulos
TARGET_YEAR = 2007

def plot_standings_evolution(df_standings, top_drivers):
    """
    Crea un gráfico de la evolución de puntos para los principales pilotos de la temporada.
    
    Args:
        df_standings (pd.DataFrame): DataFrame con los datos de clasificación del año.
        top_drivers (pd.DataFrame): DataFrame con el Top 3 de pilotos (campeón, 2do y 3er).
    """
    if df_standings is None or top_drivers.empty:
        print("Datos insuficientes para la visualización.")
        return

    # Estilos predefinidos para los tres pilotos principales
    # Los colores están elegidos para representar a los equipos (Ferrari, McLaren)
    styles = [
        {'color': '#E10600', 'linestyle': '-', 'marker': 'o', 'label': 'Campeón (1°)'},  # Rojo para el Campeón (Ferrari)
        {'color': '#FF8000', 'linestyle': '--', 'marker': 's', 'label': 'Subcampeón (2°)'},  # Naranja/Azul para McLaren
        {'color': '#0090FF', 'linestyle': ':', 'marker': 'x', 'label': '3er Lugar'}         # Azul para McLaren/Otro contendiente
    ]

    plt.figure(figsize=(14, 7))

    # Iterar sobre el Top 3 (o menos, si el DataFrame es más pequeño)
    for i, (index, driver) in enumerate(top_drivers.head(3).iterrows()):
        
        # Si hay más estilos que pilotos, evita IndexError
        if i >= len(styles):
            break 

        driver_id = driver['driverId']
        driver_name = driver['full_name']
        style = styles[i]
        
        # Filtrar datos de la temporada para el piloto actual
        df_driver = df_standings[df_standings['driverId'] == driver_id]

        # Graficar la evolución
        plt.plot(
            df_driver['round'], df_driver['points'],
            label=f"{driver_name} ({style['label']})", 
            marker=style['marker'], 
            linestyle=style['linestyle'], 
            color=style['color'], 
            linewidth=2
        )

    # Añadir elementos visuales para claridad
    plt.title(f'Evolución de Puntos Acumulados - Pilotos F1 {TARGET_YEAR}', fontsize=18, weight='bold')
    plt.xlabel('Ronda de Carrera', fontsize=14)
    plt.ylabel('Puntos Acumulados', fontsize=14)
    
    # Resaltar la última ronda donde se decidió el campeonato
    final_round = df_standings['round'].max()
    plt.axvline(x=final_round, color='gray', linestyle='-.', alpha=0.5, label='Última Carrera')
    
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    plt.legend(title=f'Piloto (Clasificación Final {TARGET_YEAR})', fontsize=11, loc='lower right')
    
    # Mejorar ticks del eje X
    plt.xticks(df_standings['round'].unique()[::2]) # Mostrar cada 2 rondas para evitar sobrecarga
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # --- Bloque de Prueba para asegurar que la visualización funcione ---
    # Simula un final muy ajustado (como el de 2007)
    rounds = list(range(1, 18))
    
    # Puntos que reflejan la lucha de 2007:
    # Hamilton y Alonso lideran, pero Kimi gana al final
    data_points = {
        'round': rounds * 3,
        'driverId': [8] * 17 + [1] * 17 + [4] * 17,
        'points': [10, 20, 30, 40, 50, 60, 64, 74, 84, 94, 98, 106, 109, 112, 112, 100, 110] + # Kimi (RAI)
                [12, 22, 32, 42, 52, 62, 70, 80, 90, 100, 107, 107, 107, 107, 109, 109, 109] + # Hamilton (HAM)
                [8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 105, 105, 105, 105, 107, 107, 109], # Alonso (ALO)
        'full_name': ['Kimi Räikkönen'] * 17 + ['Lewis Hamilton'] * 17 + ['Fernando Alonso'] * 17
    }
    df_dummy = pd.DataFrame(data_points)
    
    # Crear un Top 3 dummy ordenado por puntos finales (110, 109, 109)
    champion_sub = pd.DataFrame({
        'driverId': [8, 1, 4], 'full_name': ['Kimi Räikkönen', 'Lewis Hamilton', 'Fernando Alonso'],
        'points': [110, 109, 109], 'wins': [6, 4, 4]
    })
    
    plot_standings_evolution(df_dummy, champion_sub)