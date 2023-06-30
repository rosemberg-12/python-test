'''
Data types
'''

'''
Numeric types: int, float, complex
'''

int_variable=100
float_variable=99.9
complex_variable=82j

print(int_variable, type(int_variable))
print(float_variable, type(float_variable))
print(complex_variable, type(complex_variable))

'''
String types: String
'''

single_quote='Hi'
double_quote="Hello"

print(single_quote)
print(double_quote)

'''
List types: list, tuple, range
'''

# LIST = Mutable

numeric_list=[0,1,2,3,4,5]
string_list=["apple", "windows", "linux"]
mixed_list=["pop", 4, "push", 5]

print(numeric_list)
print(numeric_list[3])

print(string_list)
print(string_list[0])

print(mixed_list)
print(mixed_list[2])

# TUPLE = Inmmutable

numeric_tuple=(1,2,3)
string_tuple=("aws", "google", "azure")
mixed_tuple=("stack", 4, "deque", 5)

print(numeric_tuple)
print(numeric_tuple[2])

print(string_tuple)
print(string_tuple[0])

print(mixed_tuple)
print(mixed_tuple[2])


# RANGE

single_range= range(4)
print(single_range)

range_with_start= range(2,4)
print(range_with_start)

range_with_interval= range(0,10,3)
print(range_with_interval)