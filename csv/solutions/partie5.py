import psutil
import datetime
import time

with open('ram_cpu.csv', 'wt') as f:
    f.write('date,heure,ram,cpu')
    for i in range(10):
        mem = psutil.virtual_memory()[2]
        cpu = psutil.cpu_times_percent()[0]
        maintenant = datetime.datetime.now()
        date_str = maintenant.strftime('%D')
        heure_str = maintenant.strftime('%T')
        enregistrement = '\n' + date_str + ',' + heure_str + ',' + str(mem) + ',' + str(cpu)
        f.write(enregistrement)
        time.sleep(3)
