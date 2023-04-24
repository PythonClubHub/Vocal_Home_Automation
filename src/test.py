
import sqlite3
import thermostat

thermostat = thermostat.Thermostat()

value = thermostat.get_temperature_threshold()
print(value)

status = thermostat.heating_status()
print(status)

data = thermostat.compare_temp_with_threshold()
print(data)