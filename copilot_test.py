import os
import platform
import time

def get_uptime():
    if platform.system() == "Windows":
        # On Windows, use uptime from system boot time
        import ctypes
        import datetime
        kernel32 = ctypes.windll.kernel32
        uptime_ms = kernel32.GetTickCount64()
        uptime_sec = int(uptime_ms / 1000)
    else:
        # On Unix-like systems, read /proc/uptime
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_sec = int(float(f.readline().split()[0]))
        except FileNotFoundError:
            # Fallback for systems without /proc/uptime (e.g., macOS)
            uptime_sec = int(time.time() - os.stat('/').st_ctime)
    return uptime_sec

def format_uptime(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{days}d {hours}h {minutes}m {seconds}s"

if __name__ == "__main__":
    uptime = get_uptime()
    print(f"System uptime: {format_uptime(uptime)}")
