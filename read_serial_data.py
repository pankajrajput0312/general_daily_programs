import serial
serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=115200,
                            timeout=2)

while(1):
    print("thats ok")
    Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):
    print(serialPort.in_waiting > 0)
        Read data out of the buffer until a carraige return / new line is found
    serialString = serialPort.readline()
    print("serial_string", serialString)
    # Print the contents of the serial data
    print("decode", serialString.decode("ASCII"))

#     Tell the device connected over the serial port that we recevied the data!
#     The b at the beginning is used to indicate bytes!
    serialPort.write("Thank you for sending data \r\n")
