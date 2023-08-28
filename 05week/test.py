from datetime import datetime
from travel.user import User
from travel.user import FrequentTraveller
from travel.booking import Booking
from travel.city import City

print('Creating a user named Jill')
user = User()
user.register('jill','hash123','jill@google.com')
print(user)

print('################')

print('Creating a frequent traveller named Jack')
freq_user = FrequentTraveller()
freq_user.register('jack','pass123', 'jack@google.com', 123231)
print(freq_user)

print('###############')

print('Creating a city Brisbane')
brisbane = City('Brisbane', 'City in Queensland with a good weather')
print(brisbane)

start_date = datetime(2023,11,23,10,0,0)#what is ISO 8601 format?
end_date = datetime(2023,11,30,10,0,0)

print('Creating a booking for user')
booking = Booking(start_date, end_date, brisbane, user)
print('#################')
print(booking)

print('#################')
print("Access City description of Booking: ", booking.city.description)