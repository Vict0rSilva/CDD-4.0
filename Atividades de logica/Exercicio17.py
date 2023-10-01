hora_dinicio = int(input("Hora de inicio: "))
hora_dfim = int(input("Hora de fim: "))

if hora_dinicio <= hora_dfim:
    duracao = hora_dfim - hora_dinicio
else:
    duracao = 24 - hora_dinicio + hora_dfim

print(f"O jogo durou {duracao}hrs")