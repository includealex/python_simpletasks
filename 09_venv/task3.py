from base64 import urlsafe_b64encode

sample_string = input()
sample_string_bytes = sample_string.encode("utf-8")

base64_bytes = urlsafe_b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("utf-8")

print(f"{base64_string}")
