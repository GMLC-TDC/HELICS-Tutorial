import os
import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipaddr = s.getsockname()[0]

CURDIR = os.path.realpath(os.path.dirname(__file__))

def main(broker="broker"):

    for root, _, filenames in os.walk(os.path.join(CURDIR, "../../test_system_data/gldFeeders/")):
        for filename in filenames:
            if filename.endswith(".json"):
                with open(os.path.join(root, filename)) as f:
                    data = json.loads(f.read())
                    data["core_init_string"] = "--federates=1 --broker_address=tcp://{broker} --interface=tcp://{ipaddr} --localport=23500".format(broker=broker, ipaddr=ipaddr)
                with open(os.path.join(root, filename), "w") as f:
                    f.write(json.dumps(data, sort_keys=True, indent=2, separators=(",", ": ")))

if __name__ == "__main__":

    import sys
    try:
        broker = sys.argv[1]
    except:
        broker = "broker"

    main(broker)
