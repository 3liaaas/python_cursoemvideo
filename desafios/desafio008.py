medida = float(input('Digite um valor em metros: '))
cm = medida * 100
mm = medida * 1000
dec = medida * 10
km = medida / 1000
hc = medida / 100
dam = medida / 10

print(f'A medida de {medida}m corresponde a \n {cm:.0f}cm \n {mm:.0f}mm \n {dec}dec \n {km}Km \n {hc}hc \n {dam}dam')