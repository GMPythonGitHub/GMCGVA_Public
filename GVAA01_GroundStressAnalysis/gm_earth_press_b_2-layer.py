# gm_earth_press_b_2-layerr.py:: coded by Kinya MIURA 250428
# --------------------------------------------------------
print('*** ground stress analysis ***')
print('   *** earth pressire ***')
# --------------------------------------------------------
print('### --- section_module: importing items from modules --- ###')
from numpy import array

# =========================================================
print('### --- section_s: setting --- ###')
## --- section_sa: surcharge and gravity --- ##
qqq, gra = 10. * 1000, 9.80665
print(
    f'surcharge (kN/m^3); {qqq/1000 = :.2f}, '
    f'gravity acceleration (m/s^2); {gra = :.3f}' )

## --- section_sb: ground condition --- ##
print(':: layer 0')
zzu0, thk0 = 0., 3.
print(
    f'upper level (m); {zzu0 = :.2f}, '
    f'thickness (m); {thk0 = :.2f}' )
print(':: layer 1')
zzu1, thk1 = zzu0 + thk0, 7.
print(
    f'upper level (m); {zzu1 = :.2f}, '
    f'thickness (m); {thk1 = :.2f}' )

## --- section_sc: soil properties --- ##
print(':: layer 0')
rhot0, kkk0 = 1600., 0.3
print(
    f'wet density of soil (kg/m^3); {rhot0 = :.3f}, '
    f'earth pressure coeff. (); {kkk0 = }' )
print(':: layer 1')
rhot1, kkk1 = 1900., 0.5
print(
    f'wet density of soil (kg/m^3); {rhot1 = :.3f}, '
    f'earth pressure coeff. (); {kkk1 = }' )

# =========================================================
print('### --- section_c: calculating --- ###')
zz0 = array([zzu0, zzu0+thk0])
sigv0 = qqq + (zz0 - zzu0) * rhot0 * gra
sigh0 = sigv0 * kkk0

zz1 = array([zzu1, zzu1+thk1])
sigv1 = sigv0[-1] + (zz1 - zzu1) * rhot1 * gra
sigh1 = sigv1 * kkk1

zz = array(list(zz0) + list(zz1))
sigv = array(list(sigv0) + list(sigv1))
sigh = array(list(sigh0) + list(sigh1))

# =========================================================
print('### --- section_d: drawing graph --- ###')
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(4,6))
ax.invert_yaxis()
ax.vlines(0, min(zz), max(zz), color='k', linewidth=.5)
ax.hlines(0, 0., max(sigv)/1000, color='k', linewidth=.5)
ax.set_xlabel('earth pressure, $\sigma_{v}$, $\sigma_{v}$ (kN/m$^2$)')
ax.set_ylabel('depth, $z$ (m)')

ax.plot(sigv/1000, zz, label='$\sigma_{v}$')
ax.plot(sigh/1000, zz, label='$\sigma_{h}$')

ax.legend()

print(': showing figure : ')
plt.show()
print(': saving figure : ')
fig.savefig('gm_earth_press_b_2-layer.png')

