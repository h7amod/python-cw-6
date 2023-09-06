# write your code here
def check_hobbies(person):
    if len(person['hobbies']) > 3:
        print('WOW YOU ARE AMAZING')

if __name__ == "__main__":

    person = {
        'name': 'John',
        'age': 30,
        'hobbies': ['reading', 'swimming', 'cooking']
    }

    print(person['name'])
    print(person['age'])

    person['age'] = 35
    person['country'] = 'USA'
    print(person)
    print(len(person))

    person['hobbies'].append('painting')
    check_hobbies(person)