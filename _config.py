# # Prod (Batch)
IS_BUILDING_DOCKER = False
IS_DEVELOPING      = False

# # Prod (Docker)
# IS_BUILDING_DOCKER = True
# IS_DEVELOPING      = False

# # Dev
# IS_BUILDING_DOCKER = False
# IS_DEVELOPING      = True

# Port
API_PORT = 8888
APP_PORT = 9999

# Host
API_HOST = "127.0.0.1"
APP_HOST = "127.0.0.1"
if IS_BUILDING_DOCKER:
    API_HOST = "0.0.0.0"
    APP_HOST = "0.0.0.0"
