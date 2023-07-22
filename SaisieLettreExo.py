lettre=input('Saisissez une lettre : ')
if lettre in ('aeiouy'):
    print('La lettre',lettre,'est une voyelle')
elif lettre in ('AEIOUY'):
    print('La lettre',lettre,'est une voyelle')
else:
    print('La lettre',lettre,'est une consonne')
    input('appuyez sur entrer pour quitter')