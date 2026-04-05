import psycopg2

from psycopg2 import sql
class QueryDatabase:
    def __init__(self, host_="localhost", database_="database",user_="postgres",password_="password",port_="5432"):
        import psycopg2
        self._database_connection = psycopg2.connect(host= host_, database = database_, user = user_, password = password_, port=port_)
        self._cursor = self._database_connection.cursor()
        #TODO: Set a try except block testing all the possible connection errors that can occur when connecting
                # Tips
                #try creating the errors first by providing each info wrongly
                # ensure you return the possible  error issue to the user
    def insert_data_into_table_query(self, col_names_list=[],table_name="" ,data_to_insert_list=[]):
        """This function takes the data provided by the user as lists, gets how long the data is to know
        how many %s will be passed into the values() part of the insert query.
        The function the replaces the column_name part in the insert query with the col_name given
        The function the replaces the columns
         part with the column names passed in the list and the data with the data passed in the list"""
        from psycopg2 import sql
        len_of_col_names_list = len(col_names_list)
        len_of_data_to_insert_list = len(data_to_insert_list)
        #TODO: Create a if else block that makes sure the col_names_list is of the same length as data_to_insert_list
            # if they are not of the same size return that message and pass the function else continue with the functions task
        placeholders= "%s,"
        #TODO: Do error handling here to prevent the program from crashing if the list has 0 or 1 elements
        placeholders*=len_of_data_to_insert_list-1
        placeholders+= "%s"
        col_name_unpacked_list = ", ".join(col_names_list)

        self._cursor.execute(f"""INSERT INTO {table_name}({col_name_unpacked_list}) VALUES ({placeholders})""",
                             (data_to_insert_list))
        self._database_connection.commit()
        self._cursor.close()
        self._database_connection.close()

query = QueryDatabase(database_="Kinjo")
query.insert_data_into_table_query(table_name="signup_info",
                                   col_names_list=["first_name","second_name", "surname","email","phone_number"],
                                   data_to_insert_list=["denis", "mwenda", "Gitonga", "ian@gmail.com", "01234567890"])
