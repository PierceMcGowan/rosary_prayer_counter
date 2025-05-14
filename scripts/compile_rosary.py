import os
import subprocess
import platform
import shutil

def compile_executable(script_path, output_dir, target_os):
    """
    Compile a Python script into an executable for the specified OS.
    
    Args:
        script_path (str): Path to the Python script (e.g., start_rosary.py).
        output_dir (str): Directory to store the compiled executables.
        target_os (str): Target operating system ('windows' or 'linux').
    """
    try:
        # Check if the script exists
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script {script_path} not found!")

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Determine executable name based on target OS
        exe_name = "start_rosary"
        if target_os.lower() == "windows":
            exe_name += ".exe"

        # PyInstaller command
        pyinstaller_cmd = [
            "pyinstaller",
            "--onefile",  # Create a single executable file
            "--distpath", output_dir,  # Output directory
            "--name", exe_name,  # Name of the executable
            script_path  # Path to the script
        ]

        # Run PyInstaller
        print(f"Compiling {script_path} for {target_os}...")
        result = subprocess.run(pyinstaller_cmd, capture_output=True, text=True)

        # Check for errors
        if result.returncode != 0:
            print(f"Error compiling for {target_os}:")
            print(result.stderr)
            return False

        print(f"Successfully compiled {exe_name} for {target_os} in {output_dir}")
        return True

    except Exception as e:
        print(f"Error during compilation for {target_os}: {str(e)}")
        return False

def clean_up():
    """
    Clean up temporary files created by PyInstaller.
    """
    try:
        for folder in ["build", "__pycache__"]:
            if os.path.exists(folder):
                shutil.rmtree(folder)
        for file in ["start_rosary.spec"]:
            if os.path.exists(file):
                os.remove(file)
        print("Cleaned up temporary files.")
    except Exception as e:
        print(f"Error during cleanup: {str(e)}")

def main():
    # Configuration
    script_path = "scripts/start_rosary.py"  # Path to your Python script
    output_dir = "dist"  # Output directory for executables

    # Detect current OS
    current_os = platform.system().lower()
    print(f"Detected OS: {current_os}")

    # Compile for Windows
    if current_os == "windows":
        compile_executable(script_path, os.path.join(output_dir, "windows"), "windows")
    else:
        print("Skipping Windows compilation (not on Windows).")

    # Compile for Linux
    if current_os == "linux":
        compile_executable(script_path, os.path.join(output_dir, "linux"), "linux")
    else:
        print("Skipping Linux compilation (not on Linux).")

    # Clean up temporary files
    clean_up()

if __name__ == "__main__":
    main()