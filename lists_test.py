
user_input = input('enter integers but leave spaces ')
integers = [int(i) for i in user_input.split()] # split the integers using split() which splits after every whitespce 
sum_of_integers = sum(integers)
print(f'sum of the integers {sum_of_integers}')# i learnt about fstring which allows you to dynamically compose a string by adding python expressions using {} which is beautiful

## tuple assignment
favourite_books = {'Hyper Focus', 'the Alchemist', 'the Daily Laws', 'Rich Dad Poor Dad'}
for favourite_book in favourite_books:
    print(favourite_book)

profile_user ={}
profile_user['name'] = input('Enter your name ')
profile_user['age'] = input('Enter your age ')
profile_user['color'] = input('Enter your favourite color ')
print(profile_user)

num_input = input('Enter integers but leave spaces ')
first_set = {int(num) for num in num_input.split()}
print(first_set)
nap_input = input('Enter integers but leave spaces ')
second_set = {int(num) for num in nap_input.split()}
print(second_set)

print(first_set | second_set)

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Original list of words:", words)
print("Words with odd length:", odd_length_words)

