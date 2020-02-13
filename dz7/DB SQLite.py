import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE Employee(
        Employee_id integer PRIMARY KEY NOT NULL, 
        name text NOT NULL,
        address text NOT NULL, 
        city text NOT NULL, 
        contact integer NOT NULL, 
        email text)"""
               )
cursor.execute("""
    INSERT INTO Employee VALUES (
        '1000000001', 'John Smith', '200 Maple Lane', 'Detroit', '44444', 'sales@villagetoys.com')"""
               )
cursor.execute("""
    INSERT INTO Employee VALUES (
        '1000000002', 'Denise L. Stephens', '333 South Lake Drive', 'Columbus', '43333', 'dstephens@fun4all.com')"""
               )
cursor.execute("""
    INSERT INTO Employee VALUES (
        '1000000003', 'Jim Jones', '829 Riverside Drive', 'Phoenix', '88888', 'jjones@fun4all.com')"""
               )
conn.commit()
cursor.execute("SELECT name FROM Employee")
results1 = cursor.fetchall()
print(results1)


cursor.execute("""
    CREATE TABLE Salary(
        Salary_id integer PRIMARY KEY NOT NULL,
        Employee_id integer NOT NULL,
        name text NOT NULL, 
        base rate integer NOT NULL,
        bonus integer NOT NULL,
        FOREIGN KEY (Employee_id) REFERENCES Employee (Employee_id))"""
               )
cursor.execute("""
    INSERT INTO Salary VALUES (
        '001', '1000000001', 'John Smith', '10000', '8000')"""
               )
cursor.execute("""
    INSERT INTO Salary VALUES (
        '002', '1000000002', 'Denise L. Stephens', '25000', '10000')"""
               )
cursor.execute("""
    INSERT INTO Salary VALUES (
        '003', '1000000003', 'Jim Jones', '8000', '7000')"""
               )
conn.commit()
cursor.execute("SELECT base rate FROM Salary")
results2 = cursor.fetchall()
print(results2)


cursor.execute("""
    CREATE TABLE Position(
        Position_id integer PRIMARY KEY NOT NULL,
        Employee_id integer NOT NULL,
        name text NOT NULL,
        status text NOT NULL,
        company_department text NOT NULL,
        city text, 
        contact integer,
        FOREIGN KEY (Employee_id) REFERENCES Employee (Employee_id))"""
               )
cursor.execute("""
    INSERT INTO Position VALUES (
        '1', '1000000001', 'John Smith', 'Company member', 'Executive department', 'Detroit', '44444')"""
               )
cursor.execute("""
    INSERT INTO Position VALUES (
        '2', '1000000002', 'Denise L. Stephens', 'Department head', 'Main department', 'Columbus', '43333')"""
               )
cursor.execute("""
    INSERT INTO Position VALUES (
        '3', '1000000003', 'Jim Jones', 'Company member', 'Executive department', 'Phoenix', '88888')"""
               )
conn.commit()
cursor.execute("SELECT status FROM Position")
results3 = cursor.fetchall()
print(results3)

conn.close()