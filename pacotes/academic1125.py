trabalho = float(input())
prova = float(input())

media = (trabalho + prova)/2

if (media < 6):
  if((trabalho + 10)/2>=6):
    print('talvez com a sub')
  else:
    print('reprovado')
  
else:
  print('aprovado')