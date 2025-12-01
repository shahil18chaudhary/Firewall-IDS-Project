import os
import socket
import threading
import time
import json
import random

blocked_ips = set()
blocked_ports = set()
history = []

log_file = "firewall_logs.txt"
rule_file = "firewall_rules.json"

attack_ips = ["45.12.56.90","51.33.28.1","105.77.99.2","139.199.3.7","72.101.3.9","8.8.8.8"]
attack_ports = [21,22,23,25,53,80,135,139,443,445,8080,3306,9999]

def add_history(msg):
    history.append("• " + msg)
    if len(history) > 18:
        history.pop(0)

def clear():
    os.system("clear")

def save_rules():
    data = {"blocked_ips": list(blocked_ips), "blocked_ports": list(blocked_ports)}
    with open(rule_file, "w") as f:
        json.dump(data, f)

def log_event(msg):
    with open(log_file, "a") as f:
        f.write(msg + "\n")

# ---------- UI ----------
def draw_ui():
    clear()
    left = 60
    right = 60
    rows = 18

    print("┌" + "─"*left + " SELECT " + "─"*left + "┐", end="")
    print("    ┌" + "─"*right + " OUTPUT FIELD " + "─"*right + "┐")

    for i in range(rows):

        if i == 0:
            l = " 1 ► Block IP"
        elif i == 1:
            l = " 2 ► Block Port"
        elif i == 2:
            l = " 3 ► View Logs"
        elif i == 3:
            l = " 4 ► Honeypot View"
        elif i == 4:
            l = " 5 ► Attack Demo"
        elif i == 5:
            l = " 6 ► Combined Attack"
        elif i == 6:
            l = " 7 ► Dashboard"
        elif i == 7:
            l = " 8 ► Unblock IP"
        elif i == 8:
            l = " 9 ► Exit"
        elif i == 9:
            l = "10 ► Attack Flood Mode"
        else:
            l = ""

        l = l.ljust(left)
        r = history[i] if i < len(history) else ""
        r = r[:right].ljust(right)

        print(f"│ {l} │    │ {r} │")

    print("└" + "─"*(left*2+8) + "┘", end="")
    print("    └" + "─"*(right*2+8) + "┘")

# ---------- Firewall Functions ----------

def block_ip(ip):
    blocked_ips.add(ip)
    add_history(f"IP Blocked: {ip}")

def block_port(port):
    blocked_ports.add(port)
    add_history(f"Port Blocked: {port}")

def unblock_ip(ip):
    if ip in blocked_ips:
        blocked_ips.remove(ip)
        add_history(f"Unblocked: {ip}")
    else:
        add_history("Failed: IP not found")
        add_history("Solution: Use option 7 to see blocked IPs.")

def show_logs():
    add_history("Showing logs in terminal…")
    try:
        with open(log_file) as f:
            print(f.read())
    except:
        print("No logs.")
    input("\nPress Enter…")

def dashboard():
    add_history("Dashboard Opened")
    add_history(f"Blocked IPs: {list(blocked_ips)}")
    add_history(f"Blocked Ports: {list(blocked_ports)}")

def honeypot_view():
    add_history("Honeypot: Port 9999 catches suspicious connections.")

# ---------- Attack Simulations ----------

def random_ip_attack():
    ip = random.choice(attack_ips)
    add_history(f"Random IP Attack: {ip}")
    block_ip(ip)

def random_port_attack():
    port = random.choice(attack_ports)
    add_history(f"Random Port Attack: {port}")
    block_port(port)

def combined_attack():
    add_history("Combined Attack Triggered")
    random_ip_attack()
    time.sleep(0.2)
    random_port_attack()

def attack_flood():

    add_history("⚠ MASSIVE ATTACK STARTED")
    add_history("Attacks running…")


    ips = ["45.12.56.90","51.33.28.1","72.101.3.9","139.199.3.7","103.22.44.1"]
    ports = [80,443,445,8080,9999]

    # first show 5 ip attacks clearly
    for ip in ips:
        add_history(f"‼ IP Attack: {ip}")
        block_ip(ip)
        time.sleep(0.20)

    # then 5 port attacks clearly
    for p in ports:
        add_history(f"‼ Port Attack: {p}")
        block_port(p)
        time.sleep(0.20)

    # ADD FAILED EVENTS ------------------------------------
    add_history("⚠ Failed Attack: Port 9999 already in honeypot")
    add_history("Solution: Honeypot auto-blocks attacker IP.")

    add_history("⚠ Failed Attack: Binding to port 80 denied")
    add_history("Solution: Port already used by system services.")

    # BACKGROUND SPAM (not all visible)
    def spam():
        for _ in range(30):
            add_history(f"Background Attack {random.randint(100,999)}")
            time.sleep(0.05)

    threading.Thread(target=spam, daemon=True).start()

# ---------- Listening ----------

def handle_client(conn, addr, port):
    ip = addr[0]
    add_history(f"Conn {ip}:{port}")

    if ip in blocked_ips or port in blocked_ports:
        add_history(f"Blocked {ip}:{port}")
        conn.close()
        return
    
    if port == 9999:
        add_history(f"Honeypot Hit: {ip}")
        block_ip(ip)
        conn.close()
        return

    conn.close()

def start_listener(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind(("0.0.0.0", port))
        s.listen(5)
        add_history(f"Listening {port}")
    except:
        add_history(f"FAILED: Cannot bind port {port}")
        add_history("Solution: Stop other services or use a free port.")
        return

    while True:
        try:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr, port)).start()
        except:
            break

def start_listeners(ports):
    for p in ports:
        threading.Thread(target=start_listener, args=(p,), daemon=True).start()

# ---------- Menu ----------

def menu():
    while True:
        draw_ui()
        ch = input("\nChoose ▸ ")

        if ch == "1":
            block_ip(input("Enter IP: "))
        elif ch == "2":
            try:
                block_port(int(input("Enter Port: ")))
            except:
                add_history("Invalid port")
        elif ch == "3":
            show_logs()
        elif ch == "4":
            honeypot_view()
        elif ch == "5":
            random_ip_attack()
        elif ch == "6":
            combined_attack()
        elif ch == "7":
            dashboard()
        elif ch == "8":
            unblock_ip(input("Enter IP: "))
        elif ch == "9":
            add_history("Exiting…")
            break
        elif ch == "10":
            attack_flood()

if __name__ == "__main__":
    ports = [21,22,23,80,135,139,143,443,445,8080,3306,9999]
    add_history("Starting listeners…")
    start_listeners(ports)
    menu()
