from faker import Faker
fake = Faker('pt-br')

def sobrenomeordem(Name, Sobrenome1, Sobrenome2 ):
        
    if( len(Sobrenome1) <len(Sobrenome2) ):
        return Name  +  ' '  +  Sobrenome1  +  ' '  +  Sobrenome2
    else:
        return Name  +  ' '  +  Sobrenome2   +  ' '   +   Sobrenome1
    
print(sobrenomeordem(fake.first_name(),  fake.last_name(),  fake.last_name()))

print(sobrenomeordem(fake.first_name(),  fake.last_name(),  fake.last_name()))

