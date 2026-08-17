import subprocess
import platform

# List of servers/websites to monitor
TARGET_HOSTS = ["google.com", "aws.amazon.com", "1.1.1.1"]

def ping_host(host):
    # Determine the operating system command parameter (-n for Windows, -c for Linux/Mac)
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    
    # Execute system ping without displaying raw output in console
    response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response.returncode == 0

def run_uptime_check():
    print("--- SYSTEM INFRASTRUCTURE UPTIME MONITOR ---")
    for host in TARGET_HOSTS:
        is_online = ping_host(host)
        status = "ONLINE [✓]" if is_online else "OFFLINE [X]"
        print(f"Host: {host:<20} | Status: {status}")

if __name__ == "__main__":
    run_uptime_check()