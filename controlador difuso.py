#control difuso
# jonatan hernandez henao 
#1053864927
#encontrar valor de la propina a partir de la calidad del servicio

#importar librerias
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x_calidad = np.arange (0, 11, 1)
x_servicio = np.arange(0, 11, 1)
x_propina = np.arange (0, 26, 1)

calidad_baja = fuzz.trimf(x_calidad, [0, 0, 5])  
calidad_media = fuzz.trimf (x_calidad, [0, 5, 10]) 
calidad_alta = fuzz.trimf(x_calidad, [5, 10, 10])

servicio_bajo = fuzz.trimf(x_servicio, [0, 0, 5])
servicio_medio = fuzz. trimf(x_servicio, [0, 5, 10]) 
servicio_alto = fuzz.trimf(x_servicio, [5, 10,10])

propina_baja = fuzz.trimf(x_propina, [0, 0, 13])
propina_media = fuzz.trimf(x_propina, [0, 13, 25])  
propina_alta = fuzz.trimf(x_propina, [13, 25, 25])  
                                       
                                       
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))
ax0.plot(x_calidad, calidad_baja, 'b', linewidth=1.5, label='Mala') 
ax0.plot(x_calidad, calidad_media, 'g', linewidth=1.5, label='Aceptable')
ax0.plot(x_calidad, calidad_alta,'r', linewidth=1.5, label='Buena')
ax0.set_title('Calidad de la comida')
ax0.legend()

ax1.plot(x_servicio, servicio_bajo, 'b', linewidth=1.5, label='Malo')
ax1.plot(x_servicio, servicio_medio, 'g', linewidth=1.5, label='Aceptable')
ax1.plot(x_servicio, servicio_alto,'r', linewidth=1.5, label='Excelente')
ax1.set_title('Calidad del servicio')
ax1.legend()
               
ax2.plot(x_propina, propina_baja, 'b',linewidth=1.5, label='Bajo')
ax2.plot(x_propina, propina_media, 'g', linewidth=1.5, label='Medio')
ax2.plot(x_propina, propina_alta, 'r', linewidth=1.5, label='Alto')
ax2.set_title('Valor de la propina')
ax2.legend()
         
for ax in (ax0, ax1, ax2):
    ax.spines ['top'].set_visible(False)
    ax.spines ['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
plt.tight_layout()