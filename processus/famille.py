import os
import time

# Récupération du PID du programme principal
pid_actuel = os.getpid()
print(f"--- Lancement du programme (PID: {pid_actuel}) ---")

# Création d'un processus fils via os.fork()
# fork() renvoie 0 dans le fils et le PID du fils dans le père.
n = os.fork()

if n > 0:
    # Code exécuté par le PÈRE
    print(f"[PÈRE] Mon PID est {os.getpid()}. Mon fils a le PID {n}")
    print("[PÈRE] J'attends 60 secondes...")
    time.sleep(60)
else:
    # Code exécuté par le FILS
    print(f"[FILS] Mon PID est {os.getpid()}. Mon père est le PID {os.getppid()}")
    print("[FILS] J'attends 60 secondes...")
    time.sleep(60)

print(f"Fin du processus {os.getpid()}")
