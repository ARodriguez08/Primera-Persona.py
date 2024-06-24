from ursina import Entity

# Función para generar un nuevo segmento de suelo
def generate_ground_segment(x, z, segment_size):
    segment = Entity(model='plane', scale=(segment_size, 1, segment_size), texture='white_cube', texture_scale=(10, 10))
    segment.y = -0.5  # Ajusta la altura del suelo según sea necesario
    segment.x = x * segment_size  # Posición en el eje X multiplicado por el tamaño del segmento
    segment.z = z * segment_size  # Posición en el eje Z multiplicado por el tamaño del segmento
    segment.collider = 'box'  # Agrega un collider tipo caja para colisiones precisas
    return segment
