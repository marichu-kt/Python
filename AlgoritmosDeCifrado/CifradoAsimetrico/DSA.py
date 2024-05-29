from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Generar par de claves DSA
key = DSA.generate(2048)

# Mensaje a firmar
message = b"Este es un mensaje de ejemplo para firmar con DSA"

# Crear un objeto hash
hash_obj = SHA256.new(message)

# Crear un objeto de firma
signer = DSS.new(key, 'fips-186-3')

# Firmar el mensaje
signature = signer.sign(hash_obj)

# Verificar la firma
verifier = DSS.new(key, 'fips-186-3')
try:
    verifier.verify(hash_obj, signature)
    print("La firma es válida.")
except ValueError:
    print("La firma no es válida.")
