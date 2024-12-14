import awscrt

# Create a TLS context
tls_context = awscrt.TlsContext()

# User-supplied CA certificate
user_ca_cert = "path/to/user_ca.pem"

# Improperly appending user CA to the default trust store
tls_context.add_ca_from_path(user_ca_cert)

# Establish a connection
mqtt_client = awscrt.mqtt.MqttClient(tls_context=tls_context)