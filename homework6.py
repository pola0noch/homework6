# Домашнее задание по теме "Словари и множества"
my_dict = {"Kate": 1999, "Kirill": 1996, "Nina": 1997}
print("Dict:",my_dict)
print("Existing value:",my_dict["Kate"])
print("Not existing value:",my_dict.get("Roma"))
my_dict.update({"Tom": 1991,"Anna": 1979})
#del my_dict["Tom"]
a = my_dict.pop("Tom")
print("Deleted value:",a)
print("Modified dictionary:",my_dict)

my_set = {1,2,True,"Kirill",2,2,"Kirill",3,3,3}
print("Set:",set(my_set))
my_set.update([(5,6,7),"Kate"])
print("Modified set:",my_set)