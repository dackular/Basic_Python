age = 34
age_str = str(age)
print("You are " + age_str)
print("-------------------")
print(f"You are {age}")
print("-------------------")


name = "Jose"
greeting = f"How are you, {name}?"
print(greeting)
print("-------------------")
name = "Bob"
print(greeting)

print("-------------------")


name = "Abc"
final_greeting = "How are you, {}?"
abc_greeting = final_greeting.format(name)
print(abc_greeting)

name = "Def"
def_greeting = final_greeting.format(name)
print(def_greeting)