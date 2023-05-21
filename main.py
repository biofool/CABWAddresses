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

    # Read data from file
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Process each line
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if 0 == len(line):
            dojo_name: str = ''
            postal_code: str = ''
            city: str = ''
            country: str = ''
        else:
            # Check for division line
            if line.startswith("DIVISION"):
                current_division = line.split()[1]
            # Check for address line
            elif line:
                # Split the address into different fields
                fields = line.split()

                # Extract dojo name
                dojo_name = line

                # Extract postal code, city, and country
                postal_code = ""
                city = ""
                country = ""

                # Check for postal code
                if "#" in fields[-1]:
                    postal_code = fields.pop(-1)

                # Extract city and country
                if fields:
                    city = fields.pop(0)
                if fields:
                    country = " ".join(fields)

                # Append data to the list
                data.append([current_division, dojo_name, postal_code, city, country])

    # Write data to a spreadsheet
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Division", "Dojo Name", "Postal Code", "City", "Country"])  # Write header
        writer.writerows(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
