import datetime
import random

from data import post_name, post_description, employee_name, employee_surname, care_process, inventory_name

my_file = open("out.txt", "w")
cleaner = []

def generate_datetime(min_year: int, max_year: int):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime.date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + datetime.timedelta(days=365 * years)
    return str(start + (end - start) * random.random())[0:19]

def generate_storage(n: int):
    res = "INSERT INTO storage (empty_containers, location, full_containers, fish_quantity, food_quantity, date) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(0, 20)) + \
               ", \'Рыбная ул. " + str(random.randint(1, 70)) + \
               "\', " + str(random.randint(0, 100)) + \
               ", " + str(random.randint(0, 20)) + \
               ", " + str(random.randint(0, 100)) + \
               ", \'" + generate_datetime(2021, datetime.datetime.now().year) + "\')"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_post(n = 4):
    res = "INSERT INTO post (name, salary, description) \nVALUES "
    for i in range(n):
        res += "(\'" + post_name[i] + \
               "\', " + str(random.randint(20000, 50000)) +\
               ", \'" + post_description[i] + "\')"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_employee(n: int, storage_count: int):
    res = "INSERT INTO employee (id_storage, id_post, name, surname, date_of_birth) \nVALUES "
    for i in range(n):
        rand = random.randint(1, len(post_name))
        res += "(" + str(random.randint(1, storage_count)) + \
            ", " + str(rand) + \
            ", \'" + employee_name[random.randint(0, 19)] + \
            "\', \'" + employee_surname[random.randint(0, 19)] + \
            "\', \'" + generate_datetime(1950, 2004) + "\')"
        if (rand == 4): cleaner.append(i+1)
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_pool(n: int):
    res = "INSERT INTO pool (location, size) \nVALUES "
    for i in range(n):
        res += "(\'Рыбная ул. " + str(random.randint(1, 70)) + \
               "\', " + str(random.randint(25, 150)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_sturgeon(n: int, pool_count: int):
    res = "INSERT INTO sturgeon (id_pool, date_of_birth) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, pool_count)) + \
            ", \'" + generate_datetime(2020, 2022) + "\')"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_pool_cleaning(n: int, pool_count: int):
    res = "INSERT INTO pool_cleaning (id_employee, id_pool, date) \nVALUES "
    for i in range(n):
        res += "(" + str(cleaner[random.randint(0, len(cleaner)-1)]) + \
            ", " + str(random.randint(1, pool_count)) + \
            ", \'" + generate_datetime(2022, 2022) + "\')"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_sturgeon_care(n: int, pool_count: int):
    res = "INSERT INTO sturgeon_care (id_pool, process, date) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, pool_count)) + \
               ", \'" + care_process[random.randint(0, len(care_process)-1)] +\
               "\', \'" + generate_datetime(2022, 2022) + "\')"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_inventory(n: int):
    res = "INSERT INTO inventory (name, quantity, date) \nVALUES "
    for i in range(n):
        res += "(\'" + inventory_name[random.randint(0, len(inventory_name)-1)] + \
               "\', " + str(random.randint(0, 5)) +\
               ", \'" + generate_datetime(2022, 2022) + "\')"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_purchasing(n: int, inventory_count: int):
    res = "INSERT INTO purchasing (id_inventory, sum, date) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, inventory_count)) + \
               ", " + str(random.randint(5000, 30000)) +\
               ", \'" + generate_datetime(2022, 2022) + "\')"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_market_request(n: int):
    res = "INSERT INTO market_request (containers_quantity_request) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(20, 100)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res

def generate_sending_containers(n: int, market_request_count: int):
    res = "INSERT INTO sending_containers (id_market_request, containers_quantity, date) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, market_request_count)) + \
               ", " + str(random.randint(20, 100)) + \
               ", \'" + generate_datetime(2022, 2022) + "\')"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_employee_sending(n: int, sending_containers_count: int, employee_count: int):
    res = "INSERT INTO employee_sending (id_sending_containers, id_employee) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, sending_containers_count)) + \
               ", " + str(random.randint(1, employee_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_storage_sending(n: int, sending_containers_count: int, storage_count: int):
    res = "INSERT INTO storage_sending (id_sending_containers, id_storage) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, sending_containers_count)) + \
               ", " + str(random.randint(1, storage_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_employee_storage(n: int, employee_count: int, storage_count: int):
    res = "INSERT INTO employee_storage (id_employee, id_storage) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, employee_count)) + \
               ", " + str(random.randint(1, storage_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_employee_sturgeon_care(n: int, employee_count: int, sturgeon_care_count: int):
    res = "INSERT INTO employee_sturgeon_care (id_employee, id_sturgeon_care) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, employee_count)) + \
               ", " + str(random.randint(1, sturgeon_care_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_sturgeon_sturgeon_care(n: int, sturgeon_care_count: int, sturgeon_count: int):
    res = "INSERT INTO sturgeon_sturgeon_care (id_sturgeon_care, id_sturgeon) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, sturgeon_care_count)) + \
               ", " + str(random.randint(1, sturgeon_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_employee_purchasing(n: int, employee_count: int, purchasing_count: int):
    res = "INSERT INTO employee_purchasing (id_employee, id_purchasing) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, employee_count)) + \
               ", " + str(random.randint(1, purchasing_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_employee_pool_cleaning(n: int, employee_count: int, pool_cleaning_count: int):
    res = "INSERT INTO employee_pool_cleaning (id_employee, id_pool_cleaning) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, employee_count)) + \
               ", " + str(random.randint(1, pool_cleaning_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_storage_inventory(n: int, storage_count: int, inventory_count: int):
    res = "INSERT INTO storage_inventory (id_storage, id_inventory) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, storage_count)) + \
               ", " + str(random.randint(1, inventory_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


def generate_storage_purchasing(n: int, storage_count: int, purchasing_count: int):
    res = "INSERT INTO storage_purchasing (id_storage, id_purchasing) \nVALUES "
    for i in range(n):
        res += "(" + str(random.randint(1, storage_count)) + \
               ", " + str(random.randint(1, purchasing_count)) + ")"
        if i == n - 1:
            res += ";\n\n"
        else:
            res += ",\n"
    return res


storage_count = 10
pool_count = 100
employee_count = 200
sturgeon_count = 10000
pool_cleaning_count = 100
care_count = 100
inventory_count = 100
purchasing_count = 100
market_request_count = 100
sending_containers_count = 100

my_file.write(generate_storage(storage_count))
my_file.write(generate_post())
my_file.write(generate_employee(employee_count, storage_count))
my_file.write(generate_pool(pool_count))
my_file.write(generate_sturgeon(sturgeon_count, pool_count))
my_file.write(generate_pool_cleaning(pool_cleaning_count, pool_count))
my_file.write(generate_sturgeon_care(care_count, pool_count))
my_file.write(generate_inventory(inventory_count))
my_file.write(generate_purchasing(purchasing_count, inventory_count))
my_file.write(generate_market_request(market_request_count))
my_file.write(generate_sending_containers(sending_containers_count, market_request_count))

my_file.write(generate_employee_sending(100, sending_containers_count, employee_count))
my_file.write(generate_storage_sending(100, sending_containers_count, storage_count))
my_file.write(generate_employee_storage(100, employee_count, storage_count))
my_file.write(generate_employee_sturgeon_care(100, employee_count, care_count))
my_file.write(generate_sturgeon_sturgeon_care(100, care_count, sturgeon_count))
my_file.write(generate_employee_purchasing(100, employee_count, purchasing_count))
my_file.write(generate_employee_pool_cleaning(100, employee_count, pool_cleaning_count))
my_file.write(generate_storage_inventory(100, storage_count, inventory_count))
my_file.write(generate_storage_purchasing(100, storage_count, purchasing_count))

my_file.close()

