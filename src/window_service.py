import win32service
import win32serviceutil
import win32event
import servicemanager
import sys
import socket

class WindowService(win32serviceutil.ServiceFramework):
    _svc_name_ = "RUL-WRS"
    _svc_display_name_ = "RUL-WRS Servicio Windows"
    _svc_description_ = "Este servicio monitorea la base de datos RUL-WRS para procesar informacion"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
        socket.setdefaulttimeout(60)  

    def SvcStop(self):
        # tell the SCM we're shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # fire the stop event
        win32event.SetEvent(self.hWaitStop)

    # core logic of the service   
    def SvcDoRun(self):
        f = open('test.dat', 'w+')
        rc = None
        
        # if the stop event hasn't been fired keep looping
        while rc != win32event.WAIT_OBJECT_0:
            f.write('TEST DATA\n')
            f.flush()
            # block for 5 seconds and listen for a stop event
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
            
        f.write('SHUTTING DOWN\n')
        f.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(WindowService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(WindowService)