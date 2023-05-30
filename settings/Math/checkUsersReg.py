
from data_base.mainDB import checkUsersInDb

async def checkUsersOfRegInDb(id):
    var = await checkUsersInDb(id)
    if var == True:
        return var
    elif var == False:
        return var