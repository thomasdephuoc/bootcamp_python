import getopt, sys

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
for language, inventor in languages.items():
    print(f'{language} was created by {inventor}')