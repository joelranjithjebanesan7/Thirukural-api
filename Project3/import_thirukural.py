import csv
import sqlite3

def thirukural_db():
    
    conn = sqlite3.connect("/home/joelrj/Project3/thirukural.db")
    c = conn.cursor()
    with open("/home/joelrj/Downloads/indianpincode.csv","r",encoding = 'latin-1') as csv_file:
        csvReader = csv.DictReader(csv_file)
        value_db = [(i['officename'],i['pincode'],i['officetype'],i['Deliverystatus'],i['regionname'],i['circlename'],i['taluk'])for i in csvReader]
    c.executemany("INSERT INTO pincodes_pincode('officename','pincode','officetype','Deliverystatus','regionname','circlename','taluk') VALUES(?,?,?,?,?,?,?)",value_db)
    conn.commit()
    return "Data base Created"


print(pincode_db())