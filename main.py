from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ground_generator import generate_ground_segment
import movement_logic

# Configuración inicial de Ursina
app = Ursina()

# Lista para almacenar los segmentos de suelo
ground_segments = []

# Tamaño de los segmentos de suelo
segment_size = 20  # Ajusta el tamaño según sea necesario

# Generar los primeros segmentos de suelo
for z in range(-3, 4):  # Genera segmentos en el eje Z desde -3 hasta 3
    for x in range(-3, 4):  # Genera segmentos en el eje X desde -3 hasta 3
        ground_segment = generate_ground_segment(x, z, segment_size)
        ground_segments.append(ground_segment)

# Crea una cámara para la vista en primera persona
camera = FirstPersonController()

# Función para mover y generar nuevos segmentos de suelo cuando sea necesario
def update():
    global ground_segments, camera, segment_size
    # Llama a la función update definida en movement_logic.py
    movement_logic.update(ground_segments, camera, segment_size)

# Ejecuta la aplicación de Ursina
app.run()
