# Dawson Richey
# This will serve as the main app file for the project
from datetime import datetime, date

time = datetime.time()
date = date.date()
# Time abbreviation, hour min, and second
current_time = time.strftime("%H:%M:%S")
# Date abbreviation, day and year
current_date = date.strftime("%b-%d-%Y")

full_datetime = print("Time and Date =", current_time, current_date)