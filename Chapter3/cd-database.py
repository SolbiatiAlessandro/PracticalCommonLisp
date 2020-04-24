record = []
def insert_record(name, rating):
    record.append({
        'name':name,
        'rating':rating
        })

def select_by_name(name):
    return filter(lambda x: x['name'] == name, record)

def select_by_name_iter(name):
    return [r for r in record if r['name'] == name]

def select(where):
    return filter(where, record)

def name_where(name):
    return lambda x: x['name'] == name

def where(field, value):
    return lambda x: x[field] == value

# NON FUNCTIONAL
def select_generic(field, value):
    return filter(where(field, value), record)

# FUNCTIONAL
# >>> select(where('asd', 'asg'))

"""
I can't do this cause lambda is statless
def update(where_field, where_value, set_field, set_value):
    map(lambda x: x[set_field] = set_value, select(where(where_field, where_value)))
"""

# TODO: finish
def update(where_field, where_value, set_field, set_value):
    map(
            lambda row: row if where(where_field, where_value)(row) else row
        )



if __name__ == "__main__":
    insert_record("aa", 1)
    insert_record("bb", 2)
    assert select_by_name("aa")[0]['rating'] == 1
    assert select_by_name_iter("aa")[0]['rating'] == 1
    assert select(name_where("aa"))[0]['rating'] == 1
    assert select_generic('name', 'aa')[0]['rating'] == 1
