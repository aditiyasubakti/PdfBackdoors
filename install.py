import os
import subprocess
import sys

def create_virtual_env(env_name='myenv'):
    # Membuat virtual environment
    subprocess.check_call([sys.executable, '-m', 'venv', env_name])
    print(f"Virtual environment '{env_name}' telah dibuat.")

def activate_virtual_env(env_name='myenv'):
    # Mengaktifkan virtual environment
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(env_name, 'Scripts', 'activate')
    else:  # macOS/Linux
        activate_script = os.path.join(env_name, 'bin', 'activate')
    
    # Menampilkan cara mengaktifkan virtual environment
    print(f"\nUntuk mengaktifkan virtual environment, jalankan:\nsource {activate_script}")

def install_dependencies(env_name='myenv'):
    # Menginstal pikepdf di dalam virtual environment
    pip_executable = os.path.join(env_name, 'bin', 'pip') if os.name != 'nt' else os.path.join(env_name, 'Scripts', 'pip')
    subprocess.check_call([pip_executable, 'install', 'pikepdf'])
    print("Pustaka 'pikepdf' telah diinstal.")

def run_pdf3_script():
    # Menjalankan file pdf3.py
    subprocess.check_call(['python3', 'pdf3.py'])

if __name__ == '__main__':
    create_virtual_env()
    activate_virtual_env()
    install_dependencies()
    run_pdf3_script()
