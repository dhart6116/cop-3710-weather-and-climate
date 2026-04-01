import oracledb
import csv

# Initialize database information
LIB_DIR = r"C:\oracle\instantclient_21_3"
DB_USER = "your_username"
DB_PASS = "your_password"
DB_DSN = "host:port/service_name"

# Initialize thick mode
oracledb.init_oracle_client(lib_dir=LIB_DIR)

def load_city_attributes(fpath):
    try:
        # Make connection
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        
        # Read CSV after skipping header
        with open(fpath, mode = 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            city_data = [row for row in header]
        
        # Bulk-load command
        city_sql = "INSERT INTO city_attributes (CityID, CityName, Country, Latitude, Longitude) VALUES (:1, :2, :3, :4, :5)"
        
        # Being loading
        print(f"Starting bulk load of {len(city_data)} rows into city_attributes...")
        cursor.executemany(city_sql, city_data)
        
        cursor.close()
        conn.close()
        print("Oracle connection closed.")

def load_weather_desc_lookup(fpath):
    try:
        # Make connection
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        
        # Read CSV after skipping header
        with open(fpath, mode = 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            desc_lookup_data = [row for row in header]
        
        # Bulk-load command
        desc_lookup_sql = "INSERT INTO weather_desc_lookup (DescID, Description) VALUES (:1, :2)"
        
        # Being loading
        print(f"Starting bulk load of {len(desc_lookup_data)} rows into weather_desc_lookup...")
        cursor.executemany(desc_lookup_sql, desc_lookup_data)
        
        cursor.close()
        conn.close()
        print("Oracle connection closed.")

def load_records(fpath):
    try:
        # Make connection
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        
        # Read CSV after skipping header
        with open(fpath, mode = 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            records_data = [row for row in header]
        
        # Bulk-load command
        records_sql = "INSERT INTO records (RecordID, CityID, DateDay, DateHour) VALUES (:1, :2, :3, :4)"
        
        # Being loading
        print(f"Starting bulk load of {len(records_data)} rows into records...")
        cursor.executemany(records_sql, records_data)
        
        cursor.close()
        conn.close()
        print("Oracle connection closed.")

def load_humidity(fpath):
    try:
        # Make connection
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        
        # Read CSV after skipping header
        with open(fpath, mode = 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            humidity_data = [row for row in header]
        
        # Bulk-load command
        humidity_sql = "INSERT INTO humidity (RecordID, Humidity) VALUES (:1, :2)"
        
        # Being loading
        print(f"Starting bulk load of {len(humidity_data)} rows into humidity...")
        cursor.executemany(humidity_sql, humidity_data)
        
        cursor.close()
        conn.close()
        print("Oracle connection closed.")
        
def load_pressure(fpath):
    try:
        # Make connection
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        
        # Read CSV after skipping header
        with open(fpath, mode = 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            pressure_data = [row for row in header]
        
        # Bulk-load command
        pressure_sql = "INSERT INTO pressure (RecordID, Pressure) VALUES (:1, :2)"
        
        # Being loading
        print(f"Starting bulk load of {len(pressure_data)} rows into pressure...")
        cursor.executemany(pressure_sql, pressure_data)
        
        cursor.close()
        conn.close()
        print("Oracle connection closed.")
        
def load_temperature(fpath):
    try:
        # Make connection
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        
        # Read CSV after skipping header
        with open(fpath, mode = 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            temperature_data = [row for row in header]
        
        # Bulk-load command
        temperature_sql = "INSERT INTO temperature (RecordID, Temperature) VALUES (:1, :2)"
        
        # Being loading
        print(f"Starting bulk load of {len(temperature_data)} rows into temperature...")
        cursor.executemany(temperature_sql, temperature_data)
        
        cursor.close()
        conn.close()
        print("Oracle connection closed.")
        
def load_wind(fpath):
    try:
        # Make connection
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        
        # Read CSV after skipping header
        with open(fpath, mode = 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            wind_data = [row for row in header]
        
        # Bulk-load command
        wind_sql = "INSERT INTO wind (RecordID, WindDir, WindSpd) VALUES (:1, :2, :3)"
        
        # Being loading
        print(f"Starting bulk load of {len(wind_data)} rows into wind...")
        cursor.executemany(wind_sql, wind_data)
        
        cursor.close()
        conn.close()
        print("Oracle connection closed.")
        
def load_weather_desc(fpath):
    try:
        # Make connection
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        
        # Read CSV after skipping header
        with open(fpath, mode = 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            weather_desc_data = [row for row in header]
        
        # Bulk-load command
        weather_desc_sql = "INSERT INTO wind (RecordID, DescID) VALUES (:1, :2)"
        
        # Being loading
        print(f"Starting bulk load of {len(weather_desc_data)} rows into weather_description...")
        cursor.executemany(weather_desc_sql, weather_desc_data)
        
        cursor.close()
        conn.close()
        print("Oracle connection closed.")