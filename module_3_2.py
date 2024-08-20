def send_email(message, recipient, sender ='university.help@gmail.com'):

    if ("@" and (".com" or ".ru" or ".net")) not in (sender or recipient):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
            print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
            print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)

send_email(1,  'money@gmail.com')

send_email(1, 'urban.teacher@mail.uk', 'university.help@gail.com')
send_email(1,'money@gmail.com', 'pochta@ru')
send_email(1,'university.help@gmail.com', 'university.help@gmail.com' )





