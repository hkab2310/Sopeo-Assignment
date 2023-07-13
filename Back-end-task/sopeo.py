import csv
import json

with open('dataset.csv',mode="r") as file:

    datafile = csv.reader(file)

    # for lines in datafile:
    #     print(lines)

   
   
    countOfBedsPerWard = {}
    countOfBedsPerRoom = {}
    countOfBedsPerStatus = {}
    countOfOccupiedBedsPerWard = {}
    occupancyPerWard={}
    countOfOccupiedBedsPerRoom = {}
    occupancyPerRoom={}
    countOfBedPerWardWithStatus={}
    countOfBedPerRoomWithStatus={}
    totalBeds = 0
    for lines in datafile:
        if(lines[4]=='NURSENAME'):
            continue

        totalBeds = totalBeds+1

        if lines[4] in countOfBedsPerWard.keys():
            countOfBedsPerWard[lines[4]] = countOfBedsPerWard[lines[4]] + 1
        else:
            countOfBedsPerWard[lines[4]] = 1

        if lines[5] in countOfBedsPerRoom.keys():
            countOfBedsPerRoom[lines[5]] = countOfBedsPerRoom[lines[5]] + 1
        else:
            countOfBedsPerRoom[lines[5]] = 1

        if lines[9] in countOfBedsPerStatus.keys():
            countOfBedsPerStatus[lines[9]] = countOfBedsPerStatus[lines[9]] + 1
        else:
            countOfBedsPerStatus[lines[9]] = 1

        if lines[4] in countOfOccupiedBedsPerWard.keys():
            if lines[9] == 'Occupied Discharge' or lines[9] == 'Occupied(Male)' or lines[9] == 'Occupied(Female)':
                countOfOccupiedBedsPerWard[lines[4]] = countOfOccupiedBedsPerWard[lines[4]] + 1 
        else:
            if lines[9] == 'Occupied Discharge' or lines[9] == 'Occupied(Male)' or lines[9] == 'Occupied(Female)':
                countOfOccupiedBedsPerWard[lines[4]] = 1
            else:
                countOfOccupiedBedsPerWard[lines[4]] = 0

        if lines[5] in countOfOccupiedBedsPerRoom.keys():
            if lines[9] == 'Occupied Discharge' or lines[9] == 'Occupied(Male)' or lines[9] == 'Occupied(Female)':
                countOfOccupiedBedsPerRoom[lines[5]] = countOfOccupiedBedsPerRoom[lines[5]] + 1 
        else:
            if lines[9] == 'Occupied Discharge' or lines[9] == 'Occupied(Male)' or lines[9] == 'Occupied(Female)':
                countOfOccupiedBedsPerRoom[lines[5]] = 1
            else:
                countOfOccupiedBedsPerRoom[lines[5]] = 0

        if lines[4] in countOfBedPerWardWithStatus.keys():
            countOfBedPerWardWithStatus[lines[4]][lines[9]] =  countOfBedPerWardWithStatus[lines[4]][lines[9]] + 1
        else:
            countOfBedPerWardWithStatus[lines[4]] = {
                'Occupied Discharge': 0,
                'Vacant Dirty': 0,
                'Available': 0,
                'Occupied(Male)': 0,
                'Occupied(Female)': 0, 
                'Blocked': 0  
            }
            countOfBedPerWardWithStatus[lines[4]][lines[9]] = countOfBedPerWardWithStatus[lines[4]][lines[9]] + 1

        if lines[5] in countOfBedPerRoomWithStatus.keys():
            countOfBedPerRoomWithStatus[lines[5]][lines[9]] =  countOfBedPerRoomWithStatus[lines[5]][lines[9]] + 1
        else:
            countOfBedPerRoomWithStatus[lines[5]] = {
                'Occupied Discharge': 0,
                'Vacant Dirty': 0,
                'Available': 0,
                'Occupied(Male)': 0,
                'Occupied(Female)': 0, 
                'Blocked': 0  
            }
            countOfBedPerRoomWithStatus[lines[5]][lines[9]] =  countOfBedPerRoomWithStatus[lines[5]][lines[9]] + 1



    # 1.Get the Count of beds in each ward.
    print(json.dumps(countOfBedsPerWard,indent=4))

    # 2.Get the count of bed in each room.
    print(json.dumps(countOfBedsPerRoom,indent=4))

    # 3.Get the count of the bed under each status.
    print(json.dumps(countOfBedsPerStatus,indent=4))

    # 4.Calculate the overall occupancy percentage (total occupied / total bed).
    # i am considering 'Occupied Discharge' , 'Occupied(Male)' ,'Occupied(Female)' as occupied
    print((countOfBedsPerStatus['Occupied Discharge']+countOfBedsPerStatus['Occupied(Male)']+countOfBedsPerStatus['Occupied(Female)'])/totalBeds)
    
    # 5.Calculate occupancy for each ward.
    for key,value in countOfOccupiedBedsPerWard.items():
        occupancyPerWard[key] = value/countOfBedsPerWard[key]
    print(json.dumps(occupancyPerWard,indent=4))       

    # 6.Calculate occupancy for each room. 
    for key,value in countOfOccupiedBedsPerRoom.items():
        occupancyPerRoom[key] = value/countOfBedsPerRoom[key]
    print(json.dumps(occupancyPerRoom,indent=4))  

    # 7.Calculate count of bed with all the different bed statuses for each ward.
    print(json.dumps(countOfBedPerWardWithStatus,indent=4))  

    # 8.Calculate count of bed with all the different bed statuses for each room.
    print(json.dumps(countOfBedPerRoomWithStatus,indent=4))