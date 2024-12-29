
def show_student(**std):
    print(type(std))
    print(f"Hello {std['name']}")
    print(f"Umur saya {std['age']}")
    print(f"Alamat saya di {std['address']}")
    print(f"food saya di {std['food']}")

show_student(
    name="taruna",
    age=22,
    address="Jakarta",
    hobbies= ['A', 'B', 'C', 'D']
)