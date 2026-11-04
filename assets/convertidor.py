import os
from pathlib import Path
from PIL import Image

# ==========================================
# CONFIGURACIÓN EXACTA
# ==========================================
CARPETA_ASSETS = Path(r"C:\Users\valen\Documents\EnglishMaster\assets")
MAX_WIDTH = 800  # Ancho máximo idéntico a tu app
QUALITY = 85     # Calidad WebP idéntica a tu app

def convertir_imagen(nombre_archivo):
    ruta_origen = CARPETA_ASSETS / nombre_archivo
    
    if not ruta_origen.exists():
        print(f"❌ No se encontró el archivo: {ruta_origen}")
        return

    # Si ya es webp y quieres procesarla de nuevo o cambiar tamaño, o ignorarla:
    ruta_destino = ruta_origen.with_suffix(".webp")

    try:
        with Image.open(ruta_origen) as img:
            img = img.convert("RGB")
            
            # Redimensionado proporcional con la misma lógica de tu app
            if img.width > MAX_WIDTH:
                propo = MAX_WIDTH / float(img.width)
                nuevo_alto = int(img.height * propo)
                img = img.resize((MAX_WIDTH, nuevo_alto), Image.Resampling.LANCZOS)
                print(f"📐 Redimensionada: {img.width}x{nuevo_alto}px")

            # Guardar con compresión WebP exacta
            img.save(ruta_destino, "WEBP", quality=QUALITY)
            print(f"✅ ¡Convertida! -> {ruta_destino.name}")
            
    except Exception as e:
        print(f"❌ Error al procesar {nombre_archivo}: {e}")

if __name__ == "__main__":
    print(f"📁 Buscando en: {CARPETA_ASSETS}\n")

    # OPCIÓN A: Si quieres convertir una sola imagen específica, descomenta la línea de abajo y pon su nombre:
    # convertir_imagen("mi_imagen_ejemplo.jpg")

    # OPCIÓN B: Si quieres barrer y convertir automáticamente TODAS las imágenes JPG, JPEG o PNG que estén en la carpeta assets:
    extensiones = ("*.png", "*.jpg", "*.jpeg")
    for ext in extensiones:
        for archivo in CARPETA_ASSETS.glob(ext):
            convertir_imagen(archivo.name)
            
    print("\n🏁 ¡Proceso finalizado!")