# gm_water_press.py:: coded by Kinya MIURA 240428
# --------------------------------------------------------
print('*** ground stress analysis ***')
print('   *** water pressure ***')
# --------------------------------------------------------
print('### --- section_module: importing items from modules --- ###')
from numpy import array

# =========================================================
print('### --- section_s: setting --- ###')
## --- section_sa: water condition --- ##
zzo, dep = 0, 10.
print(
    f'surface level (m); {zzo = :.2f}, '
    f'depth (m); {dep = :.2f}' )

## --- section_sb: water properties --- ##
rhow, gra = 1000., 9.80665
print(
    f'density of water (kg/m^3); {rhow = :.3f}, '
    f'gravity acc. (m/s^2); {gra = :.3f}' )

# =========================================================
print('### --- section_c: calculating --- ###')
zz = array([zzo, zzo+dep])  # depth (m)
ppp = (zz - zzo) * rhow * gra  # water pressure, p (N/m^2)

# =========================================================
print('### --- section_d: drawing --- ###')
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(4,6))
ax.invert_yaxis()
ax.vlines(0, min(zz), max(zz), color='k', linewidth=.5)
ax.hlines(0, 0., max(ppp)/1000, color='k', linewidth=.5)
ax.set_xlabel('water pressure, $p$ (kN/m$^2$)')
ax.set_ylabel('depth, $z$ (m)')

ax.plot(ppp/1000, zz)

print(': showing figure : ')
plt.show()
print(': saving figure : ')
fig.savefig('gm_water_press.png')

