# rul-wrs
# Remaining Useful Life (RUL) Wire rope Shovel

# In order to start with the development:
# Para iniciar debe de instalar la ultima version de python y luego de pip.

# Para instalar las dependencias debe ejecutar el siguiente comando a nivel de la raiz del proyecto:
pip install -r requirements.txt

# Para ejecutar las pruebas use el siguiente comando a nivel del directorio src:
python -m pytest test/

# Para generar el instalador del servicio, ejecute este comando en la raiz del proyecto:
pyinstaller -F --hidden-import=win32timezone .\src\window_service.py

# Para instalar el servicio debe de abrir una consola cmd como administrador y ejecutar el siguiente
# archivo generado con el paso anterior: dist/window_service.exe
window_service.exe install
