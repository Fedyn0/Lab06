from database.DB_connect import DBConnect


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

        query = """ select distinct Retailer_name as retailer
                    from go_retailers"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["retailer"])

        res.sort()
        cursor.close()
        cnx.close()
        return res
