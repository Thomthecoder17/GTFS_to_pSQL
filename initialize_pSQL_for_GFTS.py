# Helps set up a simple sql file to initialize the database. Certain additional fields can be added to the file as needed.
# For example, the included sql file in the repository is set up to use postGIS, and therefore has lines added in accordingly.

import glob
import csv

FOLDER_PATH = "formatFeed\\"

with open("initialize_pSQL_for_GTFS", "a") as sqlFile:
    for file in glob.glob(FOLDER_PATH + "*.txt"):
        table = file.split(FOLDER_PATH)[1].split(".")[0]
        with open(file) as csvFile:
            csvReader = csv.DictReader(csvFile)
            keys = csvReader.fieldnames
            fields = ", \n".join([("    " + key + " TEXT") for key in keys])
            sqlFile.write(f"CREATE TABLE {table} (\n{fields}\n);\n\n")          