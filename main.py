# main.py

import data_loader
import analysis_2007
import visualization

def run_2007_analysis():

    print("--- INICIO DEL ANÁLISIS DE DATOS F1 2007 ---")
    
    #Carga y Preparación de Datos
    all_data = data_loader.load_all_data()
    df_2007 = data_loader.get_2007_data(all_data)
    
    if df_2007 is None or df_2007.empty:
        print("Análisis detenido debido a datos faltantes o nulos.")
        return

    #Análisis y Reporte de Clasificación Final
    champion_and_runner_up = analysis_2007.get_champions_and_report(df_2007)
    
    #Visualización de Insights
    if champion_and_runner_up is not None:
        visualization.plot_standings_evolution(df_2007, champion_and_runner_up)
    
    print("--- ANÁLISIS COMPLETADO ---")

if __name__ == '__main__':
    run_2007_analysis()