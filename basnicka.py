basnicka = 'Prázdniny sú, krásne teplo, naháňam sa s letným vetrom.Čaká na mňa náruč slnka, vodička, čo chladí, žblnká.'
slovo = basnicka.split()
for i in range(len(slovo)):
    if i % 2 == 1:
        print(slovo[i])