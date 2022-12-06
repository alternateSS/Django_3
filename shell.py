from credit.models import Client, Account, Credit
from random import randint

client = Client.objects.create(name='Бердиев Н.Д.', birth_year='1994-11-09', work_place='Codify')
client_2 = Client.objects.create(name='Нурлан', birth_year='1986-08-02', work_place='Godify')

acc1 = client.accounts.create(number=randint(1000000000000000, 9999999999999999), account_type=1)
acc2 = client.accounts.create(number=randint(1000000000000000, 9999999999999999), account_type=1)
acc3 = client_2.accounts.create(number=randint(1000000000000000, 9999999999999999), account_type=2)
acc4 = client_2.accounts.create(number=randint(1000000000000000, 9999999999999999), account_type=2)

credit1 = acc1.credits.create(sum=2555)
credit1 = acc2.credits.create(sum=25355)
credit1 = acc3.credits.create(sum=25545)
credit1 = acc4.credits.create(sum=25555)

