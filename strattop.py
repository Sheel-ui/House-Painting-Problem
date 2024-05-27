from heapq import heappop, heappush, heapify

def strattop(n,m,houseList):
    heap = []
    paintedIndexList = []

    # Start currentDay with StartDate of first house
    currentDay = houseList[0]['startDate']

    # House 1 to m
    for house in houseList:

        # add to heap if StartDate of house is equal to currentDay
        if house['startDate'] == currentDay:
            heappush(heap,
                (
                house['endDate'],
                house['startDate'],
                house['index'],
                house
                ) 
            )
        # if StartDate is not equal to CurrentDate
        else:
            nextDay = house['startDate']
            # pop from the heap and paint the house (if valid) and increment the current day until you reach the nextDay
            while currentDay < nextDay and len(heap)>0 :
                paintedHouse = heappop(heap)[-1]
                if currentDay <= paintedHouse['endDate']:
                    if currentDay > n:
                        return paintedIndexList
                    paintedIndexList.append(paintedHouse['index'])
                    currentDay += 1
            currentDay = nextDay
            heappush(heap,
                (
                house['endDate'],
                house['startDate'],
                house['index'],
                house
                ) 
            )
    # after iterating through houses, pop the heap and paint the house (if valid) until the heap is empty
    while(len(heap)>0):
        paintedHouse = heappop(heap)[-1]
        if currentDay >= paintedHouse['startDate'] and currentDay <= paintedHouse['endDate']:
            if currentDay > n:
                return paintedIndexList
            paintedIndexList.append(paintedHouse['index'])
            currentDay += 1
    return paintedIndexList