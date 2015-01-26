from TwitterData import *
from Data.Return import Return

def getLastUserData():
    dataReturn = Return()
    lastUser = dataReturn.getLastUsername()
    getUserNetwork(lastUser)


if __name__ == "__main__":
    getLastUserData()
