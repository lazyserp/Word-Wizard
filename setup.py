import subprocess
import sys
import os

def install_requirements():
    # Install Python packages
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])
    
    # Download and setup ChromeDriver
    try:
        import urllib.request
        import zipfile
        
        # Get Chrome version
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
        version = winreg.QueryValueEx(key, 'version')[0].split('.')[0]
        
        # Download matching ChromeDriver
        url = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{version}"
        driver_version = urllib.request.urlopen(url).read().decode()
        driver_url = f"https://chromedriver.storage.googleapis.com/{driver_version}/chromedriver_win32.zip"
        
        # Download and extract
        urllib.request.urlretrieve(driver_url, "chromedriver.zip")
        with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("chromedriver.zip")
        
        # Add to PATH
        os.environ["PATH"] += os.pathsep + os.getcwd()
        
        print("Setup completed successfully!")
        
    except Exception as e:
        print(f"Error during setup: {e}")

if __name__ == "__main__":
    install_requirements()