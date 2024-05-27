def strat1(n,m,houseList):
    day = 1
    paintedIndexList = []
    currentHouse = 0

    # Loop till either all days or all houses are not processed
    while day <= n and currentHouse < m:
        # If currentHouse can be painted on currentDay then paint it and increment currentHouse and currentDay
        if day>=houseList[currentHouse]['startDate'] and day <= houseList[currentHouse]['endDate']:
            paintedIndexList.append(houseList[currentHouse]['index'])
            currentHouse += 1
            day += 1
        # If currentHouse cannot be painted on day
        else:
            # Increment day if day is before the start date of currentHouse, if not increment house since it is not eligible to be painted anymore
            if day < houseList[currentHouse]['startDate']:
                day += 1
            else:
                currentHouse += 1
    return paintedIndexList