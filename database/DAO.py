from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendite import Vendite


class DAO():


    @staticmethod
    def getAnniVendite(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select DISTINCT YEAR(Date) as anno
                    from go_daily_sales"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["anno"])

        res.sort()
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrandProdotti(self):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select distinct Product_brand as brand
                    from go_products"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["brand"])

        res.sort()
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailers(self):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select distinct *
                    from go_retailers"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Retailer(**row))

        res.sort
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getTopVendite(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select distinct gds.*
                    from go_daily_sales gds, go_products gp 
                    where gp.Product_number = gds.Product_number
                    and gds.Retailer_code = coalesce(%s, gds.retailer_code)
                    and year(gds.Date) = coalesce(%s, year(gds.Date))
                    and gp.Product_brand = coalesce(%s, gp.Product_brand) 
                    order by (gds.Unit_sale_price * gds.Quantity) desc
                    limit 5"""

        cursor.execute(query, (retailer, anno, brand))

        res = []
        for row in cursor:
            res.append(Vendite(**row))


        cursor.close()
        cnx.close()
        return res
