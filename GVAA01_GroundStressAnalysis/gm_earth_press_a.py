# gm_earth_press_a.py:: coded by Kinya MIURA 250428
# --------------------------------------------------------
print('*** ground stress analysis ***')
print('   *** earth pressure ***')
# --------------------------------------------------------
print('### --- section_module: importing items from modules --- ###')
from numpy import(array)

# =========================================================
print('### --- section_s: setting --- ###')
## --- section_aa: setting ground condition --- ##
zzo, thk, qqq = 0., 10., 10. * 1000
print(
    f'surface level (m); {zzo = :.2f}, '
    f'thickness (m); {thk = :.2f}, '
    f'surcharge (kN/m^2); {qqq/1000 = :.2f}' )

## --- section_sb: setting soil properties --- ##
rhot, kkk, gra = 1800., 0.5, 9.80665
print(
    f'wet density of soil (kg/m^3); {rhot = :.3f}, '
    f'earth pressure coeff.; {kkk = :.3f}, '
    f'gravity acc. (m/s^2); {gra = :.3f}' )

# =========================================================
print('### --- section_c: calculating --- ###')
zz = array([zzo, zzo+thk])  # depth (m)
sigv = qqq + (zz - zzo) * rhot * gra  # vertical stress (N/m^2)
sigh = sigv * kkk  # horizontal stress (N/m^2)

# =========================================================
print('### --- section_d: drawing --- ###')
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(4,6))
ax.invert_yaxis()
ax.vlines(0, min(zz), max(zz), color='k', linewidth=.5)
ax.hlines(0, 0., max(sigv)/1000, color='k', linewidth=.5)
ax.set_xlabel('earth pressure, $\sigma_{v}$, $\sigma_{h}$ (kN/m$^2$)')
ax.set_ylabel('depth, $z$ (m)')

ax.plot(sigv/1000, zz, label='$\sigma_{v}$')
ax.plot(sigh/1000, zz, label='$\sigma_{h}$')

ax.legend()

print(': showing figure : ')
plt.show()
print(': saving figure : ')
fig.savefig('gm_earth_press_a.png')

