from env import MQTT_CLIENT_ID_ENV, MQTT_PASSWORD_ENV, MQTT_PORT_ENV, MQTT_SERVER_ADDRESS_ENV, MQTT_SSL_ENV, MQTT_USER_ENV, SSID_ENV, PASSWORD_ENV 

# ssid and password imported from env.py
secrets = {
    "ssid": SSID_ENV,
    "pw": PASSWORD_ENV
}

mqtt = {
    "server_address": MQTT_SERVER_ADDRESS_ENV, # mqtt server address here
    "port": MQTT_PORT_ENV,                     # port mqtt uses
    "user": MQTT_USER_ENV,                     # mqtt user name
    "password": MQTT_PASSWORD_ENV,             # mqtt password
    "client_id":MQTT_CLIENT_ID_ENV,            # raspberrypi2 pico unique id
    "ssl": True,                               # set to false if not using mosquitto local broker
    "topic_publish": "pico2/temp",             # For this example code keep the common topic for now since the JSON format below will report temperature reading
    "keep_alive": 7200,                        # TODO: ??? 
}
