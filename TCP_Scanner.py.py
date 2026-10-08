import socket
from concurrent.futures import ThreadPoolExecutor
def scan(t):
    s=socket.socket(); s.settimeout(0.5)
    try: s.connect(t); print(f"[OPEN] {t[0]}:{t[1]}")
    except: pass
    finally: s.close()
target="127.0.0.1"; ports=range(1,1025) # CHANGE to authorized target only
with ThreadPoolExecutor(100) as ex: ex.map(scan, [(target,p) for p in ports])