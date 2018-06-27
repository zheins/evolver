class Reading:

    def __init__(self, OD, temp):
    
      self.OD = OD
      self.temp = temp
      
class ReadingData: 

    CONST_VIAL = 14
    
    def __init__(self, OD, temp):
    
      self.reading = Reading(OD, temp)
      
    def __str__(self):
        return "od: " + str(self.reading.OD) + "-temp: " + str(self.reading.temp)
       

class ReadingResponse:

    CONST_UNIT_NUMBER = 1
    CONST_EXPERIMENT_ID = "b24ebdc3-cd07-4eca-8ef9-2e65516da297"
    
    def __init__(self, readingNumber, readingData, timeStamp):
        
        self.readingNumber = readingNumber
        self.readingData = readingData
        self.timeStamp = timeStamp
    
     
    def __str__(self):
       
       result = "{" + "\"" + "deviceId\":"   + str(self.CONST_UNIT_NUMBER) + "," + "\"" +  "readingNumber\":" + "\"" + str(self.readingNumber) + "\"" 
       + ","  +  "\"data\":[{\"vial\":" + str(ReadingData.CONST_VIAL) + ",\"readings\":{\"od\":" + str(self.readingData.reading.OD) 
       + ",\"temp\":"+ str(self.readingData.reading.temp) + "}}],\"timeStamp\":"+ self.timeStamp + "," + "\"experimentId\":" "\"" + self.CONST_EXPERIMENT_ID + "\"" + "}"
       return result 
       
class Event:
    
    def __init__(self, name, message):
    
        self.name = name
        self.message = message
        
class EventData:
    
    CONST_VIAL = 14 
    
    def __init__(self, name, message):
    
        self.event = Event(name, message)
    
class EventResponse:
    
    CONST_UNIT_NUMBER = 1
    CONST_EXPERIMENT_ID = "b24ebdc3-cd07-4eca-8ef9-2e65516da297"
    
    def __init__(self, startTime, endTime, eventData, timeStamp, eventNumbr, name, message):
        
        self.startTime = startTime
        self.endTime = endTime
        self.eventData = EventData(name, message)
        self.timeStamp = timeStamp
        self.eventNumber = eventNumber

