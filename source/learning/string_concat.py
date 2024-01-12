'''
String concat
'''
first_name= "Akira"
last_name= "Toriyama"

full_name_1= first_name+ " "+ last_name

full_name_2= '%s %s' % (first_name, last_name)

full_name_3= "{} {}".format(first_name, last_name)

full_name_4= f"{first_name} {last_name}"

assert full_name_1 == full_name_2 == full_name_3 == full_name_4