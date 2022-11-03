import oracle_config
import oracledb

con =oracledb.connect(user=oracle_config.user, password=oracle_config.password, dsn=oracle_config.dsn)

cur = con.cursor()
cur.execute('select * from STORE.CUSTOMERS')
# rows = cur.fetchmany(1)
# print(rows)



for CUSTOMER_ID, FIRST_NAME, LAST_NAME, DOB, PHONE in cur:
    print("Department number: ", CUSTOMER_ID)
    print("Department name: ", FIRST_NAME)
    print("Department location:", LAST_NAME)
    print(DOB)
    print(PHONE)
    print("------")

print(cur.rowcount)

# cur.execute("UPDATE STORE.CUSTOMERS SET PHONE ='800-555-1215' WHERE CUSTOMER_ID ='4'")

statment = "UPDATE STORE.CUSTOMERS SET PHONE = :v WHERE CUSTOMER_ID = :n"
cur.execute(statment, {'v': '800-555-1214', 'n': '4'})
con.commit()