CREATE TABLE city_attributes (
	CityID INT,
	Latitude FLOAT,
	Longitude FLOAT,
	CityName VARCHAR(20),
	Country VARCHAR(20),
	PRIMARY KEY (CityID)
);

CREATE TABLE records (
	RecordID INT,
	CityID INT NOT NULL,
	DateDay DATE NOT NULL,
	DateHour INT NOT NULL,
	PRIMARY KEY (RecordID)
);

CREATE TABLE weather_desc_lookup (
	DescID INT,
	Description VARCHAR(30),
	PRIMARY KEY (DescID)
);

CREATE TABLE humidity (
	RecordID INT,
	Humidity FLOAT,
	PRIMARY KEY (RecordID)
);

CREATE TABLE pressure (
	RecordID INT,
	Pressure FLOAT,
	PRIMARY KEY (RecordID)
);

CREATE TABLE temperature (
	RecordID INT,
	Temperature FLOAT,
	PRIMARY KEY (RecordID)
);

CREATE TABLE wind (
	RecordID INT,
	WindDir FLOAT,
	WindSpd FLOAT,
	PRIMARY KEY (RecordID)
);

CREATE TABLE weather_description (
	RecordID INT,
	DescID INT,
	PRIMARY KEY (RecordID)
);

ALTER TABLE records
ADD CONSTRAINT fk_records_city
	FOREIGN KEY (CityID)
	REFERENCES city_attributes(CityID);
	
ALTER TABLE humidity
ADD CONSTRAINT fk_humidity_records
	FOREIGN KEY (RecordID)
	REFERENCES records(RecordID);
	
ALTER TABLE pressure
ADD CONSTRAINT fk_pressure_records
	FOREIGN KEY (RecordID)
	REFERENCES records(RecordID);
	
ALTER TABLE temperature
ADD CONSTRAINT fk_temp_records
	FOREIGN KEY (RecordID)
	REFERENCES records(RecordID);
	
ALTER TABLE wind
ADD CONSTRAINT fk_wind_records
	FOREIGN KEY (RecordID)
	REFERENCES records(RecordID);
	
ALTER TABLE weather_description
ADD CONSTRAINT fk_wdesc_records
	FOREIGN KEY (RecordID)
	REFERENCES records(RecordID);

ALTER TABLE weather_description
ADD CONSTRAINT fk_wdesc_desclookup
	FOREIGN KEY (DescID)
	REFERENCES weather_desc_lookup(DescID);
