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
