import subprocess
from pathlib import Path

# Ruta exactita de tu proyecto en Windows
RUTA_REPOS = Path(r"C:\Users\valen\Documents\EnglishMaster")

def subir_a_github(mensaje_commit="Sincronización inicial automática"):
    try:
        print("🚀 Preparando archivos para GitHub...")
        subprocess.run(["git", "add", "."], cwd=RUTA_REPOS, check=True)

        print("✍️ Guardando punto de control (commit)...")
        # Si no hay cambios nuevos, el commit avisará pero continuará
        subprocess.run(["git", "commit", "-m", mensaje_commit], cwd=RUTA_REPOS)

        print("📤 Subiendo cambios a guiasegelcontestadas/englishmaster...")
        # Aseguramos subir a la rama main
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=RUTA_REPOS, check=True)

        print("🎉 ¡Sincronizado con GitHub exitosamente!")
        return True

    except Exception as e:
        print(f"❌ Error al subir a GitHub: {e}")
        return False

if __name__ == "__main__":
    subir_a_github("Prueba de envío automático desde Python")