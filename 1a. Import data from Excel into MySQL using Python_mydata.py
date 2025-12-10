#https://www.youtube.com/watch?v=YLXFEQLCogM

#CREATE TABLE IN MYSQL DB: create table employee_banc (empl_id int,
# fname char(20), lname char(15));



import xlrd
import MySQLdb


# Open the workbook and define the worksheet
book = xlrd.open_workbook("Employee_banc.xlsx")
sheet = book.sheet_by_name("Sheet1")

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "7...x", db = "banc")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()


#in the table 'employee' there are 18 rows. Columns: emp_id, fname, lname,
#start_date, end_date, superior_emp_id, dept_id, title, assigned_branch_id

# Create the INSERT INTO sql query
query = """INSERT INTO employee_banc (empl_id, fname, lname) VALUES (%s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2
# to skip the headers
for r in range(1, sheet.nrows):
      empl_id      = sheet.cell(r,0).value
      fname = sheet.cell(r,1).value
      lname          = sheet.cell(r,2).value
      

      # Assign values from each row
      values = (empl_id, fname, lname)

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

