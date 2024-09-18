metros = float(input('Digite um valor em metros:'))
mm = metros * 1000
cm = metros * 100
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000

print('Em milímetros {}mn \nEm centímetros {}cm\nEm decímetros {} \nEm decâmetro {} \nEm hektômetro {} \nEm Quilômetros {}'.format(mm, cm, dm, dam, hm, km))
