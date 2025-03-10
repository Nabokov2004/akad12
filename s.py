import time
import subprocess

def get_arp_table():
    """Получение ARP-таблицы интерфейса eth0"""
    try:
        result = subprocess.run(['ip', 'neigh', 'show', 'dev', 'eth0'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Ошибка получения ARP-таблицы: {e}"

def arp_daemon():
    """Бесконечный цикл демона"""
    while True:
        print(get_arp_table(), flush=True)  
        time.sleep(60)

if __name__ == "__main__":
    arp_daemon()
