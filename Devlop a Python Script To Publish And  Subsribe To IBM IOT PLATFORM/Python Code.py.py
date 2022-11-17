import time
import sys
import ibmiotf.device
import random

organization="vh5b9d"
deviceType="Raspberry"
deviceId="0330"
authMethod="token"
authToken="123456789" 

try:
    deviceOptions={"org": organization,"type": deviceType,"id": deviceId,"auth-method": authMethod,"auth-token": authToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print("caught exception connecting device:%s" % str(e))
    sys.exit()
    
deviceCli.connect()    
while True:
         
          temp=random.randint(-20,125)
          hum=random.randint(0,100)
          haz=random.randint(1,100)
          pre=random.randint(0,100)
          data={'temperature':temp,'humidity':hum,'hazardous gas level':haz,'pressure':pre}
          def myOnPublishCallback():
            print("published temperature=%d" %temp,"humidity=%d" %hum,"pressure=%d" %pre,"hazardous gas level=%d" %haz, "to ibm watson")
          
        
          success=deviceCli.publishEvent("IotSensor","json",data,qos=0,on_publish=myOnPublishCallback)
          if not success:
              print("Not connected to IoTF")
          time.sleep(3)

               
deviceCli.disconnect()
