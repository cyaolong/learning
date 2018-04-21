#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# def display_message():
#     print("I'm learning Python.")

# display_message()


# def favorite_book(title):
#     print("One of my favorite books is" + title)

# favorite_book(' Sherlock Holmes')


# def describe_pet(pet_name, animal_type='dog'):
#     print('I have a ' + animal_type + '.')
#     print('My ' + animal_type + "'s name is " + pet_name + '.')

# describe_pet('harry')


#8-3/8-4
# def make_shirt(size, content):
#     print('T-shirt is to be make in '+size+','+'and its content is about '+content+'.')

# make_shirt('76A', 'I love Python')
# make_shirt(content='I love Python', size='80C')


#8-5
# def describe_city(name, country=' China'):
#     print(name + 'is in' + country + '.')

# describe_city('Beijing ')
# describe_city('New York ', ' USA')
# describe_city('Manko ', ' Thailand')


# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return(full_name.title())

# astronaut = get_formatted_name('ken', 'vincent')
# print(astronaut)

# def build_person(first_name, last_name, age=''):
#     person = {'first':first_name, 'last':last_name}
#     if age:
#         person['age'] = age
#     return person

# person = build_person('Ken', 'Vincent', age=30)
# print(person)

# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     print(full_name.title())

# while True:
#     print('Please tell me your name.You Could press ''q'' at any time to quit.')
#     f_name = input('First name is: ')
#     if f_name == 'q':
#         break
#     l_name = input('Last name is: ')
#     if l_name == 'q':
#         break

#     get_formatted_name(f_name, l_name)


#8-6
# def city_country(city, country):
#     print(city + ', ' + country)

# city_country(city='Santiago',country='Chile')
# city_country(city='Beijing',country='China')
# city_country(city='San Francisco',country='USA')


#8-7/8-8
# def make_album(singer_name, album_name, song_num=''):
#     album = {'singer':singer_name, 'album':album_name}
#     if song_num:
#         album['songs'] = song_num
#     print (album)

# make_album('Jackie', 'abc', song_num=8)
# make_album('Cheung', 'cdf')
# make_album('Ken', 'efg')

# while True:
#     print('Please enter an album info(or ''q'' to quit)')
#     a_name = input('Please enter an album(or ''q'' to quit): ')
#     if a_name == 'q':
#         break
#     s_name = input('Please enter a singer(or ''q'' to quit): ')
#     if a_name == 'q':
#         break
#     make_album(a_name,s_name)

# def greet_users(names):
#     for name in names:
#         print ('Hello, ' + name.title() + '!')

# names = ['Ken', 'Vincent', 'Nuke']
# greet_users(names)

#p127
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print (current_design + ' is printing!')
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print ('\nThe following model has been printed:')
#     for completed_model in completed_models:
#         print (completed_model)

# unprinted_designs = ['iPhone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# [:]表示创建副本，不影响原有列表
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print unprinted_designs

#8-9/8-10/8-11
# magicians =['Ken', 'Vincent', 'Van Gogh']
# great_magicians = []
# def show_magicians(magicians):
#     for magician in magicians:
#         print (magician)

# def make_great(magicians, great_magicians):
#     while magicians:
#         current_magician = magicians.pop()
#         great_magicians.append(current_magician + ' the Great')

#     for magician in great_magicians:
#         print (magician)

# make_great(magicians[:], great_magicians)
# for magician in magicians:
#     print (magician)

# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last

#     for k,v in user_info.items():
#         profile[k] = v
#     return profile

# user_profile = build_profile('Ken', 'Vincent', profession='PM', age='30')
# print (user_profile)

#8-12
# def add_food(*foods):
#     print('Customer A has order a Sandwich with ')
#     for food in foods:
#         print(' - ' + food)

# add_food('vegetables','meat','beef')

#8-13
# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for k,v in user_info.items():
#         profile[k] = v
#     return profile

# user_profile = build_profile('Ken', 'Vincent', age='30',profession='PM',location='Guangzhou')
# for info in user_profile:
#     print(info + ': ' + user_profile[info])

#8-14
def make_car(manufacture, model, **car_info):
    profile = {}
    profile['manufacture_name'] = manufacture
    profile['model_name'] = model
    for k,v in car_info.items():
        profile[k] = v
    return profile

car = make_car('Audi', 'A6L', color='blue', tow_package='True')
print(car)