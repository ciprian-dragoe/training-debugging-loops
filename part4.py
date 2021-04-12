ceva = 1

def functia1():
  print('intru functia1')
  print('ies functia1')


def functia2(intentie):
  print('intru functia2')
  print('intentie: ', intentie)
  print('ies functia2')


def functia3(alta_intentie):
  print('intru functia3')
  print('alta_intentie: ', alta_intentie)
  print('ies functia3')
  return alta_intentie * 2


def functia4():
  print('intru functia4')
  functia2("argument din partea functia4")
  print('ies functia4')

functia1()
print('===========')
functia2(1)
functia2(3)
print('===========')
raspuns = functia3(2) # raspuns = 4
print(raspuns)
print(functia3(ceva)) # print(functia3(1)) # print(2)
print('===========')
functia4()
print('terminat program')