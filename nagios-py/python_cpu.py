#! /usr/bin/env python3.8
import psutil
import configparser
import logging

logging.basicConfig(filename='cpupy.log', filemode='w', level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('pycpu.ini')

crit = int(config["cpu"]["critical"])
warn = int(config["cpu"]["warning"])
#print(crit, warn)
def send_alert(a):
    if a > crit:
        logging.critical("Sending Sev0 alert")
    if a > warn and a < crit:
        logging.warning("Sending Sev1 alert")


def usage():
    total_cpu_use = psutil.cpu_percent(interval=1, percpu=False)
    if total_cpu_use > crit:
        logging.critical(f"Current usage is {total_cpu_use}")
        send_alert(total_cpu_use)
    elif total_cpu_use > warn and total_cpu_use < crit:
        logging.warning(f"Current usage is {total_cpu_use}")
        send_alert(total_cpu_use)
    else:
        logging.info(f"Current usage is {total_cpu_use}, INFO")


def main():
    usage()

if __name__ == '__main__':
  main()
