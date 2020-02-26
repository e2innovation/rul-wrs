
<p align="center"><img src="http://www.e2i.com.pe/images/E2I.png" width="196px"><p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![GitHub issues](https://img.shields.io/github/issues-raw/e2innovation/rul-wrs)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/e2innovation/rul-wrs)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![GitHub pull requests](https://img.shields.io/github/issues-pr/e2innovation/Proyecto1_GD)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

# Remaining useful life (Rul) Wire rope shovel (wrs)
### [Rul-wrs]

Para iniciar se debe instalar la ultima versión de **Python** y luego **pip**.

Para instalar las dependencias debe ejecutar el siguiente comando a nivel de la raíz del proyecto:  
``
pip install -r requirements.txt
``

<<<<<<< HEAD
Para ejecutar las pruebas use el siguiente comando a nivel del directorio *src*:    
``
python -m pytest test/
``
=======
# Para ejecutar las pruebas use el siguiente comando a nivel del directorio src:
python -m pytest -v test/
>>>>>>> Agregar detector de ciclos

Para generar el instalador del servicio, ejecute este comando en la raíz del proyecto:  
```
pyinstaller -F --hidden-import=win32timezone .\src\window_service.py
```

Para instalar el servicio debe de abrir una consola *cmd* como administrador y ejecutar el siguiente archivo generado con el paso anterior:
**dist/window_service.exe**
```
window_service.exe install
```
