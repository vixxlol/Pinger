import socket
import time

def ping(host):
    # Create a new socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(1)

    start_time = time.time()

    try:
        s.connect((host, 80))

        end_time = time.time()

        elapsed_time = end_time - start_time

        print(f"Ping to {host} took {elapsed_time:.2f} seconds.")
    except socket.error:
        print(f"Could not connect to {host}.")
    finally:
        s.close()

print("Welcome! Enter the website you want to ping.")
host = input("> ")

print("Press CTRL+C to exit.")

while True:
	try:
	    ping(host)
	except KeyboardInterrupt:
		exit()