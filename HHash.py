import hashlib
class hash():
    def __init__(self):
        try:
            def encrypt_string(hash_string):
                print(type(hashlib.sha256(hash_string.encode())))
                sha_signature = \
                    hashlib.sha256(hash_string.encode()).hexdigest()
                return sha_signature

            hash_string = input("Ingrese el nombre del archivo.")
            sha_signature = encrypt_string(hash_string)
            f=open("hashes.txt","a")
            f.write(hash_string)
            f.write(sha_signature)
            f.close()
            print(sha_signature)
        except:
            print("Error, vuelva a ejecutar el script")
