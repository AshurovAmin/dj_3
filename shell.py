import os
import random

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking.settings')
django_asgi_app = get_asgi_application()

from credit.models import Client, Account, Credit



def generate_account_number():
    return ''.join(random.choice('0123456789') for i in range(16))


client1 = Client.objects.create(name='Бердиев Н.Д.', citizenship='КР', birth_year='1994-01-01', work_place='Codify')
client2 = Client.objects.create(name='Иванов И.Ю', citizenship='КР', birth_year='1991-03-05', work_place='Megacom')

account1_1 = Account.objects.create(number=generate_account_number(), account_type=1, client=client1)
account1_2 = Account.objects.create(number=generate_account_number(), account_type=2, client=client1)

account2_1 = Account.objects.create(number=generate_account_number(), account_type=1, client=client2)
account2_2 = Account.objects.create(number=generate_account_number(), account_type=2, client=client2)

credit1_1 = Credit.objects.create(sum=10000, account=account1_1)
credit1_2 = Credit.objects.create(sum=20000, account=account1_2)

credit2_1 = Credit.objects.create(sum=15000, account=account2_1)
credit2_2 = Credit.objects.create(sum=30000, account=account2_2)
