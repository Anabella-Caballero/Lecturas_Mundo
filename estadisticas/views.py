import matplotlib
matplotlib.use('Agg') 

import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from coleccion.models import Libro, Puntuacion
from django.db.models import Count, Avg

def libros_por_genero(request):
    # Obtener datos
    datos = Libro.objects.values('genero__nombre').annotate(cantidad=Count('id')).order_by('-cantidad')

    # Separar nombres y cantidades
    nombres_generos = [item['genero__nombre'] for item in datos]
    cantidades = [item['cantidad'] for item in datos]

    
    colores = ['#FFB6C1', '#FF69B4', '#FFC0CB', '#FFA07A', '#FFDAB9', '#FAAFBA', '#F4C2C2']

    # Crear gráfico
    plt.figure(figsize=(8, 6))
    plt.bar(nombres_generos, cantidades, color=colores[:len(nombres_generos)])
    plt.title('Cantidad de Libros por Género', fontsize=14)
    plt.xlabel('Género', fontsize=12)
    plt.ylabel('Cantidad', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Exportar imagen como respuesta HTTP
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='image/png')



def promedio_puntuaciones_libro(request):
    datos = Libro.objects.annotate(promedio=Avg('puntuaciones__puntuacion')).filter(promedio__isnull=False).order_by('-promedio')

    titulos = [libro.titulo for libro in datos]
    promedios = [round(libro.promedio, 2) for libro in datos]

    colores = ['#F4A7B9', '#F7C5CC', '#FFD1DC', '#FAB1A0', '#FDCBBA', '#E0B0FF', '#FFCCE5']

    # Aumentar tamaño del gráfico en altura
    plt.figure(figsize=(12, max(6, len(titulos) * 0.4)))  # Altura dinámica

    # Gráfico de barras horizontal
    plt.barh(titulos, promedios, color=colores, edgecolor='gray')
    plt.xlabel('Promedio de Puntuación', fontsize=12)
    plt.title('Promedio de Puntuaciones por Libro', fontsize=14)

    # Reducir tamaño de fuente de etiquetas y mejorar espacio
    plt.yticks(fontsize=9)
    plt.xticks(fontsize=10)
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='image/png')