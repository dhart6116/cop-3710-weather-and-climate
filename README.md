# COP-3710.04 Project - Weather and Climate

Goal/Scope: To design a climate database that integrates temperature, precipitation, and weather events and includes anomaly detection queries, long-term trend windows, and partitioned time-series storage.

Application Domain: Long-term climate analysis

Users: Meteorologists and weather enthusiasts

Data Source: https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data

[ER Diagram can be found here.](database_er.md)

# How to use

- Use create_db to create the database tables
- Change lines 5-8 in dataload and 3-5 in main to your database's information
- Use dataload to populate the tables with data
- Run main.py with the command "Python -m main.py"
