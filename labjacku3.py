import time
import os
import csv
from datetime import datetime
from decimal import *
import u3_mod

FILE_SAVE_TO = "E:\\test_python\\New"
FILE_NAME = ""	
CURRENT_FILE = ""

lj = u3_mod.U3()
lj.debug = True
lj.configIO(EnableCounter0 = True, EnableCounter1 = True, FIOAnalog = 0)

tstart = time.perf_counter() 

def write_file(path):
    global CURRENT_FILE
    get_file_name()
    path_to_file = os.path.join(FILE_SAVE_TO, FILE_NAME)
    CURRENT_FILE = path_to_file

    if not os.path.isfile(path_to_file):
        f = open(path_to_file, "x")
        f.close()
		
def get_file_name():
    global FILE_NAME
    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    FILE_NAME = "rpm_log_." + day + month + year + ".csv"

def write_data_to_file(message):
    write_file(FILE_SAVE_TO)
    data = message.split(',')
    with open(CURRENT_FILE, 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(data)
    csvFile.close()
	

while True :

    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S:%f")

    tcurr = time.perf_counter() - tstart
    #Every second Count and reset count
    if tcurr > 1:
        print("--",timestamp,"--")
        
        x = lj.getFeedback(u3_mod.Counter0( Reset = True ), u3_mod.Counter1( Reset = True ) )
        #Split list to 2 variable
        y = x[:1]
        z = x[1:]
        #Convert to float
        y = sum(y)
        z = sum(z)
        
        ppr = 4*360
        y = (y/ppr)*60
        z = (z/ppr)*60   

        #Make it decimal
        y = int(y)
        z = int(z)

        print("Counter 0:",y)
        print("Counter 1:",z)

        #Convert to string for log purpose
        a = str(y)
        b = str(z)

        #Save as log
        dataresult = timestamp + "/ Counter 0:" + a + "/ Counter 1:" + b  
        print(dataresult)
        #write_data_to_file(dataresult)

        print("----------------")
        tstart = time.perf_counter() 
        