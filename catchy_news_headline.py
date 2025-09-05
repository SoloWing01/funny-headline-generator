import random as r

subjects = ["The cat", "A teacher", "My friend", "The police officer", "An astronaut"]
actions = ["runs", "teaches", "jumps", "explores", "writes"]
places_or_things = ["the park", "a spaceship", "the classroom", "a mountain", "the library"]

# sub=r.choices(subjects)
# print(sub)

def crazy_headline():
    sub=str(r.choices(subjects))
    act=str(r.choices(actions))
    pla=str(r.choice(places_or_things))
    headline=f'{sub} {act} {pla}'
    return headline

def store(headline):
    with open('saved_headline.txt',mode='a') as file:
        file.write(headline+'\n')

def main():
    while True:
        headline=crazy_headline()
        choice=input('1 for another headline, 2 for save and 3 for exit : ')
        match choice:
            case '1':
                print(str(headline))
            case '2':
                store(headline)
            case '3':
                break
            case _:
                print('invalid input')

if __name__ == '__main__':
    h1=crazy_headline()
    print(h1)
    main()