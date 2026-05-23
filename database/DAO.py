from database.DB_connect import DBConnect


class DAO():

    @staticmethod
    def getAllCorsi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select DISTINCT YEAR(Date)
                    from go_daily_sales"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res
