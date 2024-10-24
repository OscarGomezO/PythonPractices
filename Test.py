onemilla = 1609.344		#Una milla a metros
onegallon = 3.785411784	#Un galón a litros

def liters_100km_to_miles_gallon(liters):
    result = (100 * onegallon) / (liters * (onemilla/1000))
    return result

def miles_gallon_to_liters_100km(miles):
    result = (100 * onegallon)/ (miles * (onemilla/1000))
    return result

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))



                     
#print(is_prime(1))
