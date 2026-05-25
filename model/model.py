from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getAnniVendite(self):
        return DAO.getAnniVendite(self)

    def getBrandProdotti(self):
        return DAO.getBrandProdotti(self)

    def getRetailers(self):
        return DAO.getRetailers(self)

    def getTopVendite(self, anno, brand, retailer):
        return DAO.getTopVendite(self, anno, brand, retailer)