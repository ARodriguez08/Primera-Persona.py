def update(ground_segments, camera, segment_size):
    player_position = camera.position
    
    # Mover y generar segmentos de suelo en el eje Z
    for segment in ground_segments:
        if segment.z < player_position.z - segment_size * 2:  # Si el segmento está muy detrás del jugador en Z
            segment.z += segment_size * 7  # Mueve el segmento al frente en Z
        
        # Remueve segmentos muy lejos en Z para evitar acumulación de memoria
        if segment.z > player_position.z + segment_size * 3:
            segment.z -= segment_size * 7

    # Mover y generar segmentos de suelo en el eje X
    for segment in ground_segments:
        if segment.x < player_position.x - segment_size * 2:  # Si el segmento está muy detrás del jugador en X
            segment.x += segment_size * 7  # Mueve el segmento al frente en X
        
        # Remueve segmentos muy lejos en X para evitar acumulación de memoria
        if segment.x > player_position.x + segment_size * 3:
            segment.x -= segment_size * 7
