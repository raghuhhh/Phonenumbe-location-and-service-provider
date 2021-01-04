'''
initially you need to install the phonenumber librarry by the commad "pipo install phonenumber" in the terminal

'''

import phonenumbers 
'''
this is imported from the phonenumbers library
'''

 
from phonenumbers import carrier 
'''
we need carrier to know the service provider
like Vi,Jio,BSNL,....
inorder to know carrier name we import carrier lib from phonenumbers lib
'''

service_provider = phonenumbers.parse("+919704038024") 

'''
we need to enter the phone number specifically with the country code
'''
	

print(carrier.name_for_number(service_provider,'en')) 
'''
it prints the service provider
'''
from phonenumbers import geocoder 

'''
inorder to know location name we import geocoder lib from phonenumbers lib
'''
   
phone_number = phonenumbers.parse("+919704038024")  
 
print(geocoder.description_for_number(phone_number,'en'))    

#it prints the name of the phone numnber located