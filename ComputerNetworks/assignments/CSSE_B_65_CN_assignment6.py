import math
import ipaddress

def calculate_subnet(network_cidr, required_hosts):
    network = ipaddress.IPv4Network(network_cidr, strict=False)

    # Step 1: Calculate host bits needed
    host_bits = math.ceil(math.log2(required_hosts + 2))

    # Step 2: Calculate new prefix
    new_prefix = 32 - host_bits

    if new_prefix < network.prefixlen:
        raise ValueError("Not enough address space for requested hosts")

    # Step 3: Generate subnets
    subnets = list(network.subnets(new_prefix=new_prefix))

    return {
        "Original Network": str(network),
        "Required Hosts": required_hosts,
        "Host Bits": host_bits,
        "New Subnet Mask": str(ipaddress.IPv4Network(f"0.0.0.0/{new_prefix}").netmask),
        "CIDR Notation": f"/{new_prefix}",
        "Total Subnets": len(subnets),
        "Subnets": [str(subnet) for subnet in subnets]
    }


result = calculate_subnet("192.168.1.0/24", 50)

for key, value in result.items():
    if key == "Subnets":
        print(f"{key}:")
        for s in value:
            print(f"  {s}")
    else:
        print(f"{key}: {value}")