import pydantic
import enum
import typing

T = typing.TypeVar("T", bound=enum.Enum)

def map_str_to_reconocer_source(
    cls: typing.Any, value: str, enum_cls: typing.Type[T], separator: str= "-"
) -> typing.List[T]:
        enum_list: typing.List[T] = [
            enum_cls(item)
            for item in value.split(separator)
            if item in enum_cls._value2member_map_
        ]
        return enum_list


def map_str_to_enum_list2(field: str, enum_cls: typing.Type[T], separator: str= "-"
) -> typing.List[T]:
    print("map in action")
    def wrapper(cls, value: str)-> typing.List[T]:
        print(f"map in action 2 with {value}")
        enum_list: typing.List[T] = [
            enum_cls(item)
            for item in value.split(separator)
            if item in enum_cls._value2member_map_
        ]
        print(enum_list)
        return enum_list
    return pydantic.validator(field, pre=True, allow_reuse=True)(wrapper)


class ExampleEnum(enum.Enum):
    value1= "1"
    value2= "2"
    value3= "3"

class ExampleEnum2(enum.Enum):
    valueA= "A"
    valueB= "B"
    valueC= "C"

#@map_str_to_enum_list(field="enum", enum_cls=ExampleEnum, separator=",")
class ModelExample(pydantic.BaseModel):
    enum: typing.List[ExampleEnum]
    _map_enum= map_str_to_enum_list2("enum", ExampleEnum, ",")


#print(map_str_to_reconocer_source(None, "1,3,2,2,2", ExampleEnum, ","))

entry= {
     "enum": "1,2,3"
}
print(ModelExample.parse_obj(entry))