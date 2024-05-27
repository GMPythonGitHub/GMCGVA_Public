## gm_class_eprs_a_layer.py: coded by Kinya MIURA 240527
# ---------------------------------------------------------
print("*** (GMEprsLayer) class for earth pressure in layer ***")
# ---------------------------------------------------------
print("### --- section_module: (GMEprsLayer) importing items from module --- ###")
from numpy import (
    deg2rad as d2r, rad2deg as r2d, cos, sin, tan, arctan2,
    ndarray, array, inner, outer, cross )
from copy import deepcopy
from typing import Self

# =========================================================
print("### --- section_class: (GMEprsLayer) describing class --- ###")
class GMEprsLayer():
    ## --- section_ca: (GMEprsLayer) initializing class instance --- ##
    def __init__(self,
            zzu: float = 0, thk: float = 1,
            wcnd: str = 'wet', rhot: float = 1800, kkk: float = .5,
            sigvu: float = 0, pppu: float = 0):
        self.__zzu = None  # upper surface level of layer (m): float
        self.__thk = None  # thickness of layer (m): float
        self.__wcnd = None  # wet condition: str [t; wet, s; submerged, w; water]
        self.__rhot = None  # wet density of soil (kg/m^3): float
        self.__kkk = None  # earth pressure coefficient (): float
        self.__sigvu = None  # vertical stress on upper surface (kN/m^2): float
        self.__pppu = None  # pore water pressure on upper surface (kN/m^2): float
        self.__rhow = 1000  # density of water (kg/m^3): float
        self.__gra = 9.80665  # aravity acceleration (m/s^2): float
        self.set_eprs_layer(
            zzu=zzu, thk=thk, wcnd=wcnd, rhot=rhot, kkk=kkk,
            sigvu=sigvu, pppu=pppu )
    ## --- section_cb: (GMEprsLayer) setting and getting functions --- ##
    ## setting functions
    def set_eprs_layer(self,
            zzu: float = None, thk: float = None,
            wcnd: str = None, rhot: float = None, kkk: float = None,
            sigvu: float = None, pppu: float = None) -> None:
        if zzu is not None: self.__zzu = zzu
        if thk is not None: self.__thk = thk
        if wcnd is not None:
            if wcnd in ('wet', 't'): self.__wcnd = 'wet'
            elif wcnd in ('submerged', 's'): self.__wcnd = 'submerged'
            elif wcnd in ('water', 'w'): self.__wcnd = 'water'
        if rhot is not None: self.__rhot = rhot
        if kkk is not None: self.__kkk = kkk
        if sigvu is not None: self.__sigvu = sigvu * 1e3
        if pppu is not None: self.__pppu = pppu * 1e3
    ## getting functions
    def zzu(self) -> float: return self.__zzu
    def thk(self) -> float: return self.__thk
    def zzl(self) -> float: return self.__zzu + self.__thk
    def wcnd(self) -> str: return self.__wcnd
    def rhot(self) -> float: return self.__rhot
    def kkk(self) -> float: return self.__kkk
    def sigvu(self, cnv: bool = True) -> float:
        return self.__sigvu/1e3 if cnv else self.__sigvu
    def sigv(self, zz: float, cnv: bool = True) -> float:
        sigv = self.__sigvu
        if self.__wcnd == 'wet': sigv += self.__rhot * self.__gra * zz
        elif self.__wcnd == 'submerged': sigv += (self.__rhot-self.__rhow) * self.__gra * zz
        elif self.__wcnd == 'water': pass
        return sigv/1e3 if cnv else sigv
    def sigvl(self, cnv: bool = True) -> float:
        return self.sigv(self.__thk, cnv=cnv)
    def sighu(self, cnv: bool = True) -> float:
        return self.sigvu(cnv=cnv) * self.__kkk
    def sigh(self, zz: float, cnv: bool = True) -> float:
        return self.sigv(zz, cnv=cnv) * self.__kkk
    def sighl(self, cnv: bool = True) -> float:
        return self.sigvl(cnv=cnv) * self.__kkk
    def pppu(self, cnv: bool = True) -> float:
        return self.__pppu/1e3 if cnv else self.__pppu
    def ppp(self, zz: float, cnv: bool = True) -> float:
        ppp = self.__pppu
        if self.__wcnd == 'wet': pass
        elif self.__wcnd == 'submerged': ppp += self.__rhow * self.__gra * zz
        elif self.__wcnd == 'water': ppp += self.__rhow * self.__gra * zz
        return ppp/1e3 if cnv else ppp
    def pppl(self, cnv: bool = True) -> float:
        return self.ppp(self.__thk, cnv=cnv)
    def rhow(self) -> float: return self.__rhow
    def gra(self) -> float: return self.__gra
    def copy(self) -> Self:
        return deepcopy(self)
    ## --- section_cc: (GMEprsLayer) string function for print() --- ##
    def __str__(self) -> str:
        return (
            f'  zzu = {self.zzu():g} : thk = {self.thk():g} : zzl = {self.zzl():g} : '
            f'  wcnd = {self.wcnd():s} : rhot = {self.rhot():g} : kkk = {self.kkk():g} : '
            f'  rhow = {self.rhow():g} : gra = {self.gra():g} \n'
            f'  sigvu = {self.sigvu():g} : sigvl = {self.sigvl():g} : '
            f'  sighu = {self.sighu():g} : sighl = {self.sighl():g} : '
            f'  pppu = {self.pppu():g} : pppl = {self.pppl():g}' )
    def classprop(self, idx: str = '') -> str:
        return idx + ':: GMEprsLayer ::\n' + self.__str__()

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMEprsLayer) main process --- ###")
    print()
    ## --- section_ma: (GMEprsLayer) creating class instances --- ##
    eprslyra = GMEprsLayer(zzu=0, thk=2, wcnd='t', rhot=1800, kkk=.5);
    print(eprslyra.classprop('eprslyra -> '))
    eprslyrb = GMEprsLayer(zzu=0, thk=2, wcnd='s', rhot=2100, kkk=.5);
    print(eprslyrb.classprop('eprslyrb -> '))
    eprslyrc = GMEprsLayer(zzu=0, thk=2, wcnd='w', rhot=1600, kkk=.5);
    print(eprslyrc.classprop('eprslyrc -> '))
    print()
    ## --- section_mb: (GMEprsLayer) vector properties --- ##

    '''
    '''

