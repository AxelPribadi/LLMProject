
import pandas as pd
import pymysql
from dataclasses import dataclass


@dataclass
class MySQL():
    user: str
    password: str
    host: str
    database: str
    connection: pymysql.connections.Connection = None


    def connect(self):
        # connect to the database
        try:
            self.connection = pymysql.connect(host=self.host,
                                              user=self.user,
                                              password=self.password,
                                              database=self.database)
            
            if self.connection:
                print("Established connection with the database")
            else:
                self.connection = None
        except pymysql.MySQLError as e:
            print(f"Failed to connect to MySQL: {e}")
            self.connection = None


    def disconnect(self):
        # disconnect from the database
        try:
            if self.connection:
                self.connection.close()
                self.connection = None
                print("Terminated connection with the database")
        except pymysql.MySQLError as e:
            print(f"Failed to disconnect from MySQL: {e}")


    def status(self):
        # Check connector status
        if self.connection:
            return "Status: Connected"
        else:
            return "Status: Disconnected"


    def __check_query(self,query):
        # check if query is DQL or DML
        query_type = query.strip().split()[0].upper()

        if query_type in ['SELECT', 'SHOW', 'DESCRIBE', 'EXPLAIN']:
            return 'DQL'
        elif query_type in ['INSERT', 'UPDATE', 'DELETE', 'REPLACE']:
            return 'DML'
        else:
            return 'UNKNOWN'


    def dql_query(self, query, params=()): 
        # execute DQL query and return data in a DataFrame
        
        # check if connector is connected
        if not self.connection:
            print("No connection to the database")
            return None
        
        # check query type
        query_type = self.__check_query(query)
        if query_type != 'DQL':
            print("Query provided is not a DQL-statement")
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)

                # store data in DataFrame
                cols = [i[0] for i in cursor.description]
                df = pd.DataFrame(cursor.fetchall(), columns=cols)

            return df
            
        except pymysql.MySQLError as e:
            # discard any changes made
            self.connection.rollback()
            print(f"Failed to run query: {e}")
            return None


    def dml_query(self, query, params=()):
        # execute query and return data in a DataFrame
        
        # check if connector is connected
        if not self.connection:
            print("No connection to the database")
            return None

        # check query type
        query_type = self.__check_query(query)
        if query_type != 'DML':
            print("Query provided is not a DML-statement. No changes were made in the database")
            return None
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                affected_rows = cursor.rowcount

            print(f"Query executed successfully, {affected_rows} rows affected")
            return affected_rows

        except pymysql.MySQLError as e:
            # discard any changes made
            self.connection.rollback()
            print(f"Failed to run query: {e}")
            return None
        

if __name__ == "__main__":
    # dbconnect("localhost", "root", "axelp1403", "sakila")

    # query = ("""
    #          select *
    #          from actor limit 10 
    #          """)
    
    # query2 = ("""
    #          select *
    #          from customer limit 10 
    #          """)
    
    query = "select * from Prompts"

    db = MySQL("root", "password", "localhost", "llmproject")

    print(db.status())
    db.connect()

    x = db.dql_query(query)
    print(x)

    print(db.status())

    # y = db.dql_query(query2)
    # print(y)

    db.disconnect()
    print(db.status())


