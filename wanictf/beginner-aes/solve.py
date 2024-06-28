from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import hashlib

# Given encrypted data and original key/iv with appended bytes
enc = b'\x16\x97,\xa7\xfb_\xf3\x15.\x87jKRaF&"\xb6\xc4x\xf4.K\xd77j\xe5MLI_y\xd96\xf1$\xc5\xa3\x03\x990Q^\xc0\x17M2\x18'  # Example encrypted data
original_key = b'the_enc_key_is_'
original_iv = b'my_great_iv_is_'

# Original flag and its hash
flag_hash = "6a96111d69e015a07e96dcd141d31e7fc81c4420dbbef75aef5201809093210e"

# Brute-force through all possible key and iv combinations
for key_byte in range(256):
    for iv_byte in range(256):
        # Append the guessed byte to the original key and iv
        key = original_key + bytes([key_byte])
        iv = original_iv + bytes([iv_byte])

        # Create AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)

        try:
            # Decrypt the encrypted data
            decrypted_data = cipher.decrypt(enc)

            # Unpad the decrypted data
            plaintext = unpad(decrypted_data, AES.block_size)

            # Calculate SHA-256 hash of the plaintext
            sha256_hash = hashlib.sha256(plaintext).hexdigest()

            # Compare with original flag hash
            if sha256_hash == flag_hash:
                print(f"Decrypted flag: {plaintext.decode('utf-8')}")
                print(f"Guessed Key: {key}")
                print(f"Guessed IV: {iv}")
                break  # Exit the loop if flag is found

        except ValueError:
            # Incorrect decryption (padding error), continue to next key/iv combination
            continue

    else:
        continue  # Continue outer loop if flag not found
    break  # Exit outer loop if flag is found