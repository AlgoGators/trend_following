import pandas as pd 
from sqlalchemy import create_engine
import urllib

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DUSTIN_DATE_FORMAT = "%m/%d/%Y"

def get_data(instrument_list: list):
    # get all tables from database
    driver = "ODBC Driver 18 for SQL Server"
    server = "algo.database.windows.net"
    username = "dbmaster"
    password = "Password1"

    database = "NG_Carver_Data"

    # Connection string for SQL Server Authentication - do not change
    params = urllib.parse.quote_plus(fr'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    # Retrieve a list of all table names in the database - do not change
    table_names_query = "SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_catalog='" + database + "'"
    table_names = pd.read_sql(table_names_query, engine)['table_name'].tolist()

    # Dictionary to store each table's DataFrame
    dataframes = {}

    # Remove instrument from list table_names if it is not in instrument_list
    for table_name in table_names:
        # remove _Data from table name temporarily
        name = table_name[:-5]
        if name not in instrument_list:
          table_names.remove(table_name)

    # Remove sysdiagrams from table_names
    table_names.remove('sysdiagrams')

    # Remove _Data from table names
    for i in range(len(table_names)):
        table_names[i] = table_names[i][:-5]

    # Print the tables that will be pulled
    print(sorted(table_names))

    # Loop through all table names, pulling data from each one
    for table_name in table_names:
        table_query = f"SELECT * FROM [{table_name}_Data]"
        dataframes[table_name] = pd.read_sql(table_query, engine)

    # Convert date column to datetime
    for table_name in table_names:
        dataframes[table_name]['Date'] = pd.to_datetime(dataframes[table_name]['Date'], format=mixed)

    # Set index to date column
    for table_name in table_names:
        dataframes[table_name].set_index('Date', inplace=True)
        assert dataframes[table_name].index.name == 'Date'

    # Get all adjusted close prices in each dataframe
    adjusted_prices = {}
    for table_name in table_names:
        adjusted_prices[table_name] = dataframes[table_name]['Close']

    # Get all unadjusted close prices in each dataframe
    current_prices = {}
    for table_name in table_names:
        current_prices[table_name] = dataframes[table_name]['Unadj_Close']
    
    return adjusted_prices, current_prices


def pd_read_sql(
    ins_code: str,
    engine,
        date_format=DUSTIN_DATE_FORMAT,
        date_index_name: str="Date",
) -> pd.DataFrame:

    ans = pd.read_sql(ins_code, engine)
    ans.index = pd.to_datetime(ans[date_index_name], format=date_format).values

    del ans[date_index_name]

    ans.index.name = None

    return ans

def pd_read_sql_carry(
    ins_code: str,
    engine,
        date_format=DEFAULT_DATE_FORMAT,
        date_index_name: str="index",
) -> pd.DataFrame:

    ans = pd.read_sql(ins_code, engine)
    ans.index = pd.to_datetime(ans[date_index_name], format=date_format).values

    del ans[date_index_name]

    ans.index.name = None

    return ans

def get_data_dict_sql_no_carry(instr_list: list):
    driver = "ODBC Driver 18 for SQL Server"
    server = "algo.database.windows.net"
    username = "dbmaster"
    password = "Password1"
    database1 = "NG_Carver_Data"
    database2 = "NG_Carver_Data_Carry"

    params = urllib.parse.quote_plus(
        fr"DRIVER={driver};SERVER={server};DATABASE={database1};UID={username};PWD={password}"
    )
    engine1 = create_engine(
        "mssql+pyodbc:///?odbc_connect=%s" % params, pool_size=10, max_overflow=-1
    )

    # Connection to carry database
    params2 = urllib.parse.quote_plus(
        fr"DRIVER={driver};SERVER={server};DATABASE={database2};UID={username};PWD={password}"
    )
    engine2 = create_engine(
        "mssql+pyodbc:///?odbc_connect=%s" % params2, pool_size=10, max_overflow=-1
    )

    all_data = dict(
        [
            (instrument_code, pd_read_sql(f"SELECT * FROM [{instrument_code}]", engine1))
            for instrument_code in instr_list
        ]
    )

    all_data_carry = dict(
        [
            (instrument_code, pd_read_sql(f"SELECT * FROM [{instrument_code}_Carry]", engine2))
            for instrument_code in instr_list
        ]
    )

    adjusted_prices = dict(
        [
            (instrument_code, data_for_instrument.Close)
            for instrument_code, data_for_instrument in all_data.items()
        ]
    )

    current_prices = dict(
        [
            (instrument_code, data_for_instrument.Unadj_Close)
            for instrument_code, data_for_instrument in all_data.items()
        ]
    )
    return adjusted_prices, current_prices, 

def get_data_dict_sql_carry(instr_list: list):
    driver = "ODBC Driver 18 for SQL Server"
    server = "algo.database.windows.net"
    username = "dbmaster"
    password = "Password1"
    database1 = "NG_Carver_Data"
    database2 = "NG_Carver_Data_Carry"

    params = urllib.parse.quote_plus(
        fr"DRIVER={driver};SERVER={server};DATABASE={database1};UID={username};PWD={password}"
    )
    engine1 = create_engine(
        "mssql+pyodbc:///?odbc_connect=%s" % params, pool_size=10, max_overflow=-1
    )

    # Connection to carry database
    params2 = urllib.parse.quote_plus(
        fr"DRIVER={driver};SERVER={server};DATABASE={database2};UID={username};PWD={password}"
    )
    engine2 = create_engine(
        "mssql+pyodbc:///?odbc_connect=%s" % params2, pool_size=10, max_overflow=-1
    )

    all_data = dict(
        [
            (instrument_code, pd_read_sql(f"SELECT * FROM [{instrument_code}]", engine1))
            for instrument_code in instr_list
        ]
    )

    all_data_carry = dict(
        [
            (instrument_code, pd_read_sql(f"SELECT * FROM [{instrument_code}_Carry]", engine2))
            for instrument_code in instr_list
        ]
    )

    adjusted_prices = dict(
        [
            (instrument_code, data_for_instrument.Close)
            for instrument_code, data_for_instrument in all_data.items()
        ]
    )

    current_prices = dict(
        [
            (instrument_code, data_for_instrument.Unadj_Close)
            for instrument_code, data_for_instrument in all_data.items()
        ]
    )

    return adjusted_prices, current_prices, all_data_carry
def main():
    instrument_list = ['CL', 'ES', 'GC', 'HG', 'HO', 'NG', 'RB', 'SI']
    adjusted_prices, current_prices = get_data(instrument_list)
    print(adjusted_prices['CL'].tail())

if __name__ == '__main__':
    main()
