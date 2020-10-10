import hashlib

message = input()

result = hashlib.sha256(message.encode())

print(result.hexdigest())