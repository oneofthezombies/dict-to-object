import dicttoobject


a = {
    "b": 1
}
b = dicttoobject.dict_to_readonly_object(a)
c = dicttoobject.dict_to_writable_object(a)
d = dicttoobject.object_to_dict(b)
e = dicttoobject.object_to_dict(c)
print(a)
print(b)
print(c)
print(d)
print(e)
try:
    b.b = 2
except dicttoobject.DoNotWriteError as e:
    print(e.attr_name)
    print(e.attr_value)
