CREATE TABLE city_attributes (
	CityID INT PRIMARY KEY,
	Latitude FLOAT(24),
	Longitude FLOAT(24),
	CityName VARCHAR(20),
	Country VARCHAR(20)
);

CREATE TABLE records (
	RecordID INT PRIMARY KEY,
	CityID INT,
	DateDay DATE,
	DateHour INT
);

CREATE TABLE weather_desc_lookup (
	DescID INT PRIMARY KEY,
	Description VARCHAR(30)
);

CREATE TABLE humidity (
	RecordID INT PRIMARY KEY,
	Humidity FLOAT(24)
);

CREATE TABLE pressure (
	RecordID INT PRIMARY KEY,
	Pressure FLOAT(24)
);

CREATE TABLE temperature (
	RecordID INT PRIMARY KEY,
	Temperature FLOAT(24)
);

CREATE TABLE wind (
	RecordID INT PRIMARY KEY,
	WindDir FLOAT(24),
	WindSpd FLOAT(24)
);

CREATE TABLE weather_description (
	RecordID INT PRIMARY KEY,
	DescID INT
);
