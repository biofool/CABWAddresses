# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# import googlemaps
#
#
# def validate_address(country, address, postal_code, city=''):
#     # Initialize the Google Maps client
#     gmaps = googlemaps.Client()
#
#     # Concatenate the address components with a comma separator
#     full_address = ', '.join(filter(None, [address, city, postal_code, country]))
#
#     # Geocode the address to retrieve location details
#     geocode_result = gmaps.geocode(full_address)
#
#     # Check if the geocode request returned any results
#     if geocode_result:
#         # Extract the postal code and city from the  resultS
#         result = geocode_result[0]
#         components = result.get('address_components', [])
#
#         for component in components:
#             types = component.get('types', [])
#             if 'postal_code' in types:
#                 postal_code = component['long_name']
#             elif 'locality' in types:
#                 city = component['long_name']
#
#         return postal_code, city
#
#     # No results found, return None for both postal code and city
#     return None, None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import csv

    # Initialize variables
    data = []
    address_lines = []
    current_dojo = ""
    current_address = []
    city_state_parts = []
    address_started = False
    (current_division, dojo_name, postal_code, city, country) = ('', '', '', '', '')
    # Read data from file
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Process each line
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if not len(line):
            # Blank Line encountered
            if address_started:
                # Process the collected address lines
                if len(current_address):
                    # Append data to the list
                    if (current_address > 1)
                        city_state_line = current_address[-1]
                        city_state_parts = city_state_line.split(", ")
                        city = city_state_parts[0]

                        # Extract postal code and country if available
                        if len(city_state_parts) > 1:
                            postal_code_country = city_state_parts[1]
                            postal_code_parts = postal_code_country.split()
                            if len(postal_code_parts) > 1:
                                postal_code = postal_code_parts[0]
                                country = " ".join(postal_code_parts[1:])
                            else:
                                country = postal_code_country
                    data.append([current_division, dojo_name, postal_code, city, country])
                    # Reset variables for the next address
                    postal_code = ""
                    country = ""
                    current_dojo = ""
                    current_address = []
                    address_started = False

        elif line.startswith("DIVISION"):
        # Check for division line
            current_division = line.split()[1]
            continue
        elif address_started:
            address_lines.append(line)
        else:
            address_started = True
            dojo_name = current_dojo

        # # Check for dojo name line  DUPLICATE
        # elif not address_started:
        #     current_dojo = line
        #     address_started = True
        #     current_address = []
        #     city_state_parts = []
        # Check for end of address

    # Write data to a spreadsheet
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Division", "Dojo Name", "Postal Code", "City", "Country"])  # Write header
        writer.writerows(data)
