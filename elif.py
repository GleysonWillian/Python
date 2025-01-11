tenho_sede = False
tenho_fome = False
estou_em_dieta = False

if tenho_sede and tenho_fome:
    if estou_em_dieta:
        print("Vou beber suco da fruta e fazer um sanduiche natural!")
    else:
        print("Vou beber refri e comer uma pizza!")
elif tenho_sede and not(tenho_fome):
    if estou_em_dieta:
        print("Vou beber agua!")
    else:
        print("Vou beber uma agua!")
elif not(tenho_sede) and tenho_fome:
    print("Vou fazer um lanche!")
else:
    print("Ficarei lendo livro!")