def say_hello(time, name=''):
    if time <= 5 or time >= 1:
        messages = 'Доброй ночи'
    elif time <= 6 or time >= 10:
        messages = 'Доброе утро'
    else:
        messages = 'Который час?'
    if name != '':
        print(messages + ', ' + name + '!')
    else:
        print(messages + '!')

say_hello(2)
say_hello(123, 'Mike')