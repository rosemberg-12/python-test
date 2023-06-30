
import base64
import typing

message= "rosemberg"

encoded_message= base64.b64encode(message.encode())

base64_message = encoded_message.decode()

print (base64_message)

