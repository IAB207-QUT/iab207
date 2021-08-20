from datetime import datetime
from travel.user import User
from travel.user import FrequentTraveller
from travel.booking import Booking
from travel.city import City

print('Creating a user named Jill')
user1 = User()
user1.register('jill','iueo','jill@y.com')
print(user1)

print('################')

print('Creating a frequent traveller named Jack')
su = FrequentTraveller()
su.register('jack','iituri', 'jack@x.com',123231)
print(su)

print('###############')

print('Creating a city Brisbane')
brisbane = City('Brisbane', 'City in Queensland with a good weather')
print(brisbane)

st_date = datetime(2019,11,23)
end_date = datetime(2019,11,30)

print('Creating a booking for user')
booking = Booking(st_date,end_date,brisbane,user1)
print('#################')
print(booking)

print('#################')
print("Access City description of booking: " , booking.city.description)