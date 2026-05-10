import requests
from requests_gssapi import HTTPKerberosAuth

# Setup Kerberos authentication
# mutual_authentication=REQUIRED is the default and recommended for security
kerberos_auth = HTTPKerberosAuth()

# Make the request to a Kerberos-protected endpoint
response = requests.get("http://example.com", auth=kerberos_auth)

print(f"Status Code: {response.status_code}")
print(response.text)
