from collections import defaultdict
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd

if __name__ == "__main__":

    test_data = defaultdict(list)

    for i in range(5000000):
        test_data["pk"].append(i)
        test_data["id"].append(str(100*i+1))
        test_data["title"].append("TestTitle"+str(i))
        test_data["description"].append("Testdescription"+str(i))
        test_data["published_timestamp"].append(datetime.now())
        test_data["last_update_timestamp"].append(datetime.now())

    df_test_data = pd.DataFrame(test_data)

    engine = create_engine('postgresql+psycopg2://postgres:Sulfi5687@localhost/testdb')

    df_test_data.to_sql('testapps', con=engine, index=False)

