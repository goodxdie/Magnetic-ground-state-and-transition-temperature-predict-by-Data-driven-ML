from pymatgen.core import Element
# 指定需要获取磁矩的元素符号列表
elements = [Ag, Au, Cd, Co, Cr, Cu, Fe, Hf, Hg, Ir, Mn, Mo, Nb, Ni, Os,
        Pd, Pt, Re, Rh, Ru, Sc, Ta, Tc, Ti, V, W, Y, Zn, Zr, Ge, P, Si, Te]
# 获取指定元素的磁矩数据
magnetic_moments = []
for el in elements:
    element = Element(el)
    mag_moment = element.data['Magnetic Type']
    magnetic_moments.append((el, mag_moment))
# 将数据保存为 CSV 文件
with open('magnetic_moments.csv', 'w') as f:
    f.write('Element, Magnetic Moment\n')
    for el, mag_moment in magnetic_moments:
        f.write('{}, {}\n'.format(el, mag_moment))
