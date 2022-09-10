def say_hello():
    print("hello world")

def say_goodbye():
    print("goodbye world")

def say_hi():
    print("hi")

def speak(message):
    print(message)
    return message

def please_speak():
    user_message = input("please speak ")
    print(user_message)

say_hello()
say_goodbye()
say_hi()
speak("hello world")
speak("goodbye world")
hi = speak("hi")
print(hi)
# please_speak()


def add_5_and_3():
    print(5+3)

def add_2_and_7():
    print(2+7)

def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum

add_5_and_3()
add_2_and_7()
add(5, 3)
add(2, 7)
large_number = add(250, 489)

add(large_number, 4)

isaac = {
    'name': "isaac",
    'age': 13,
    'hobbies': ['programming', 'playing guitar', 'photography']
}

adam = {
    'name': 'adam',
    'age': 30,
    'hobbies': ['programming', 'piano']
}

# impure function
def modify_person_impure(person):
    person["name"] = 'diana'
    person["age"] = 16

# modify_person_impure(isaac)
# now it's actually diana!
# print('now isaac is: ', isaac)

# pure function!
def modify_person_pure(person):
    # make a COPY! of the person object!
    diana = {
        **person,
        "name": "diana",
        'age': 16,
        'surname': 'craciun',
    }
    print('new person', diana)
    print('original person', person)
    return diana

modify_person_pure(isaac)