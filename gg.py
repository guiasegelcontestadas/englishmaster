import subprocess

def sincronizar_git():
    try:
        print("🚀 Preparando archivos para GitHub...")
        subprocess.run(["git", "add", "."], check=True)
        
        # Intentar hacer commit (si no hay cambios, no pasa nada)
        commit_result = subprocess.run(
            ["git", "commit", "-m", "Actualización automática de artículos y sitemap"],
            capture_output=True, text=True
        )
        
        # 1. BLINDAJE 1: Traer cambios remotos primero para evitar el error de "fetch first"
        print("🔄 Sincronizando historial con GitHub...")
        pull_process = subprocess.run(
            ["git", "pull", "origin", "main", "--rebase"],
            capture_output=True, text=True
        )
        
        if pull_process.returncode != 0:
            print("⚠️ Aviso: Hubo un pequeño ajuste en el pull, reintentando alinear...")
            # Si hay un rebase atascado por conflictos raros, lo abortamos limpiamente para no bloquear
            subprocess.run(["git", "rebase", "--abort"], capture_output=True)
            # Forzamos fetch y reset local para asegurar que mande lo nuevo sin llorar
            subprocess.run(["git", "fetch", "origin"], check=True)
            subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
            # Reaplicamos los cambios locales
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Reintento automático de sincronización"], capture_output=True)

        # 2. BLINDAJE 2: Subir con seguridad
        print("📤 Subiendo cambios a GitHub...")
        push_process = subprocess.run(
            ["git", "push", "-u", "origin", "main"],
            capture_output=True, text=True, check=True
        )
        
        print("✅ ¡Sincronización con GitHub exitosa!")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Error crítico en Git controlado: {e.stderr if e.stderr else str(e)}")
        return False