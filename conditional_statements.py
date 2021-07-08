
weight = int(input('your weight'))
kg_or_pounds = input('K or P')

if  kg_or_pounds.upper() == 'K':

    result = weight * 2.2
    type_of = 'Pounds'

elif  kg_or_pounds.upper() == 'P':

     result = weight / 2.2
     type_of= 'Kilograms'

else: 

    result = 'Please choose K or P'
   
print(f'your weight in {type_of} is {round(result)}')