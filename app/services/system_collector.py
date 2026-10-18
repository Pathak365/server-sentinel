
import os
import psutil
import platform
import socket
from app.utils.decorators import measure_execution_time




class SystemCollector:

    @measure_execution_time
    def collector(self):
        cpu_uses = psutil.cpu_percent(1)
        memory_uses = psutil.virtual_memory().percent
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(socket.gethostname())
        

        operating_system = platform.system()

        if operating_system == "Windows":
            disk_path = os.environ.get("SystemDrive", "C:")
        else:
            disk_path = "/"

        disk_uses = psutil.disk_usage(disk_path).percent

        return {
            "cpu_uses": cpu_uses,
            "memory_uses": memory_uses,
            "disk_uses": disk_uses,
            "host_name" : hostname,
            "ip_address" : ip_address
        }

        



        


