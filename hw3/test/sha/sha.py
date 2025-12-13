import hashlib

data = "hello world".encode("utf-8")

# SHA-1
sha1 = hashlib.sha1(data).hexdigest()
print("SHA-1:", sha1)

# SHA-256
sha256 = hashlib.sha256(data).hexdigest()
print("SHA-256:", sha256)

# SHA-512
sha512 = hashlib.sha512(data).hexdigest()
print("SHA-512:", sha512)

# SHA3-256
sha3_256 = hashlib.sha3_256(data).hexdigest()
print("SHA3-256:", sha3_256)

# SHAKE256 (64 bytes)
shake = hashlib.shake_256(data).hexdigest(64)
print("SHAKE-256 (64 bytes):", shake)
