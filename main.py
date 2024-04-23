#!python
from faker import Faker
# fake = Faker(['it_IT', 'en_US', 'ja_JP'])
# fake = Faker()
fake = Faker(['en_US'])

# res = fake.name()
# print(res)


for x in range(10):
  x = x + 1
  print("Number : {} - {} ".format( x, fake.name()))
  