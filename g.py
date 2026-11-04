import subprocess
from pathlib import Path

# Ruta exactita de tu proyecto en Windows
RUTA_REPOS = Path(r"C:\Users\valen\Documents\EnglishMaster")

def subir_a_github(mensaje_commit="Sincronización inicial automática"):
    try:
        print("🚀 Preparando archivos para GitHub...")
        subprocess.run(["git", "add", "."], cwd=RUTA_REPOS, check=True)

        print("✍️ Guardando punto de control (commit)...")
        subprocess.run(["git", "commit", "-m", mensaje_commit], cwd=RUTA_REPOS)

        # 1. Traer y sincronizar cambios de GitHub primero para evitar rechazos
        print("📥 Sincronizando cambios remotos...")
        subprocess.run(["git", "pull", "origin", "main", "--rebase"], cwd=RUTA_REPOS)

        print("📤 Subiendo cambios a guiasegelcontestadas/englishmaster...")
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=RUTA_REPOS, check=True)

        print("🎉 ¡Sincronizado con GitHub exitosamente!")
        return True

    except Exception as e:
        print(f"❌ Error al subir a GitHub: {e}")
        return False

if __name__ == "__main__":
    subir_a_github("Actualización automática desde Python")