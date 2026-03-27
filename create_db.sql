CREATE TABLE city_attributes (
	CityID INTEGER PRIMARY KEY,
	Latitude FLOAT(24),
	Longitude FLOAT(24),
	CityName VARCHAR(20),
	Country VARCHAR(20)
);

CREATE TABLE records (
	RecordID INTEGER PRIMARY KEY,
	CityID INTEGER,
	DateDay DATE,
	DateHour INTEGER
);

CREATE TABLE weather_desc_lookup (
	DescID INTEGER PRIMARY KEY,
	Description VARCHAR(30)
);

CREATE TABLE humidity (
	RecordID INTEGER PRIMARY KEY,
	Humidity FLOAT(24)
);
