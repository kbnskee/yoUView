db_engine=False
db_name=False
db_user=False
db_password=False
db_host=False
db_port=False





def set_database(
    ENGINE=False,
    NAME=False,
    USER=False,
    PASSWORD=False,
    HOST=False,
    PORT=False,):
    if ENGINE == False:
        print(f"ENGINE status is False.")
    else:
        db_engine = ENGINE

    if NAME == False:
        print(f"NAME status is False.")
    else:
        db_name=NAME

    if USER == False:
        print(f"USER status is False.")
    else:
        db_user=USER

    if PASSWORD == False:
        print(f"PASSWORD status is False.")
    else:
        db_password=PASSWORD

    if HOST == False:
        print(f"HOST status is False.")
    else:
        db_host=HOST

    if PORT == False:
        print(f"PORT status is False.")
    else:
        db_port=PORT


def check_connection():
    print(f"{db_engine} : {db_name} : {db_user} : {db_host} : {db_port}")


# python setup.py sdist bdist_wheel
# https://github.com/kbnskee/youview.git
