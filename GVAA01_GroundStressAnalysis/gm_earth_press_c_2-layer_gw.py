# gm_earth_press_c_2-layerr.py:: coded by Kinya MIURA 250428
# --------------------------------------------------------
print('*** ground stress analysis ***')
print('   *** earth pressire with ground water ***')
# --------------------------------------------------------
print('### --- section_module: importing items from modules --- ###')
from numpy import array

# =========================================================
print('### --- section_s: setting --- ###')
## --- section_sa: surcharge and gravity --- ##
qqq, rhow, gra = 10. * 1000, 1000., 9.80665
print(
    f'surcharge (kN/m^2); {qqq/1000 = :.2f}, '
    f'density of water (kg/m^3); {rhow = :.2f}, '
    f'gravity acceleration (m/s^2); {gra = :.3f}' )

## --- section_ab: ground condition --- ##
print(':: layer 0')
zzu0, thk0 = 0., 2.
print(
    f'upper level (m); {zzu0 = :.2f}, '
    f'thickness (m); {thk0 = :.2f}' )
print(':: layer 1')
zzu1, thk1 = zzu0 + thk0, 3.
print(
    f'upper level (m); {zzu1 = :.2f}, '
    f'thickness (m); {thk1 = :.2f}' )
print(':: layer 2')
zzu2, thk2 = zzu1 + thk1, 5.
print(
    f'upper level (m); {zzu2 = :.2f}, '
    f'thickness (m); {thk2 = :.2f}' )

## --- section_ac: soil properties --- ##
print(':: layer 0')
wcnd0 = 't'
rhot0, kkk0 = 1600., 0.4
print(
    f'wet condition [t; wet, s; submerged, w; water]; {wcnd0 = } \n'
    f'wet density of soil (kg/m^3); {rhot0 = }, '
    f'earth pressure coeff. (); {kkk0 = }' )
print(':: layer 1')
wcnd1 = 's'
rhot1, kkk1 = 1800., 0.4
print(
    f'wet condition [t; wet, s; submerged, w; water]; {wcnd1 = } \n'
    f'wet density of soil (kg/m^3); {rhot1 = :.3f}, '
    f'earth pressure coeff. (); {kkk1 = }' )
print(':: layer 2')
wcnd2 = 's'
rhot2, kkk2 = 2100., 0.5
print(
    f'wet condition [t; wet, s; submerged, w; water]; {wcnd2 = } \n'
    f'wet density of soil (kg/m^3); {rhot2 = }, '
    f'earth pressure coeff. (); {kkk2 = }' )

# =========================================================
print('### --- section_b: calculating --- ###')
zz0 = array([zzu0, zzu0+thk0])
if wcnd0 == 't':
    ppp0 = zz0 * 0.
    sigv0 = qqq + (zz0 - zzu0) * rhot0 * gra
elif wcnd0 == 's':
    ppp0 = (zz0 - zzu0) * rhow * gra
    sigv0 = qqq + (zz0 - zzu0) * (rhot0-rhow) * gra
elif wcnd0 == 'w':
    ppp0 = (zz0 - zzu0) * rhow * gra
    sigv0 = zz0 * 0.
sigh0 = sigv0 * kkk0

zz1 = array([zzu1, zzu1+thk1])
if wcnd1 == 't':
    ppp1 = zz1 * 0.
    sigv1 = sigv0[-1] + (zz1 - zzu1) * rhot1 * gra
elif wcnd1 == 's':
    ppp1 = ppp0[-1] + (zz1 - zzu1) * rhow * gra
    sigv1 = sigv0[-1] + (zz1 - zzu1) * (rhot1-rhow) * gra
elif wcnd1 == 'w':
    ppp1 = ppp0[-1] + (zz1 - zzu1) * rhow * gra
    sigv1 = zz1 * 0.
sigh1 = sigv1 * kkk1

zz2 = array([zzu2, zzu2+thk2])
if wcnd2 == 't':
    ppp2 = zz2 * 0.
    sigv2 = sigv1[-1] + (zz2 - zzu2) * rhot2 * gra
elif wcnd2 == 's':
    ppp2 = ppp1[-1] + (zz2 - zzu2) * rhow * gra
    sigv2 = sigv1[-1] + (zz2 - zzu2) * (rhot2-rhow) * gra
elif wcnd2 == 'w':
    ppp2 = ppp1[-1] + (zz2 - zzu2) * rhow * gra
    sigv1 = zz2 * 0.
sigh2 = sigv2 * kkk2

zz = array(list(zz0) + list(zz1) + list(zz2))
sigv = array(list(sigv0) + list(sigv1) + list(sigv2))
sigh = array(list(sigh0) + list(sigh1) + list(sigh2))
ppp = array(list(ppp0) + list(ppp1) + list(ppp2))

# =========================================================
print('### --- section_c: drawing graph --- ###')
from matplotlib import (
    pyplot as plt, animation as ani)

fig, ax = plt.subplots(figsize=(4,6))
ax.invert_yaxis()
ax.vlines(0, min(zz), max(zz), color='k', linewidth=.5)
ax.hlines(0, 0., max(sigv+ppp)/1000, color='k', linewidth=.5)
ax.set_xlabel('pressure, $\sigma_{v}$, $\sigma_{v}$, $p$ (kN/m$^2$)')
ax.set_ylabel('depth, $z$ (m)')

ax.plot(sigv/1000, zz, label='$\sigma_{v}\'$', color='C1')
# ax.plot(sigh/1000, zz, label='$\sigma_{h}\'$', color='C1')
ax.plot(ppp/1000, zz, label='$p$', color='C0')
ax.plot((sigv+ppp)/1000, zz, label='$\sigma_{v}$', color='C2', linestyle='--')
# ax.plot((sigh+ppp)/1000, zz, label='$\sigma_{h}$', color='C1', linestyle='--')

ax.legend()

print(': showing figure : ')
plt.show()
print(': saving figure : ')
fig.savefig('gm_earth_press_c_2-layer_gw.png')

