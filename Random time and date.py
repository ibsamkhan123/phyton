import random #import module
import time



def getRandomDate(startDate, endDate):#defining function
    print("A Random date between", startDate,"and",endDate )

    randomGenerator = random.random ()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = startTime + randomGenerator *(endTime - startTime)
    randomDate =time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
#display result
print("The random date isssss:", getRandomDate ("1/10/1985", "7/12/2025"))