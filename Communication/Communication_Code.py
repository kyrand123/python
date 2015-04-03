import time, serial, mosquitto                                          # imports the required functions, serial allows us to send data down the serial cable to the arduino and mosquitto allows us to suscribe and listening for information across the network 

def messageReceived(broker, obj, msg):                                  # creates a function that 
    global ser                                                          # allows the serial to be global
    print("Message " + msg.topic + " containing: " + msg.payload)       # prints on screen the message recieved from mosquitto, allowing us to get the information to write to the serial.
    if msg.payload == 'ON': ser.write("1")                              # listens to see if the payload is on and writes 1 to the arduino which will turn on the onboard light. 
    else : ser.write("0")                                               # if the payload is not on then the light will stay turned off


client = mosquitto.Mosquitto("45748745876")                             # creates my user id
client.connect("141.163.83.78")                                         #connects to the clients IP address
client.subscribe("lights")                                              # suscribes to "lights", meaning we listen for anything from this suscription
client.on_message = messageReceived

ser = serial.Serial("/dev/cu.usbmodem14611",9600,timeout=2)             # creates the serial communication speed for the arduino

while True: client.loop()                                               #loops through the client function constantly listening for changes.
