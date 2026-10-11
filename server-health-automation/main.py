import psutil

def check_health(usage, threshold):
    if usage > threshold:
        return "WARNING"
    else:
        return "HEALTHY"


cpu_percent = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage('C:\\')

cpu_status = check_health(cpu_percent, 80)
memory_status = check_health(memory_info.percent, 80)
disk_status = check_health(disk_info.percent, 90)

print(f"CPU Usage: {cpu_percent}%")
print(f"Memory Usage: {memory_info.percent}%")
print(f"Disk Usage: {disk_info.percent}%")

print(f"CPU Status: {cpu_status}")
print(f"Memory Status: {memory_status}")
print(f"Disk Status: {disk_status}")