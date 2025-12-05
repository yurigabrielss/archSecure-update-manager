import subprocess

def run_yay_updates():
    result = subprocess.run(["yay", "-Qu"], capture_output=True, text=True)
    return result.stdout


