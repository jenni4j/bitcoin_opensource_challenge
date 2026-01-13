import base58
import binascii

tprv = "tprv8ZgxMBicQKsPe7MSPjA62MmGvsYv8cz6UzxVVY7DzcUeoxGsxeELFRe6KXHnYVKT27wL8t2kdM6pzgEqveUYeduKL8u92vi6DDE3MAthM7x"

raw = base58.b58decode_check(tprv)

print(len(raw))      # should be 78 bytes
print(binascii.hexlify(raw))

version = raw[0:4]
depth = raw[4]
parent_fpr = raw[5:9]
child_number = raw[9:13]
chain_code = raw[13:45]
key_data = raw[45:78]
private_key = key_data[1:]

print("Version:", version.hex())
print("Depth:", depth)
print("Parent fingerprint:", parent_fpr.hex())
print("Child number:", int.from_bytes(child_number, 'big'))
print("Chain code:", chain_code.hex())
print("Private key:", private_key.hex())