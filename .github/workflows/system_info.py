import platform
import psutil
import socket

def get_system_info():
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores (Physical)": psutil.cpu_count(logical=False),
        "CPU Cores (Logical)": psutil.cpu_count(logical=True),
        "Total RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
    }

    return info

def display_info(info):
    print("\nSystem Information:")
    print("-" * 30)
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    system_info = get_system_info()
    display_info(system_info)
