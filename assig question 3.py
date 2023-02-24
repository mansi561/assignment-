from keycloak import KeycloakOpenID
keycloak_openid = KeycloakOpenID(server_url="https://your-keycloak-server-url/auth/",
                                 realm_name="your-realm",
                                 client_id="your-client-id",
                                 client_secret_key="your-client-secret-key")
username = "user@example.com"
password = "user-password"
token = keycloak_openid.token(username=username, password=password)
access_token = token["access_token"]
refresh_token = token["refresh_token"]
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get("https://your-api-endpoint", headers=headers)