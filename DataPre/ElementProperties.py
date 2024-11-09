from mendeleev import H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr, Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe, Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn
from mendeleev.fetch import fetch_ionization_energies
name = [Ag, Au, Cd, Co, Cr, Cu, Fe, Hf, Hg, Ir, Mn, Mo, Nb, Ni, Os,
        Pd, Pt, Re, Rh, Ru, Sc, Ta, Tc, Ti, V, W, Y, Zn, Zr, Ge, P, Si, Te]
with open('dataPart.csv', 'w') as f:
    for i in name:
        # 半径  原子数  质量  偶极极化率 电子亲和势 价电子数,6
        S = str((i.atomic_radius, i.atomic_number, i.atomic_weight, i.dipole_polarizability,
                 i.electron_affinity, i.nvalence()))
        #S = str((i.nvalence()))
        f.writelines(str(i)+S+'\n')
