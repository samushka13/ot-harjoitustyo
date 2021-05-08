def read_filenames():
    with open('config.txt', 'r') as file:
        data = file.read().replace('\n', '=')
        filenames = data.split("=")

    return filenames

def database_filename():
    filenames = read_filenames()
    if ".db" in filenames[1] and len(filenames[1]) > 3:
        filename = f"{filenames[1]}"
    else:
        filename = "trivioboros.db"

    return filename

def test_database_filename():
    filenames = read_filenames()
    if ".db" in filenames[3] and len(filenames[3]) > 3:
        filename = f"{filenames[3]}"
    else:
        filename = "trivioboros_tests.db"

    return filename


DATABASE_FILENAME = database_filename()
TEST_DATABASE_FILENAME = test_database_filename()
