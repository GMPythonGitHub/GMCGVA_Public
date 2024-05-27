# gm_class_eprs_b_ground.py: coded by Kinya MIURA 240527
# ---------------------------------------------------------
print("*** (GMEprsGround) class for segment ***")
print("   *** class GMEprsLayer is embedded as list layrs ***")
# ---------------------------------------------------------
print("### --- section__: (GMEprsGround) importing items from module --- ###")
from numpy import (ndarray, array)
from copy import deepcopy
from typing import Self
from gm_class_eprs_a_layer import (GMEprsLayer)

# =========================================================
print("### --- section_class: (GMEprsGround) describing class --- ###")
class GMEprsGround():
    ## --- section_ca: (GMEprsGround) initializing class instance --- ##
    def __init__(self,
            layrs: list,
            qqq: float = 0, cnv: bool = True):
        self._layrs = []  # list of ground layers [GMEprsLayer]
        self.set_eprs_ground(layrs=layrs, qqq=qqq, cnv=cnv)
    ## --- section_cb: (GMEprsGround) setting and getting functions --- ##
    ## setting functions
    def set_eprs_ground(self,
            layrs: list, qqq: float = None, cnv: bool = True ):
        self._layrs = layrs
        if qqq is not None: self.__qqq = qqq * 1e3 if cnv else qqq
    ## getting functions
    def numlayr(self) -> int:
        return len(self._layrs)
    def qqq(self, cnv: bool = True): return self.__qqq/1e3 if cnv else self.__qqq
    def copy(self) -> Self:
        return deepcopy(self)
    ## --- section_cc: (GMEprsGround) string function for print() --- ##
    def __str__(self) -> str:
        st  = (
            f'  numlayr = {self.numlayr():d} : qqq = {self.qqq():g} \n' )
        st += f'\nlayrs[{len(self._layrs)}]: GMEprsLayer:'
        for i, layr in enumerate(self._layrs):
            st += '\n' + layr.classprop(f'**[{i:02d}]')
        return st
    def classprop(self, idx: str = '') -> str:
        return idx + ':: GMEprsGround ::  ' + self.__str__()
    ## --- section_cd: (GMEprsGround) calculating properties --- ##
    def build_grnd(self) -> None:
        self._layrs[0].set_eprs_layer(
            sigvu=self.qqq(), pppu=0 )
        for i in range(1,len(self._layrs)):
            self._layrs[i].set_eprs_layer(
                zzu=self._layrs[i-1].zzl(),
                sigvu=self._layrs[i-1].sigvl(),
                pppu=self._layrs[i-1].pppl() )
    def proc_data(self) -> tuple:
        zz, sigv, sigh, ppp = [], [], [], []
        for layr in self._layrs:
            zz.extend([layr.zzu(), layr.zzl()])
            sigv.extend([layr.sigvu(), layr.sigvl()])
            sigh.extend([layr.sighu(), layr.sighl()])
            ppp.extend([layr.pppu(), layr.pppl()])
        return zz, sigv, sigh, ppp

# =========================================================
if __name__ == '__main__':
    print("### --- section_m: main process --- ###")
    print()
    ## --- section_ma: (GMEprsGround) creating class instance --- ##
    layrs = list(range(3))  # list of layers [GMEprsLayer]
    layrs[0] = GMEprsLayer(zzu=0, thk=2, wcnd='t', rhot=1600, kkk=.4, sigvu=0, pppu=0)
    layrs[1] = GMEprsLayer(thk=3, wcnd='s', rhot=1800, kkk=.4)
    layrs[2] = GMEprsLayer(thk=5, wcnd='s', rhot=2100, kkk=.5)
    eprsgrnd = GMEprsGround(layrs=layrs, qqq=10)
    eprsgrnd.build_grnd()
    print(eprsgrnd.classprop('eprsgrnd -> '))
    print()
    ## --- section_mb: processing data --- ##
    zz, sigv, sigh, ppp = eprsgrnd.proc_data()
    zz, sigv, sigh, ppp = array(zz), array(sigv), array(sigh), array(ppp)
    print()
    ## --- section_mc: drawing graph --- ##
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.invert_yaxis()
    ax.vlines(0, min(zz), max(zz), color='k', linewidth=.5)
    ax.hlines(0, 0., max(sigv + ppp), color='k', linewidth=.5)
    ax.set_xlabel('pressure, $\sigma_{v}$, $\sigma_{v}$, $p$ (kN/m$^2$)')
    ax.set_ylabel('depth, $z$ (m)')

    ax.plot(sigv, zz, label='$\sigma_{v}\'$', color='C1')
    # ax.plot(sigh, zz, label='$\sigma_{h}\'$', color='C1')
    ax.plot(ppp, zz, label='$p$', color='C0')
    ax.plot(sigv + ppp, zz, label='$\sigma_{v}$', color='C2', linestyle='--')
    # ax.plot(sigh+ppp, zz, label='$\sigma_{h}$', color='C1', linestyle='--')
    ax.legend()
    print(': showing figure : ')
    plt.show()
    print(': saving figure : ')
    fig.savefig('gm_class_eprs_ground.png')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    '''

