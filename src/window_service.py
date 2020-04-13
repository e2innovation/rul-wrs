import servicemanager
import sys
import socket
import win32event
import win32service
import win32serviceutil
import os
<<<<<<< HEAD
import sys

from obtener_orquestador import ObtenerOrquestador 
=======
from acceso_configuracion import AccesoConfiguracion
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49

class WindowService(win32serviceutil.ServiceFramework):
    _svc_name_ = "RUL-WRS"
    _svc_display_name_ = "RUL-WRS Servicio Windows"
    _svc_description_ = "Este servicio monitorea la base de datos RUL-WRS para procesar informacion"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
<<<<<<< HEAD
        socket.setdefaulttimeout(60)
        self.ruta_aplicacion = os.path.dirname(sys.executable)
        ruta_archivo_configuracion = os.path.join(self.ruta_aplicacion, "config.json")
        self.orquestador = ObtenerOrquestador.obtener_orquestador(ruta_archivo_configuracion)

=======
        socket.setdefaulttimeout(120)
        
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        ruta_aplicacion = os.path.dirname(sys.executable)
        ruta_archivo_configuracion = os.path.join(ruta_aplicacion, "config.json")
        acceso_configuracion = AccesoConfiguracion(ruta_archivo_configuracion)
        configuracion = acceso_configuracion.obtener_configuracion("servicio_windows")
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
<<<<<<< HEAD
            with open('C:\\TestService.log', 'a') as f:
                f.write('data:\n')
                f.write(str(self.orquestador.obtener_equipos()))    
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
=======
            ruta_aplicacion = os.path.dirname(sys.executable)
            ruta_archivo_cli_exe = os.path.join(ruta_aplicacion, "cli.exe")
            os.startfile(ruta_archivo_cli_exe)
            rc = win32event.WaitForSingleObject(self.hWaitStop, configuracion["tiempo_espera_milisegundos"])
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(WindowService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(WindowService)