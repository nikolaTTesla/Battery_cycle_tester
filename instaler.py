import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed',
    '--icon=logo.icns',
    '--noconsole',
    '--name=Battery_Cycle_Data_Aquisition'
])

