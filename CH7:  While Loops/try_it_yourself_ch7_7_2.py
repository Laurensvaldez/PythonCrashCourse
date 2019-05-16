table_request = input("How many people are in your dinner group? ")
table_request = int(table_request)

if table_request > 8:
    print("Sorry, you will have to wait for a table.")
else:
    print("Your table is ready, please follow me.")