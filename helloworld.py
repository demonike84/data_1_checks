performances = ['Ventriloquism' , 'Amazing Acrobatics']
performances.append('Snake Charmer')
performances.remove('Ventriloquism') 
print performances

-----------------------------------------------

performances = {'Ventriloquism': '9:00am',
                'Snake Charmer': '12:00pm',
                'Amazing Acrobatics': '2:00pm',
                'Bearded Lady': '5:00pm'}


showtime = performances.get('Bearded Lady')

if showtime:
    print('The time of the Bearded Lady show is', performances['Bearded Lady'])

else :
    print "The show doesn't exist"