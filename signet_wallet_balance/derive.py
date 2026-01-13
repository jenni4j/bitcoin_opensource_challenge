import hmac, hashlib
from decode import private_key, chain_code

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

def hmac_sha512(key, msg):
    return hmac.new(key, msg, hashlib.sha512).digest()

def derive_child(k_parent, c_parent, index):
    data = b'\x00' + k_parent + index.to_bytes(4, 'big')

    I = hmac_sha512(c_parent, data)
    IL, IR = I[:32], I[32:]

    child_key = (int.from_bytes(IL, 'big') + int.from_bytes(k_parent, 'big')) % N
    return child_key.to_bytes(32, 'big'), IR

mk = private_key
mc = chain_code

path = [
    86 | 0x80000000,
    1  | 0x80000000,
    0  | 0x80000000,
    0
]

for index in path:
    mk, mc = derive_child(mk, mc, index)

branch_private_key = mk
branch_chain_code  = mc

wallet_keys = []

k = branch_private_key
c = branch_chain_code

for i in range(2000):
    child_key, _ = derive_child(k, c, i)
    wallet_keys.append(child_key)

print("Branch Chain code:", branch_chain_code.hex())
print("Branch Private key:", branch_private_key.hex())
print("Example wallet key:", wallet_keys[0].hex())
print("Example wallet key:", wallet_keys[1].hex())
