#Login system using if else and elif statements.
print("===Login===")
print()
print()
US = input("Username: ")
PS = input("Password: ")
print()
print()
if US == "Mark" and PS == "Mark1234":
    print("""Welcome mark!!! How are you today?
          Dont forget to stay Hydrated""")
elif US == "John" and PS == "John123":
    print("""Welcome John!!! how are you today?
          Dont forget to eat food.""")
elif US == "Hannah" and PS == "H123":
    print("""Welcome Hannah!!! Hoe are you?
          Be nice""")
else:
    print("GO AWAY, WHO EVEN ARE YOU??!?!?!?!??")