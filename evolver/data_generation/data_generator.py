import random


class ReadingGenerator:
    
    #this is the threshold value for optical density
    CONST_PICK_VALUE = 0.5;

    #this is the probability of happening an event after a reading is done
    CONST_EVENT_PROBABILITY = 0.5;

    #this is the probability of an event to be PUMP, ( not OD SET )
    CONST_PUMP_PROBABILITY = 0.5;

    #this is the difference between start time and end time of an event in seconds
    CONST_EVENT_DURATION = 60;

    #device is reading the data every 45 seconds.
    CONST_TIME_INTERVALS = 45;

    #after value of OD reaches its pick,value of OD is decreased by this drop value.
    #this value is set based on the static data
    CONST_DROP_VALUE = 0.35932;

    #this is the probability of OD values to decrease at a certain point
    CONST_LOCALLY_DECREASING_PROBABILITY = 0.5;
    #this is the probability of having Jags on the OD graph
    CONST_JAGGING_PROBABILITY = 0.6;

    #magnitude of our jags on OD graph is controled by the following 2 constants
    CONST_JAGGING_COEFFICIENT = 2.5;
    CONST_JAGGING_CONSTANT = 0.002;

    #this coefficient controls the magnitude of step with a negative sign
    CONST_DECREASING_STEP_COEFFICIENT = 0.01;

    #values of the following constatnts are extracted from the data we had
    CONST_STARTING_READING_NUM = 128321;
    CONST_ENDING_READING_NUM = 128395;
    CONST_MINOD = 0.456266772509;
    CONST_MAXOD = 0.510805834559;
    CONST_MAXTEMP = 30.00536;
    CONST_MINTEMP = 29.78774;
    CONST_READING_NUMBER = "128321";
    #private static final String READING_NUMBER = "129121";
    CONST_EVENT_NUMBER = "0";


    #number of records in original data set is roughly 730 but doing 730 insertions in a row
    #results in mongoSocketReadException
    CONST_NUM_RECORDS = 500;

    
    CONST_LOWER_TEMPlIMIT = 29.8;
    CONST_UPPER_TEMPlIMIT = 29.88;

    #this is the initial value for optical density
    OD = 0.456266772509;
    #this is the initial value for temperature
    temp = 29.78774;

    #private static Date timeStamp;

    #this value will be set to true if OD reaches its threshold
    reachedPick = False;

    #this value will be set to true when the value of temperature increases
    increased = False;

    #this value specifies the number of times in a row  we want to keep the temperature fixed.
    #in the original data set, temperature doesn't change at some certain points.
    #I can set its value to a randomly created integer! right now its value is set based on the results I got
    numFixed = 200;
    
    def tempStepSizeUpperLimit(self):

        stepSizeUpperLimit = ((self.CONST_MAXTEMP - self.CONST_MINTEMP)/(self.CONST_ENDING_READING_NUM - self.CONST_STARTING_READING_NUM));
        return stepSizeUpperLimit;
    
    def generateRandomStepSize(self,upperLimit):
        return  (random.random() * upperLimit);
        
        
    def  generateRandomTemp(self):

        upperLimit = self.tempStepSizeUpperLimit();

        if random.random() < 0.3 :

            self.temp = self.temp + self.generateRandomStepSize(upperLimit) + 0.1;
            self.increased = True;
        

        elif random.random() > 0.3 and random.random() < 0.9:

            self.temp = self.temp - 200*self.generateRandomStepSize(upperLimit) + 0.1;
            self.increased = False;
        

        if self.numFixed == 0:
            if (random.random() > 0.9):
                self.temp = self.temp - self.generateRandomStepSize(upperLimit) +1;
                return self.temp
            
            else:
               self.temp = self.temp + self.generateRandomStepSize(upperLimit);
               return self.temp
            
        

        #we don't want to fix the value exactly right after we have an increase in value
        #that's why we check the value of increased to see if it's false
        if self.numFixed > 0 and self.increased == False:

            self.numFixed = self.numFixed - 1;
            #this is the temperature around which temp graph is jagging.
            #this value is extracted from the static data set we had
            self.temp = 29.9;
            return self.temp;
        

        #if we have a an increase in our values we reset the value of numFixed to its original value
        if self.increased:
            self.numFixed = 200;
        

        return self.temp;
        
    def getStepSizeUpperLimit():
        
        stepSizeUpperLimit = ((self.CONST_MAXOD - self.CONST_MINOD)/(self.CONST_ENDING_READING_NUM - self.CONST_STARTING_READING_NUM));
        
        if random.random() < self.CONST_JAGGING_PROBABILITY:
            return (self.CONST_JAGGING_COEFFICIENT * stepSizeUpperLimit) + self.CONST_JAGGING_CONSTANT;
        
        else:
           return stepSizeUpperLimit;
        
    
    


