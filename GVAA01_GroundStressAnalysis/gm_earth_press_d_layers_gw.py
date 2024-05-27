# gm_earth_press_d_layers_gw.py:: coded by Kinya MIURA 250428
# --------------------------------------------------------
print('*** ground stress analysis ***')
print('   *** earth pressure in layers with ground water ***')
# --------------------------------------------------------
print('### --- section_module: importing items from modules --- ###')
from numpy import array

# =========================================================
print('### --- section_s: setting --- ###')
## --- section_aa: surcharge and gravity --- ##
qqq, rhow, gra = 10. * 1000, 1000., 9.80665
print(
    f'surcharge (kN/m^2); {qqq/1000 = :.2f}, '
    f'density of water (kg/m^3); {rhow = :.2f}, '
    f'gravity acceleration (m/s^2); {gra = :.3f}' )

## --- section_sb: ground condition --- ##
numlyrs = 3
print(f'number of layers; {numlyrs = :d}')
zzu = [0., None, None]
thk = [2., 3., 5.]
for lyri in range(1, numlyrs):
    zzu[lyri] = zzu[lyri-1] + thk[lyri-1]
print(
    f'upper level (m); {zzu} \n'
    f'thickness (m); {thk}' )

## --- section_sc: soil properties --- ##
wcnd = ['t', 's', 's']  # wet condition
rhot = [1600., 1800., 2100.]
kkk = [0.4, 0.4, 0.5]
print(
    f'wet condition [t; wet, s; submerged, w; water]; {wcnd = } \n'
    f'wet density of soil (kg/m^3); {rhot = }, \n'
    f'earth pressure coeff. (); {kkk = }' )

# =========================================================
print('### --- section_c: calculating --- ###')
zz, sigv, sigh, ppp = [], [], [], []

for lyri, (zzui, thki, wcndi, rhoti, kkki) in enumerate(zip(zzu, thk, wcnd, rhot, kkk)):
    zzi = array([zzui, zzui+thki])
    if lyri == 0:
        if wcndi == 't':
            pppi = zzi * 0.
            sigvi = qqq + (zzi - zzui) * rhoti * gra
        elif wcndi == 's':
            pppi = (zzi - zzui) * rhow * gra
            sigvi = qqq + (zzi - zzui) * (rhoti - rhow) * gra
        elif wcndi == 'w':
            pppi= (zzi - zzui) * rhow * gra
            sigvi = zzi * 0.
        sighi = sigvi * kkki
    else:
        if wcndi == 't':
            pppi = zzi * 0.
            sigvi = sigv[-1] + (zzi - zzui) * rhoti * gra
        elif wcndi == 's':
            pppi = ppp[-1] + (zzi - zzui) * rhow * gra
            sigvi = sigv[-1] + (zzi - zzui) * (rhoti - rhow) * gra
        elif wcndi == 'w':
            pppi = ppp[-1] + (zzi - zzui) * rhow * gra
            sigvi = zzi * 0.
        sighi = sigvi * kkki
    zz.extend(zzi)
    sigv.extend(sigvi)
    sigh.extend(sighi)
    ppp.extend(pppi)
zz, sigv, sigh, ppp = array(zz), array(sigv), array(sigh), array(ppp)
print(f'{zz = } \n{sigv = } \n{sigh = } \n{ppp = }')

# =========================================================
print('### --- section_d: drawing graph --- ###')
from matplotlib import pyplot as plt

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
fig.savefig('gm_earth_press_d_layers_gw.png')
