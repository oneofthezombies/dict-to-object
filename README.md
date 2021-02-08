# dict-to-object

```python
import dicttoobject

test_dict = {
    "key1": 1,
    "key2": {
        "key3": "value3"
    }
}

readonly_object = dicttoobject.dict_to_readonly_object(test_dict)
print(readonly_object)
try:
    readonly_object.key2 = 2
except dicttoobject.DoNotWriteError as e:
    print(e.attr_name)
    print(e.attr_value)

writable_object = dicttoobject.dict_to_writable_object(test_dict)
print(writable_object)

writable_object.key2.key3 = 3
print(writable_object.key2.key3)

writable_object.key4 = 4
print(writable_object.key4)

dict_from_readonly = dicttoobject.object_to_dict(readonly_object)
print(dict_from_readonly)

dict_from_writable = dicttoobject.object_to_dict(writable_object)
print(dict_from_writable)

```