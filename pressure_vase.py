import numpy as np
import matplotlib.pyplot as plt

# ------- FASE 2 ------- FASE 2 ------- FASE 2 ------- FASE 2

a = 25                                                                          # [mm] inner radius grain
b = 50                                                                          # [mm] outer radius grain
h = 2                                                                           # [mm] case thickness
c = b + h                                                                       # [mm] outer radius case
vi = 0.5                                                                        # propellant poisson
vo = 0.3                                                                        # case poisson
Ei = 60                                                                         # [MPa] propellant modulus of elasticity
Eo = 210000                                                                     # [MPa] case modulus of elasticity
alphai = 0.000093                                                               # propellant coef. of thermal expansion
alphao = 0.000011                                                               # case coef. of thermal expansion
T1 = -40 - 65                                                                   # [K] ou [C] temp. variation for phase 2

print('------- FASE 2 -------')
print('')
print('Variação de temperatura = ', T1, ' K')
print('')

ai = alphai * T1 * a + a
bo = alphao * T1 * b + b
bi = alphai * T1 * b + b
co = alphao * T1 * c + c
print('ai = ', ai, 'mm')
print('bo = ', bo, 'mm')
print('bi = ', bi, 'mm')
print('co = ', co, 'mm')
print('')

delta = bi - bo                                                                 # [mm] cálculo da interferência
print('delta = ', delta, 'mm')
print('')

R = b
denomin1 = R*(((R**2 + co**2)/(co**2 - R**2)) + vo)/Eo
denomin2 = R*(((R**2 + ai**2)/(R**2 - ai**2)) - vi)/Ei

p = delta / (denomin1 + denomin2)                                               # [MPa] pressão de interface da fase 1
print('Pressão fase 2 = ', p, ' MPa')
print('')

ri = np.linspace(a, b, 90)
ro = np.linspace(b, c, 90)

pi_p = 0                                                                        # pressão interna do propelente
pe_p = p                                                                        # pressão externa do propelente
ri_p = a                                                                        # raio interno do propelente
re_p = b                                                                        # raio externo do propelente
A_p = (pi_p * ri_p**2 - pe_p * re_p**2) / (re_p**2 - ri_p**2)                   # [MPa] A do propelente
B_p = ((pi_p - pe_p) * (re_p**2) * (ri_p**2)) / ((re_p**2) - (ri_p**2))         # [MPa] B do propelente
print('A_p = ', A_p, 'MPa')
print('B_p = ', B_p, 'Pa')      # não sei o porquê de essa pressão estar aparecendo em Pa ao inves de MPa

pi_c = p                                                                        # pressão interna da câmara
pe_c = 0                                                                        # pressão externa da câmara
ri_c = b                                                                        # raio interno da câmara
re_c = c                                                                        # raio externo da câmara
A_c = (pi_c * ri_c**2 - pe_c * re_c**2) / (re_c**2 - ri_c**2)                   # [MPa] A da câmara
B_c = ((pi_c - pe_c) * (re_c**2) * (ri_c**2)) / ((re_c**2) - (ri_c**2))         # [MPa] B da câmara
print('A_c = ', A_c, 'MPa')
print('B_c = ', B_c, 'Pa')      # não sei o porquê de essa pressão estar aparecendo em Pa ao inves de MPa
print('')

aai = (1-2*vi)*A_p/Ei                                                           # parâmetro "a" do propelente
bbi = (1+vi)*B_p/Ei                                                             # parâmetro "b" do propelente
aao = (1-2*vo)*A_c/Eo                                                           # parâmetro "a" da câmara
bbo = (1+vo)*B_c/Eo                                                             # parâmetro "b" da câmara
print('aai = ', aai)
print('bbi = ', bbi)
print('aao = ', aao)
print('bbo = ', bbo)
print('')



def ur_bi(ri):                                                                  # [mm] deslocamento radial no propelente
    return aai*ri + bbi/ri


def ur_bo(ro):                                                                  # [mm] deslocamento radial na câmara
    return aao*ro + bbo/ro


# ------- DEFORMAÇÕES fase 2 ------- DEFORMAÇÕES fase 2 ------- DEFORMAÇÕES fase 2 ------- DEFORMAÇÕES fase 2


def e_ti(ri):                                                                  # deformação tangencial no propelente
    return aai + bbi/ri**2


def e_to(ro):                                                                  # deformação tangencial na câmara
    return aao + bbo/ro**2


def e_ri(ri):                                                                  # deformação radial no propelente
    return aai - bbi/ri**2


def e_ro(ro):                                                                  # deformação radial na câmara
    return aao - bbo/ro**2

plt.figure()
plt.subplot(1,2,1)
plt.title('Def. tangencial propelente fase 2')
plt.ylabel('def_ti')
plt.xlabel('Raio (mm)')
plt.plot(ri, e_ti(ri), 'black', label='Deformação tangencial do propelente')

plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.title('Def. tangencial câmara fase 2')
plt.ylabel('def_to')
plt.xlabel('Raio (mm)')
plt.plot(ro, e_to(ro), 'purple', label='Deformação tangencial da câmara')

plt.legend()
plt.grid()
# plt.show()

plt.figure()
plt.subplot(1,2,1)
plt.title('Def. radial propelente fase 2')
plt.ylabel('def_ri')
plt.xlabel('Raio (mm)')
plt.plot(ri, e_ri(ri), 'blue',  label='Deformação radial do propelente')

plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.title('Def. radial câmara fase 2')
plt.ylabel('def_ro')
plt.xlabel('Raio (mm)')
plt.plot(ro, e_ro(ro), 'orange', label='Deformação radial da câmara')

plt.legend()
plt.grid()
# plt.show()

# ------- TENSÕES fase 2 ------- TENSÕES fase 2 ------- TENSÕES fase 2 ------- TENSÕES fase 2


def sigma_ti(ri):                                                                  # [MPa] tensão tangenc. no propelente
    return A_p + (B_p / ri**2)


def sigma_to(ro):                                                                  # [MPa] tensão tangenc. na câmara
    return A_c + (B_c / ro**2)


def sigma_ri(ri):                                                                  # [MPa] tensão radial no propelente
    return A_p - (B_p / ri**2)


def sigma_ro(ro):                                                                  # [MPa] tensão radial na câmara
    return A_c - (B_c / ro**2)

plt.figure()
plt.subplot(1, 2, 1)
plt.title('Tensão tangencial propelente fase 2')
plt.ylabel('sigma_ti [MPa]')
plt.xlabel('Raio (mm)')
plt.plot(ri, sigma_ti(ri), 'green', label='Tensão tangencial do propelente')

plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.title('Tensão tangencial câmara fase 2')
plt.ylabel('sigma_to [MPa]')
plt.xlabel('Raio (mm)')
plt.plot(ro, sigma_to(ro), 'yellow', label='Tensão tangencial da câmara')

plt.legend()
plt.grid()
# plt.show()

plt.figure()
plt.subplot(1, 2, 1)
plt.title('Tensão radial propelente fase 2')
plt.ylabel('sigma_ri [MPa]')
plt.xlabel('Raio (mm)')
plt.plot(ri, sigma_ri(ri), 'brown', label='Tensão radial do propelente')

plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.title('Tensão radial câmara fase 2')
plt.ylabel('sigma_ro [MPa]')
plt.xlabel('Raio (mm)')
plt.plot(ro, sigma_ro(ro), 'pink', label='Tensão radial da câmara')

plt.legend()
plt.grid()
# plt.show()

# ------- FASE 3 ------- FASE 3 ------- FASE 3 ------- FASE 3

print('------- FASE 3 -------')
print('')

T2 = 20 - 65                                                                    # [K] ou [C] variação temperatura fase 3
print('Variação de temperatura = ', T2, ' K')
print('')

ai = alphai * T2 * a + a
bo = alphao * T2 * b + b
bi = alphai * T2 * b + b
co = alphao * T2 * c + c

delta3 = bi - bo                                                                # [mm] cálculo da interferência
print('delta = ', delta3, ' mm')
print('')

R = b

denomin1 = R*(((R**2 + co**2)/(co**2 - R**2)) + vo)/Eo
denomin2_3 = R*(((R**2 + ai**2)/(R**2 - ai**2)) - vi)/Ei

p = delta3 / (denomin1 + denomin2_3)                                              # [MPa] pressão de interface da fase 1
print('Pressão fase 3 = ', p, ' MPa')
print('')

pi_p = 20                                                                       # [MPa] pressão interna do propelente
pe_p = p                                                                        # [MPa] pressão externa do propelente
ri_p = a                                                                        # [mm] raio interno do propelente
re_p = b                                                                        # [mm] raio externo do propelente
A_p = (pi_p * ri_p**2 - pe_p * re_p**2) / (re_p**2 - ri_p**2)                   # [MPa] A do propelente
B_p = ((pi_p - pe_p) * (re_p**2) * (ri_p**2)) / ((re_p**2) - (ri_p**2))         # [MPa] B do propelente
print('A_p = ', A_p, 'MPa')
print('B_p = ', B_p, 'Pa')      # não sei o porquê de essa pressão estar aparacendo em Pa ao inves de MPa

pi_c = p                                                                        # [MPa] pressão interna da câmara
pe_c = 0                                                                        # [MPa] pressão externa da câmara
ri_c = b                                                                        # [mm] raio interno da câmara
re_c = c                                                                        # [mm] raio externo da câmara
A_c = (pi_c * ri_c**2 - pe_c * re_c**2) / (re_c**2 - ri_c**2)                   # [MPa] A da câmara
B_c = ((pi_c - pe_c) * (re_c**2) * (ri_c**2)) / ((re_c**2) - (ri_c**2))         # [MPa] B da câmara
print('A_c = ', A_c, 'MPa')
print('B_c = ', B_c, 'Pa')      # não sei o porquê de essa pressão estar aparecendo em Pa ao inves de MPa
print('')

aai3 = (1-2*vi)*A_p/Ei
bbi3 = (1+vi)*B_p/Ei
aao3 = (1-2*vo)*A_c/Eo
bbo3 = (1+vo)*B_c/Eo


def ur_bi3(ri):                                                                 # [m] deslocamento radial no propelente
    return aai3*ri + bbi3/ri


def ur_bo3(ro):                                                                 # [m] deslocamento radial na câmara
    return aao3*ro + bbo3/ro


# ------- DEFORMAÇÕES fase 3 ------- DEFORMAÇÕES fase 3 ------- DEFORMAÇÕES fase 3 ------- DEFORMAÇÕES fase 3


def e_ti3(ri):                                                                  # deformação tangencial no propelente
    return aai3 + bbi3/ri**2


def e_to3(ro):                                                                  # deformação tangencial na câmara
    return aao3 + bbo3/ro**2


def e_ri3(ri):                                                                  # deformação radial no propelente
    return aai3 - bbi3/ri**2


def e_ro3(ro):                                                                  # deformação radial na câmara
    return aao3 - bbo3/ro**2

plt.figure()
plt.subplot(1,2,1)
plt.title('Def. tangencial propelente fase 3')
plt.ylabel('def_ti')
plt.xlabel('Raio (mm)')
plt.plot(ri, e_ti3(ri), 'black', label='Deformação tangencial do propelente')

plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.title('Def. tangencial câmara fase 3')
plt.ylabel('def_to')
plt.xlabel('Raio (mm)')
plt.plot(ro, e_to3(ro), 'purple', label='Deformação tangencial da câmara')

plt.legend()
plt.grid()
#plt.show()

plt.figure()
plt.subplot(1,2,1)
plt.title('Def. radial propelente fase 3')
plt.ylabel('def_ri')
plt.xlabel('Raio (mm)')
plt.plot(ri, e_ri3(ri), 'blue',  label='Deformação radial do propelente')

plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.title('Def. radial câmara fase 3')
plt.ylabel('def_ro')
plt.xlabel('Raio (mm)')
plt.plot(ro, e_ro3(ro), 'orange', label='Deformação radial da câmara')

plt.legend()
plt.grid()
# plt.show()

# ------- TENSÕES fase 3 ------- TENSÕES fase 3 ------- TENSÕES fase 3 ------- TENSÕES fase 3


def sigma_ti3(ri):                                                                  # [Pa] tensão tangenc. no propelente
    return A_p + (B_p / ri**2)


def sigma_to3(ro):                                                                  # [Pa] tensão tangenc. na câmara
    return A_c + (B_c / ro**2)


def sigma_ri3(ri):                                                                  # [Pa] tensão radial no propelente
    return A_p - (B_p / ri**2)


def sigma_ro3(ro):                                                                  # [Pa] tensão radial na câmara
    return A_c - (B_c / ro**2)

plt.figure()
plt.subplot(1, 2, 1)
plt.title('Tensão tangencial propelente fase 3')
plt.ylabel('sigma_ti [MPa]')
plt.xlabel('Raio (mm)')
plt.plot(ri, sigma_ti3(ri), 'green', label='Tensão tangencial do propelente')

plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.title('Tensão tangencial câmara fase 3')
plt.ylabel('sigma_to [MPa]')
plt.xlabel('Raio (mm)')
plt.plot(ro, sigma_to3(ro), 'yellow', label='Tensão tangencial da câmara')

plt.legend()
plt.grid()
# plt.show()

plt.figure()
plt.subplot(1, 2, 1)
plt.title('Tensão radial propelente fase 3')
plt.ylabel('sigma_ri [MPa]')
plt.xlabel('Raio (mm)')
plt.plot(ri, sigma_ri3(ri), 'brown', label='Tensão radial do propelente')

plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.title('Tensão radial câmara fase 3')
plt.ylabel('sigma_ro [MPa]')
plt.xlabel('Raio (mm)')
plt.plot(ro, sigma_ro3(ro), 'black', label='Tensão radial da câmara')

plt.legend()
plt.grid()
plt.show()

