from picamera2 import Picamera2
import time
import io

# Inicializa la cámara
camera = Picamera2()

# Configura la resolución de la cámara
camera_config = camera.create_still_configuration(main={"size": (800, 600)})
camera.configure(camera_config)

# Arranca la cámara
camera.start()

# Espera un poco para asegurarse de que la cámara esté lista
time.sleep(2)

# Captura la imagen en un buffer en memoria
image_path = 'captura_imagen.jpg'
camera.capture_file(image_path, format='jpeg')
sleep(1)
camera.capture_file(image_path, format='jpeg')
# Detén la cámara
camera.stop()

# Imprime la ruta del archivo guardado
print(f"Imagen guardada en: {image_path}")
