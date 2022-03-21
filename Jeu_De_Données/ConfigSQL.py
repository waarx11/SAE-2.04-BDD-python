import pandas as pd
import psycopg2 as psy

data=pd.read_csv(r'riot_champion.csv')
data2=pd.read_csv(r'riot_item.csv')
df=pd.DataFrame(data)
df2=df.drop_duplicates()
df3=df2.dropna()

co=None
try:
    co = psy.connect(host='berlin',
                    database='',
                    user='',
                    password=)
    curs = co.cursor()

    curs.execute('''DROP TABLE IF EXISTS Formule;''')

    curs.execute('''CREATE TABLE LOL-Champion(


    );
    '''
    )

    curs.execute('''CREATE TABLE LOL-Item(


    );
    '''
    )

    for row in df.itertuples():
        curs.execute('''INSERT INTO LOL-Champion VALUES(); ''';
        ())



    co.commit()
    curs.close()


except(Exception, psy.DatabaseError) as error:
    print(error)
finally:
    if co is not None:
        co.close()





























