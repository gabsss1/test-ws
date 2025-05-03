import requests
import os

# ID del capítulo (este es el que pasaste)
chapter_id = "9d1608fa-b0f6-4faf-97c4-aa7bc4f2ba3a"

# Paso 1: Obtener servidor de imágenes y datos del capítulo (At-Home API)
server_response = requests.get(f"https://api.mangadex.org/at-home/server/{chapter_id}")
server_data = server_response.json()

base_url = server_data['baseUrl']
chapter_hash = server_data['chapter']['hash']
page_filenames = server_data['chapter']['data']

# Crear carpeta para guardar las imágenes
output_dir = f"mangadex_chapter_{chapter_id}"
os.makedirs(output_dir, exist_ok=True)

# Paso 2: Descargar cada imagen
for i, filename in enumerate(page_filenames, start=1):
    image_url = f"{base_url}/data/{chapter_hash}/{filename}"
    print(f"Descargando página {i}: {image_url}")
    
    try:
        img_data = requests.get(image_url).content
        with open(os.path.join(output_dir, f"page_{i:03}.jpg"), "wb") as f:
            f.write(img_data)
    except Exception as e:
        print(f"Error al descargar {image_url}: {e}")

print(f"\n✅ {len(page_filenames)} imágenes descargadas en la carpeta '{output_dir}'")