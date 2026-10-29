import json
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

# Ruta a tus credenciales e información de endpoint
CREDENTIALS_FILE = "credenciales.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

def enviar_url_a_indexar(url_articulo):
    try:
        # Cargar credenciales desde el archivo json
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE, scopes=SCOPES
        )
        
        # Construir el cliente de la API
        service = build('indexing', 'v3', credentials=credentials)
        
        # Cuerpo de la petición
        body = {
            "url": url_articulo,
            "type": "URL_UPDATED"  # Le avisa a Google que la URL fue creada o actualizada
        }
        
        # Ejecutar la solicitud
        print(f"🚀 Enviando orden de indexación para: {url_articulo}")
        request = service.urlNotifications().publish(body=body)
        response = request.execute()
        
        print("✅ Google confirmó la recepción con éxito:")
        print(json.dumps(response, indent=2))
        return True

    except Exception as e:
        print(f"❌ Error al notificar a Google: {e}")
        return False

if __name__ == "__main__":
    # Cambia esto por una URL real de tu sitio
    url_de_prueba = "https://quantumaudiostudio.com/"
    enviar_url_a_indexar(url_de_prueba)