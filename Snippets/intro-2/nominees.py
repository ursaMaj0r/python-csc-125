import csv

winning_title = input('Winning title: ')

with open('nominees.csv', newline='') as f:
    for line in csv.DictReader(f):
        if line['title'] == winning_title:
            print('Congratulations:', line['director(s)'])
