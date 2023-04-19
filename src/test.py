
import sqlite3
import thermostat

thermostat = thermostat.Thermostat()

value = thermostat.get_temperature_threshold()
print(value)

status = thermostat.heating_status()
print(status)