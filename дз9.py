from pprint import pprint

CONTACTS = {}


def input_error(func):
   
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Ви ввели не вірне ім'я"
        except TypeError:
            return "Ви ввели не вірний форат команди"
        except IndexError:
            return "Введіть ім'я та телефон"
        except ValueError as e:
            return e.args[0]
        except Exception as e:
            return e.args

    return wrapper

@input_error
def quit_func():
    
    return('Good bye!')




@input_error
def hello_contact():
   return('How can I help you?')



@input_error
def add_contact (name_telephone):
    lst_name_telefon = name_telephone.strip().split()
    name = lst_name_telefon[0]
    if name in CONTACTS:
        raise ValueError("Ім'я вже є у списку. Введіть іньше")
    telephone = lst_name_telefon[1]
    CONTACTS[name] = telephone
    return f'Для {name} записан телефон {telephone}'    




@input_error
def show_all():
    return '\n'.join([f'{name} {telephone}' for name, telephone in CONTACTS.items()])



    

@input_error
def change_contact(name_telephone):
    lst_name_telefon = name_telephone.strip().split()
    name = lst_name_telefon[0]
    telephone = lst_name_telefon[1]
    old_telefone = CONTACTS[name]
    CONTACTS[name] = telephone
    return f'Для {name} змінено телефон {old_telefone} на {telephone}'







@input_error
def phone_contact(name):
     telephone = CONTACTS[name.strip()]
     return telephone

@input_error
def command_error():
    return 


def get_answer_function(answer):
    
    return COMMANDS.get(answer, command_error)



@input_error
def run_command(user_command):
    command = user_command
    params = ''
    for key in COMMANDS:
        if user_command.lower().startswith(key):
            command = key
            params = user_command[len(command):]
            break
    if params:
        return get_answer_function(command)(params)
    else:
        return get_answer_function(command)()



COMMANDS = {
   'hello': hello_contact,
    'add': add_contact,
    'change': change_contact,
    'phone': phone_contact,
    'show all': show_all,
    'exit': quit_func,
    'good bye': quit_func,
    'close': quit_func
}

def main():
    while True:
        user_command = input('Введіть команду для бота: ')
        answer = run_command(user_command.strip())
        print(answer)
        if answer == 'Good bye!':
            break

if __name__ == "__main__":
    main()