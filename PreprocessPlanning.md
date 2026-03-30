# Preprocessing:

city_attributes:
- Needs IDs added when inserted into the table, no other modifications necessary

humidity, pressure, temperature:
- City names need to be moved into the rows and not be the column names
	
wind_direction, wind_speed:
- City names need to be moved into the rows
- Data columns need to be combined

weather_description:
- Unique descriptions need to be split into unique table
- City names need to be moved into rows

records:
- Needs to be created based on the cities and timestamps of all of the data
