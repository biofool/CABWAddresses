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
    current_division = ""
    current_dojo = ""
    current_address = []
    address_started = False

    # Read data from file
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Process each line
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check for division line
        if line.startswith("DIVISION"):
            current_division = line.split()[1]
        # Check for dojo name line
        elif not address_started:
            current_dojo = line
            address_started = True
        # Check for address line
        elif line:
            current_address.append(line)
        # Check for end of address
        elif address_started:
            # Process the collected address lines
            address_lines = len(current_address)
            dojo_name = current_dojo
            city_state_line = current_address[-1]
            city_state_parts = city_state_line.split(", ")
            city = city_state_parts[0]
            postal_code = ""
            country = ""

            # Extract postal code and country if available
            if len(city_state_parts) > 1:
                postal_code_country = city_state_parts[1]
                postal_code_parts = postal_code_country.split()
                if len(postal_code_parts) > 1:
                    postal_code = postal_code_parts[0]
                    country = " ".join(postal_code_parts[1:])
                else:
                    country = postal_code_country

            # Append data to the list
            data.append([current_division, dojo_name, postal_code, city, country])

            # Reset variables for the next address
            current_dojo = ""
            current_address = []
            address_started = False

    # Write data to a spreadsheet
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Division", "Dojo Name", "Postal Code", "City", "Country"])  # Write header
        writer.writerows(data)
