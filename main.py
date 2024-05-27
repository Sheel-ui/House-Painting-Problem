import operator
import sys
import strat1, strat2, strat3, strat4, strattop

# Transforming list to dict
def transformHouseList(houseList):
    houseDictList = []
    for i in range(len(houseList)):
        houseDictList.append({
            'startDate': houseList[i][0],
            'endDate': houseList[i][1],
            'index': i + 1
        })
    return houseDictList

if __name__ == "__main__":
    n_m = input()

    # STDIN
    houseList = []
    n,m = int(n_m.split(' ')[0]),int(n_m.split(' ')[1])

    for i in range(m):
        house = input()
        houseList.append([int(house.split(' ')[0]),int(house.split(' ')[1])])

    # Transform user input to supported format
    houseList = transformHouseList(houseList)

    paintedIndexList =[]
    # Invoking Strategies
    if sys.argv[1] == "strat1":
        paintedIndexList = strat1.strat1(n,m,houseList)
    elif sys.argv[1] == "strat2":
        paintedIndexList = strat2.strat2(n,m,houseList)
    elif sys.argv[1] == "strat3":
        paintedIndexList = strat3.strat3(n,m,houseList)
    elif sys.argv[1] == "strat4":
        paintedIndexList = strat4.strat4(n,m,houseList)
    elif sys.argv[1] == "stratop":
        paintedIndexList = strattop.strattop(n,m,houseList)

    print(" ".join(str(item) for item in paintedIndexList))