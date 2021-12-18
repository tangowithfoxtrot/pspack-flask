import socket
import time


def send(ip: str, port: int, file: str) -> None:
    for _ in range(3):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
            client.settimeout(3000)
            client.connect((ip, port))

            try:
                with open(file, "rb") as fp:
                    client.sendfile(fp)
            finally:
                client.close()
        except (ConnectionRefusedError, OSError):
            # Sometimes the socket isn't bound :(
            time.sleep(1)

