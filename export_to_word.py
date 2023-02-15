from django.db.backends.mysql.base import DatabaseWrapper

from appeals import models as m1
from portfolio import models as m2
from recyclables import models as m3
from users import models as m4

data_types = {
    **DatabaseWrapper.data_types,
    'ForeignKey': 'integer',
    'ImageField': 'char(60)',
}

def know_sql(inde):
    return data_types[inde]

def read_about(thing):
    for i in dir(thing):
        print(i, ':', getattr(thing, i))

def print_table(table):
    print(('\n'*2)+str(table._meta).replace('.', "_"))
    print('Имя поля', 'Расшифровка', "Ключ", "Тип данных", sep='\\t')
    for i in table._meta.fields:
        # print('\n' * 99)
        # print(i)
        #read_about(i)
        sql_type = str(i.__class__).rsplit('.')[-1][:-2]
        key = "PK" if i.primary_key else "FK" if sql_type=='ForeignKey' else ''
        sql_type = know_sql(sql_type).split(" ")[0]
        if i.max_length:
            sql_type = sql_type.replace("%(max_length)s", str(i.max_length))

        print(i.name,i.verbose_name, key, sql_type, sep='\\t')
        # print(1, i.db_type(connection))
        # if not i.primary_key:
        #    assert 0

print('\n'*99)
def get_all(*ms):
    for m in ms:
        for i in dir(m):
            i = getattr(m, i)

            try:
                # print(i.__module__, __name__)
                if hasattr(i, 'id') and issubclass(i, m.models.Model):
                    yield i#print_table(i())
            except Exception as e:
                print(repr(e))
def read_all(m):

    for i in m:
        # i = getattr(m, i)

        try:
            # print(i.__module__, __name__)
            if hasattr(i, 'id') and issubclass(i, m1.models.Model):
                print_table(i())
        except Exception as e:
            print(repr(e))

    # assert 0

# print_table(m.Event())
read_all(get_all(m1, m2, m3, m4))

print("\n"*4)

assert 0