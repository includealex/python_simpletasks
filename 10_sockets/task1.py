import socket
import struct
from datetime import datetime, timezone, timedelta

def get_time_from_nist():
    server = "time.nist.gov"
    port = 37
    epoch_difference = (1970 - 1900) * 365 + (1970 - 1900) // 4

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(5)
            sock.sendto(b"", (server, port))
            data, _ = sock.recvfrom(4)
            timestamp = struct.unpack(">I", data)[0]
            unix_time = timestamp - epoch_difference * 86400
            current_time = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=unix_time)
            return current_time
    except socket.timeout:
        print("Error. Server didn't answer.")
    except Exception as e:
        print(f"Exception happened: {e}")

time = get_time_from_nist()
if time:
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
