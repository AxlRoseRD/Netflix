from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style, init

# 1. Cargar el archivo 'netflix_title.csv'
data = pd.read_csv('netflix_titles.csv')

# 2. Visualizar los primeros 10 registros del conjunto de datos
print(Fore.CYAN + '=== 2. Mostrar los primeros 10 registros ===')
print(Fore.YELLOW, data.head(10).to_string())

# 3. Visualizar los últimos 15 registros del conjunto de datos
print(Fore.CYAN, '=== 3. Visualizar los últimos 15 registros del conjunto de datos ===')
print(Fore.YELLOW, data.tail(10))

# 4. Generar los estadísticos básicos
print(Fore.CYAN + '=== 4. Generar los estadísticos básicos ===')
print(Fore.YELLOW, data.describe())

# 5. Completar todos los datos vacíos (na) con ceros (0)
print(Fore.CYAN + '=== 5. Completar todos los datos vacíos (na) con ceros (0) ===')
print(Fore.YELLOW, data.fillna("0"))

# 6. Generar un gráfico de tipo barras que compare películas vs series desde el 2010 hasta el 2021. El resultado del grafico debe ser algo asi:
print(Fore.CYAN + '=== 6. Generar un gráfico de tipo barras que compare películas vs series desde el 2010 hasta el 2021. El resultado del grafico debe ser algo asi: ===')

# Filtrar datos por rango de años (2010-2021)
filtered_data = data[(data['release_year'] >= 2010) & (data['release_year'] <= 2021)]

#Separar películas y series
tv_shows = filtered_data[filtered_data['type'] == 'TV Show']
movies = filtered_data[filtered_data['type'] == 'Movie']

#Contar la cantidad de películas y series por año
movie_counts = movies['release_year'].value_counts().sort_index()
tv_show_counts = tv_shows['release_year'].value_counts().sort_index()

#Crear un DataFrame para el gráfico
df = pd.DataFrame({'Movies': movie_counts, 'TV Shows': tv_show_counts})

ax = df.plot.bar()

plt.show()

# Index(['show_id', 'type', 'type_id', 'title', 'director', 'cast', 'country',
#        'date_added', 'release_year', 'rating', 'duration', 'listed_in',
#        'description'],
#       dtype='object')

