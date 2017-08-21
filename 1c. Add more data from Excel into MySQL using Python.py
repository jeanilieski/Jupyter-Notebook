
import xlrd
import MySQLdb


# Open the workbook and define the worksheet
book = xlrd.open_workbook("Employee_banc2.xlsx") #it was Employee_banc1 first
sheet = book.sheet_by_name("Sheet1")

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "7b48i49x", db = "banc")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()


#in the table 'employee_banc' there are 26 rows. Columns: emp_id, fname, lname.
#I added an extra column 'Gender' (it cannot be populated before being added to the table)
#cursor.execute("ALTER TABLE employee_banc ADD Gender date;)

# Create the INSERT INTO sql query
query = """INSERT INTO employee_banc (empl_id, fname, lname, Gender) VALUES (%s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2
# to skip the headers
for r in range(1, sheet.nrows):
      empl_id      = sheet.cell(r,0).value
      fname = sheet.cell(r,1).value
      lname          = sheet.cell(r,2).value
      Gender = sheet.cell(r,3).value
      

      # Assign values from each row
      values = (empl_id, fname, lname, Gender)

      # Execute sql Query
      cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done! Bye, for now."
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print "I just imported " + columns + " columns and " + rows + " rows to MySQL!"

#check in db 'select * from employee_banc'
