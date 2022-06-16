import psycopg2
from config import Config


class Request:
    @staticmethod
    def __connect_to_db():
        try:
            connection = psycopg2.connect(
                host=Config.hostname,
                dbname=Config.pg_db_name,
                user=Config.pg_username,
                password=Config.pg_password,
                port=Config.pg_port_id
            )
            if connection:
                return connection
            else:
                raise Exception

        except Exception as ex:
            print(ex)

    @staticmethod
    def send_request(request, is_need_response):
        connection = Request.__connect_to_db()

        try:
            with connection.cursor() as cursor:
                cursor.execute(request)
                connection.commit()

            if (is_need_response):
                return cursor.fetchall()
            else:
                return True

        except Exception as ex:
            print(ex)
        finally:
            connection.close()