import subprocess
import shutil

def run_yay_updates():
    if shutil.which("yay") is None:
        raise SystemExit("Error: AUR helper 'yay' not found. ArchSecure currently requires yay to check for updates.")

    result = subprocess.run(["yay", "-Qu"], capture_output=True, text=True)
    return result.stdout

