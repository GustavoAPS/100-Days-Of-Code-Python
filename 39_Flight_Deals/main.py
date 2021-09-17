from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager


new_fly_search = FlightSearch()
# data manager will do the communication to sheets
new_data_manager = DataManager()

# receiving a dictionary from data manager
sheet_data = new_data_manager.get_sheet_data()
pprint(sheet_data)


print(new_fly_search.get_destination_code("Toronto"))

for line_data in sheet_data:
    line_data['iataCode'] = new_fly_search.get_destination_code(line_data['city'])
    # new_data_manager.update_line(line_data)

for line_data in sheet_data:
    new_data_manager.update_line(line_data)

print(sheet_data)
