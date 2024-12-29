from pprint import pprint

car = {
    'brand' : 'ford',
    'model': 'mustang',
    'year' : 2012
}

car['year'] = 2015
car['color'] = 'blue'

pprint(car)

car.update({
    'model' : 'BMW'
})

pprint(car)


