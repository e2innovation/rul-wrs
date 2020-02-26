import servicemanager
import sys
import socket
import win32event
import win32service
import win32serviceutil
import os
import sys

from obtener_orquestador import ObtenerOrquestador 

class WindowService(win32serviceutil.ServiceFramework):
    _svc_name_ = "RUL-WRS"
    _svc_display_name_ = "RUL-WRS Servicio Windows"
    _svc_description_ = "Este servicio monitorea la base de datos RUL-WRS para procesar informacion"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
        socket.setdefaulttimeout(60)
        self.ruta_aplicacion = os.path.dirname(sys.executable)
        ruta_archivo_configuracion = os.path.join(self.ruta_aplicacion, "config.json")
        self.orquestador = ObtenerOrquestador.obtener_orquestador(ruta_archivo_configuracion)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            with open('C:\\TestService.log', 'a') as f:
                f.write('data:\n')
                f.write(str(self.orquestador.obtener_equipos()))    
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(WindowService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(WindowService)