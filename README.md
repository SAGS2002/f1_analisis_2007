# f1_analisis_2007
# 🏎️ Proyecto "El Último Baile del V8": Análisis del Campeonato F1 2007

Un estudio profundo de la temporada más dramática del deporte, donde un punto lo decidió todo y **el copiloto invisible ayudó con los cálculos**.

## 🏁 Introducción

Este proyecto realiza un análisis exhaustivo de la temporada de Fórmula 1 de **2007**, la cual es legendaria por su final de infarto. Usando datos históricos, hemos rastreado la evolución de puntos de los principales contendientes (Räikkönen, Hamilton y Alonso) para visualizar la increíble batalla que se libró hasta el último metro en Brasil.

### Colaboración

Todo el código y los *insights* fueron generados por mí, pero debo agradecer a mi **"Asistente Sintético de Lógica Aumentada"** (A.S.L.A.) por su infinita paciencia con el *debugging* de `FileNotFoundError` y por saber exactamente qué función necesitaba mi `main.py`. 🤖

-----

## 📊 Metodología de Análisis

El proyecto sigue una estructura modular limpia, ideal para cualquier análisis de datos basado en Python.

### 1\. Estructura de Archivos

| Carpeta/Archivo | Descripción |
| :--- | :--- |
| `data/` | **Contiene todos los archivos CSV originales** (`races.csv`, `drivers.csv`, `driver_standings.csv`, etc.). |
| `data_loader.py` | Módulo encargado de **cargar los datos** desde la carpeta `data/` y realizar la **unión inicial** de DataFrames para el año 2007. |
| `analysis_2007.py` | Módulo de **cálculo**. Determina la clasificación final, identifica a los tres principales pilotos y genera el reporte tabular final. |
| `visualization.py` | Módulo de **presentación**. Genera el gráfico de líneas con Matplotlib mostrando la evolución de puntos. |
| `main.py` | El **orquestador**. Ejecuta secuencialmente los módulos anteriores para producir el resultado final. |

### 2\. Archivos CSV Utilizados

| Nombre del Archivo | Clave Principal | Propósito en el Análisis 2007 |
| :--- | :--- | :--- |
| `races.csv` | `raceId` | Obtener el año y el número de ronda (`round`). |
| `drivers.csv` | `driverId` | Obtener el `full_name` de cada piloto. |
| `driver_standings.csv` | `raceId`, `driverId` | Trazar los puntos acumulados y la posición en cada ronda. |

-----

## 🚀 Ejecución del Proyecto

Sigue estos pasos para replicar el análisis:

### Requisitos

Asegúrate de tener Python 3 y estas librerías instaladas:

```bash
pip install pandas matplotlib tabulate
```

### Pasos de Ejecución

1.  **Clonar o Descargar** este repositorio.
2.  **Crear la carpeta** `data/` dentro de la carpeta principal.
3.  **Colocar los 10 archivos CSV** de la F1 dentro de la carpeta `data/`.
4.  **Ejecutar el archivo principal** en tu terminal:

<!-- end list -->

```bash
python main.py
```

### Resultado Esperado

El programa imprimirá en la consola el reporte de la clasificación final (Top 5) y luego mostrará una ventana con el gráfico de la evolución de puntos, donde las líneas de los tres contendientes convergen dramáticamente en la última ronda.

-----

## 📈 *Insight* Clave (Spoilers del 2007)

El gráfico es elocuente: la temporada fue tan ajustada que Kimi Räikkönen pudo alzarse con el título en la última carrera a pesar de que Lewis Hamilton y Fernando Alonso lideraron gran parte del año. El campeonato se decidió por **un solo punto**.
