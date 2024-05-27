from heapq import heappop, heappush, heapify

def strat4(n,m,houseList):
    heap = []
    paintedIndexList = []
    currentHouse = 0
    day = 1
    
    # Iterate day from 1 to n
    for day in range(1,n+1):
        isPainted = False
        # Add all the houses which become available at currentDay to min heap ordered by (ascending) endDate and (ascending) startDate
        while currentHouse < m and houseList[currentHouse]['startDate'] <= day:
            heappush(heap, 
            (
                houseList[currentHouse]['endDate'],
                houseList[currentHouse]['startDate'],
                houseList[currentHouse]['index'],
                houseList[currentHouse]
            ))
            currentHouse += 1
        # While there are houses available to be painted and no houses have been painted on currentDay
        while len(heap)>0 and isPainted == False:
            # Pop house from min heap and see if it can be painted and paint it
            house = heappop(heap)[-1]
            if day >= house['startDate'] and day <= house['endDate']:
                paintedIndexList.append(house['index'])
                isPainted = True
    return paintedIndexList