import oracledb

DB_USER = "system"
DB_PASS = "testpass1"
DB_DSN = "localhost:1521/XE" 

# Initialize thick mode - COMMENTED OUT TO USE THIN MODE (Fixes DPI-1047)
# LIB_DIR = r"C:\app\conno\product\21c\dbhomeXE\bin"
# try:
#     oracledb.init_oracle_client(lib_dir=LIB_DIR)
# except Exception as e:
#     print(f"Warning: Oracle client init failed. Error: {e}")

def get_connection():
    return oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)

def feature_1():
    print("\n--- Get Temperature by City and Date ---")
    city = input("Enter city name (e.g., Miami): ")
    date_day = input("Enter date (YYYY-MM-DD): ")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT c.CityName, TO_CHAR(r.DateDay, 'YYYY-MM-DD'), r.DateHour, t.Temperature 
            FROM city_attributes c 
            JOIN records r ON c.CityID = r.CityID 
            JOIN temperature t ON r.RecordID = t.RecordID 
            WHERE LOWER(c.CityName) = LOWER(:1) AND r.DateDay = TO_DATE(:2, 'YYYY-MM-DD')
            ORDER BY r.DateHour
        """
        cursor.execute(query, [city, date_day])
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"City: {row[0]} | Date: {row[1]} | Hour: {row[2]} | Temp: {row[3]:.2f}")
        else:
            print("No records found for that city and date.")
    except Exception as e:
        print(f"Database Error: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def feature_2():
    print("\n--- High Wind Speed Alert ---")
    try:
        threshold = float(input("Enter minimum wind speed: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT c.CityName, TO_CHAR(r.DateDay, 'YYYY-MM-DD'), r.DateHour, w.WindSpd 
            FROM wind w 
            JOIN records r ON w.RecordID = r.RecordID 
            JOIN city_attributes c ON r.CityID = c.CityID 
            WHERE w.WindSpd > :1 
            ORDER BY w.WindSpd DESC FETCH FIRST 50 ROWS ONLY
        """
        cursor.execute(query, [threshold])
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"City: {row[0]} | Date: {row[1]} | Hour: {row[2]} | Wind Speed: {row[3]:.2f}")
        else:
            print("No records found exceeding that wind speed.")
    except Exception as e:
        print(f"Database Error: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def feature_3():
    print("\n--- Search Weather by Description ---")
    keyword = input("Enter weather keyword (e.g., rain, clear, clouds): ")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT c.CityName, TO_CHAR(r.DateDay, 'YYYY-MM-DD'), r.DateHour, l.Description 
            FROM weather_description wd 
            JOIN weather_desc_lookup l ON wd.DescID = l.DescID 
            JOIN records r ON wd.RecordID = r.RecordID 
            JOIN city_attributes c ON r.CityID = c.CityID 
            WHERE LOWER(l.Description) LIKE LOWER('%' || :1 || '%')
            FETCH FIRST 50 ROWS ONLY
        """
        cursor.execute(query, [keyword])
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"City: {row[0]} | Date: {row[1]} | Hour: {row[2]} | Conditions: {row[3]}")
        else:
            print("No matching weather descriptions found.")
    except Exception as e:
        print(f"Database Error: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def feature_4():
    print("\n--- Find City Geographic Details ---")
    city = input("Enter city name: ")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT CityName, Country, Latitude, Longitude FROM city_attributes WHERE LOWER(CityName) = LOWER(:1)"
        cursor.execute(query, [city])
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"City: {row[0]} | Country: {row[1]} | Lat: {row[2]} | Lon: {row[3]}")
        else:
            print("City not found in the database.")
    except Exception as e:
        print(f"Database Error: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def feature_5():
    print("\n--- Average Historical Temperature by City ---")
    city = input("Enter city name: ")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT c.CityName, AVG(t.Temperature) as AvgTemp 
            FROM city_attributes c 
            JOIN records r ON c.CityID = r.CityID 
            JOIN temperature t ON r.RecordID = t.RecordID 
            WHERE LOWER(c.CityName) = LOWER(:1)
            GROUP BY c.CityName
        """
        cursor.execute(query, [city])
        results = cursor.fetchall()
        if results and results[0][1] is not None:
            print(f"The average historical temperature for {results[0][0]} is {results[0][1]:.2f}")
        else:
            print("No temperature records found for that city.")
    except Exception as e:
        print(f"Database Error: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def main():
    while True:
        print("\n=== Weather and Climate DB Interface ===")
        print("1. Get Temperature by City and Date")
        print("2. High Wind Speed Alert")
        print("3. Search Weather by Description")
        print("4. Find City Geographic Details")
        print("5. Average Historical Temperature by City")
        print("6. Exit")
        choice = input("Select a feature (1-6): ")
        if choice == '1': feature_1()
        elif choice == '2': feature_2()
        elif choice == '3': feature_3()
        elif choice == '4': feature_4()
        elif choice == '5': feature_5()
        elif choice == '6':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
