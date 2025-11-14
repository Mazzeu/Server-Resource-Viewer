#!/usr/bin/env python3
from datetime import datetime
from zoneinfo import ZoneInfo
import psutil
import os

def main():
    time = get_system_data()
    print_banner(time)
    cpu_info()
    mem_ram_info()
    disk_info()

def cpu_info():
    logical_cpu = os.cpu_count() or 1
    physical_cpu = psutil.cpu_count(logical=False)
    cpu_usage_pct = psutil.cpu_percent(interval=1)
    print("\n--- Dados de uso de CPU ---")
    print(f"Núcleos de CPU Físicos = {physical_cpu}"
          f"\nNúcleos de CPU: Lógicos = {logical_cpu}"
          f"\nUso de CPU (%) = {cpu_usage_pct}%"
          )
    if cpu_usage_pct > 80:
        print("Aviso: Uso de CPU acima de 80%")

def mem_ram_info():
    virtual_mem = psutil.virtual_memory()
    ram_total_gb = virtual_mem.total / (1024 ** 3)
    ram_used_gb = (virtual_mem.total - virtual_mem.available) / (1024 ** 3)
    ram_used_pct = virtual_mem.percent
    print("\n--- Dados de uso de RAM ---")
    print(f"RAM Usada = {ram_used_gb:.3f} GB"
          f"\nRAM Total = {ram_total_gb:.3f} GB"
          f"\nRAM Usada (%) = {ram_used_pct:.2f}%"
          )
    if ram_used_pct > 80:
        print("Aviso: Uso de RAM acima de 80%")

def disk_info():
    disk_usage = psutil.disk_usage('/')
    disk_total_tb = disk_usage.total / (1024 ** 4)
    disk_used_tb = disk_usage.used / (1024 ** 4)
    disk_used_pct = disk_usage.percent
    print("\n--- Dados de uso de Disco ---")
    print(f"Espaço em Disco Usado = {disk_used_tb:.2f} TB"
          f"\nEspaço em Disco Total = {disk_total_tb:.2f} TB"
          f"\nEspaço em Disco Usado (%) = {disk_used_pct:.2f}%"
          )
    if disk_used_pct > 80:
        print("Aviso: Uso de Disco acima de 80%")

def get_system_data():
    # Tempo atual no formato RFC 3339 no TZ America/Sao_Paulo | Vai ser utilizado no banner e no logging
    current_time_with_tz = datetime.now(ZoneInfo("America/Sao_Paulo")).isoformat()
    return current_time_with_tz

def print_banner(current_time_with_tz, program_name: str = "Calculadora de Recursos do Servidor", width: int = 64) -> None:
    # Imprime um banner de inicialização com nome do programa, descrição e timestamp.
    # Centraliza o texto e garante que caiba na largura
    title = f" {program_name} "
    description = " Script para mostrar informações da CPU, RAM e Disco do Servidor"
    ts = f"Inicialização: {current_time_with_tz}"

    # limites - ajusta a largura se necessário
    if len(title) + 4 > width:
        width = len(title) + 4
    if len(description) + 4 > width:
        width = len(description) + 4
    if len(ts) + 4 > width:
        width = len(ts) + 4

    border = "+" + ("-" * (width - 2)) + "+"
    empty = "|" + (" " * (width - 2)) + "|"

    print(border)
    print(empty)
    print("|" + title.center(width - 2) + "|")
    print("|" + description.center(width - 2) + "|")
    print("|" + ts.center(width - 2) + "|")
    print(empty)
    print(border)

if __name__ == "__main__":
    main()
