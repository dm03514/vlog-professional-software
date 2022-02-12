from typing import NewType
import os
Account = NewType('Account', object)


def create_account(account_name: str) -> Account:
    # validate account name
    validate_account_name(account_name)

    if account_name.endswith('.us'):
        account_name = account_name.replace('.us', '@us')

    # check if test env
    if os.getenv('ENVIRONMENT') == 'test':
        # get the flat file account store
        account_connection = FlatFileAccountStore()
        return account_connection.get_or_create(account_name)

    # check if prod env
    else:
        # create db connection
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="Abcd1234")

        cur = conn.cursor()
        # execute statement
        try:
            cur.execute('INSERT INTO accounts (name) VALUES (?)', account_name)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

        return Account(account_name)

def validate_account_name(): pass



class FlatFileAccountStore:
    pass


class psycopg2:
    DatabaseError = None
