#!/usr/bin/env python 
# encoding: utf-8 

name = "Surface Adsorption Corrections"
shortDesc = u""
longDesc = u"""
Changes due to adsorbing on a surface.
Here, Pt(111)
Note: "-h" means "horizontal"
"""

entry( 
    index = 1,
    label = "R*",
    group= 
"""
1 R u0
2 X u0
""",
    thermo=None,
    shortDesc=u"""Anything adsorbed anyhow.""",
    longDesc=u"""
   R
   x
***********
This node should be empty, ensuring that one of the nodes below is used.
""",
)

entry( 
    index = 1,
    label = "CR2CR2CR3",
    group = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {2,S}
7 R u0 p0 c0 {2,S}
8 R u0 p0 c0 {3,S}
9 R u0 p0 c0 {3,S}
10 R u0 p0 c0 {3,S}
11 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.55, 6.96, 9.45, 11.26, 13.57, 14.85, 16.12], 'J/(mol*K)'),
        H298=(-208.97, 'kJ/mol'),
        S298=(-210.73, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2CH2CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 2,
    label = "CR2CR2OR",
    group = 
"""
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {3,S}
7 R u0 p0 c0 {3,S}
8 R u0 p0 c0 {1,S}
9 X u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.17, -3.29, -0.52, 1.48, 4.01, 5.46, 7.1], 'J/(mol*K)'),
        H298=(-231.15, 'kJ/mol'),
        S298=(-175.31, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2CH2OH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 3,
    label = "CR2CR3",
    group = 
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {3,S}
8 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.06, 5.79, 8.47, 10.4, 12.82, 14.17, 15.62], 'J/(mol*K)'),
        H298=(-200.7, 'kJ/mol'),
        S298=(-194.94, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 4,
    label = "CR2CRCR2-mono",
    group = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {2,S}
7 R u0 p0 c0 {3,S}
8 R u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.46, 0.05, 2.05, 3.56, 5.54, 6.65, 7.79], 'J/(mol*K)'),
        H298=(-195.67, 'kJ/mol'),
        S298=(-155.85, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2CHCH2-mono single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 5,
    label = "CR2CRO-mono",
    group = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {3,S}
7 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.68, 0.82, 2.62, 3.95, 5.76, 6.81, 7.9], 'J/(mol*K)'),
        H298=(-225.47, 'kJ/mol'),
        S298=(-159.45, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2CHO-mono double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 6,
    label = "CR3",
    group = 
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 R  u0 p0 c0 {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.59, 2.2, 5.74, 8.34, 11.69, 13.59, 15.58], 'J/(mol*K)'),
        H298=(-193.8, 'kJ/mol'),
        S298=(-155.84, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 7,
    label = "CR3CRCR3",
    group = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 R u0 p0 c0 {2,S}
8 R u0 p0 c0 {3,S}
9 R u0 p0 c0 {3,S}
10 R u0 p0 c0 {3,S}
11 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.17, 8.07, 10.44, 11.93, 13.57, 14.42, 15.43], 'J/(mol*K)'),
        H298=(-201.26, 'kJ/mol'),
        S298=(-218.44, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3CHCH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 8,
    label = "CR3CROR",
    group = 
"""
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {3,S}
6 R u0 p0 c0 {3,S}
7 R u0 p0 c0 {3,S}
8 R u0 p0 c0 {1,S}
9 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.68, 2.1, 3.89, 5.05, 6.38, 7.09, 7.87], 'J/(mol*K)'),
        H298=(-230.23, 'kJ/mol'),
        S298=(-161.99, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3CHOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 9,
    label = "R2COR",
    group = 
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.61, -2.1, 0.51, 2.42, 4.89, 6.29, 7.73], 'J/(mol*K)'),
        H298=(-220.91, 'kJ/mol'),
        S298=(-153.14, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from H2COH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 10,
    label = "CR2CCR3",
    group = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {9,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {1,S}
7 R u0 p0 c0 {3,S}
8 R u0 p0 c0 {3,S}
9 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.21, 7.01, 10.5, 12.58, 14.58, 15.4, 16.09], 'J/(mol*K)'),
        H298=(-322.09, 'kJ/mol'),
        S298=(-224.56, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2CCH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 11,
    label = "CR2COR",
    group = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 R u0 p0 c0 {3,S}
5 R u0 p0 c0 {3,S}
6 R u0 p0 c0 {1,S}
7 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.44, 6.26, 7.2, 7.7, 8.15, 8.31, 8.42], 'J/(mol*K)'),
        H298=(-293.92, 'kJ/mol'),
        S298=(-153.64, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2COH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 12,
    label = "CR3CO",
    group = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.03, 2.39, 4.05, 5.19, 6.51, 7.15, 7.8], 'J/(mol*K)'),
        H298=(-279.61, 'kJ/mol'),
        S298=(-160.67, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3CO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 13,
    label = "CRCCR2",
    group = 
"""
1 C u0 p0 c0 {3,D} {4,S} {7,S}
2 C u0 p0 c0 {3,D} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,D}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.41, 3.72, 7.67, 10.5, 13.84, 15.47, 16.78], 'J/(mol*K)'),
        H298=(-272.91, 'kJ/mol'),
        S298=(-184.12, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 14,
    label = "CRCR2",
    group = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 R  u0  p0 c0 {2,S}
5 R  u0  p0 c0 {3,S}
6 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.58, 7.63, 9.78, 11.32, 13.19, 14.22, 15.4], 'J/(mol*K)'),
        H298=(-268.02, 'kJ/mol'),
        S298=(-179.96, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 15,
    label = "CRCRCR3-mono",
    group = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {1,S}
7 R u0 p0 c0 {2,S}
8 R u0 p0 c0 {3,S}
9 X u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.38, -0.31, 1.59, 3.09, 5.07, 6.19, 7.41], 'J/(mol*K)'),
        H298=(-283.9, 'kJ/mol'),
        S298=(-170.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCHCH3-mono single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 16,
    label = "CRCO-mono",
    group = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 R u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.55, -4.82, -2.31, -0.6, 1.49, 2.62, 3.75], 'J/(mol*K)'),
        H298=(-304.39, 'kJ/mol'),
        S298=(-153.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCO-mono double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 17,
    label = "COOR",
    group = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 R u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.1, 3.6, 5.13, 6.12, 7.27, 7.86, 8.41], 'J/(mol*K)'),
        H298=(-294.57, 'kJ/mol'),
        S298=(-154.05, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from COOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 18,
    label = "RCO-mono",
    group = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 R  u0  p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.42, 8.26, 10.63, 12.12, 13.7, 14.49, 15.43], 'J/(mol*K)'),
        H298=(-266.93, 'kJ/mol'),
        S298=(-163.88, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HCO-mono single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 19,
    label = "C",
    group = 
"""
1 X u0 p0 c0 {2,Q}
2 C u0 p0 c0 {1,Q}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.34, -3.34, -1.0, 0.42, 1.97, 2.73, 3.51], 'J/(mol*K)'),
        H298=(-657.91, 'kJ/mol'),
        S298=(-133.84, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from C quadruple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 20,
    label = "CR",
    group = 
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.04, -0.75, 3.1, 5.48, 8.05, 9.33, 10.79], 'J/(mol*K)'),
        H298=(-619.32, 'kJ/mol'),
        S298=(-165.81, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 21,
    label = "COR",
    group = 
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.83, 9.83, 11.9, 12.95, 13.69, 13.91, 14.43], 'J/(mol*K)'),
        H298=(-463.49, 'kJ/mol'),
        S298=(-187.54, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from COH triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 22,
    label = "CCRCR2",
    group = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {7,T}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.26, 4.53, 7.18, 9.16, 11.68, 13.1, 14.8], 'J/(mol*K)'),
        H298=(-568.85, 'kJ/mol'),
        S298=(-197.63, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CCHCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 23,
    label = "CCR3",
    group = 
"""
1 X  u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.5, 3.54, 6.44, 8.47, 10.96, 12.37, 14.19], 'J/(mol*K)'),
        H298=(-591.35, 'kJ/mol'),
        S298=(-166.06, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CCH3 triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 24,
    label = "CCR2CR3",
    group = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,T}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {2,S}
7 R u0 p0 c0 {2,S}
8 R u0 p0 c0 {2,S}
9 X u0 p0 c0 {3,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.15, 5.31, 7.68, 9.44, 11.71, 13.04, 14.7], 'J/(mol*K)'),
        H298=(-598.94, 'kJ/mol'),
        S298=(-188.36, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CCH2CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 25,
    label = "CR2",
    group = 
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 R  u0 p0 c0 {2,S}
4 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.03, 1.86, 6.14, 8.81, 11.7, 13.14, 14.75], 'J/(mol*K)'),
        H298=(-390.72, 'kJ/mol'),
        S298=(-176.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 26,
    label = "CR3CCR3",
    group = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {2,S} {10,D}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {1,S}
7 R u0 p0 c0 {2,S}
8 R u0 p0 c0 {2,S}
9 R u0 p0 c0 {2,S}
10 X u0 p0 c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.07, 9.75, 11.48, 12.64, 14.03, 14.78, 15.67], 'J/(mol*K)'),
        H298=(-373.64, 'kJ/mol'),
        S298=(-186.25, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3CCH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 27,
    label = "CR3COR",
    group = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {8,D}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 R u0 p0 c0 {1,S}
8 X u0 p0 c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.69, 3.6, 4.78, 5.62, 6.8, 7.54, 8.34], 'J/(mol*K)'),
        H298=(-329.24, 'kJ/mol'),
        S298=(-150.16, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3COH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 28,
    label = "CRCR2CR3",
    group = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,S} {10,D}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {2,S}
7 R u0 p0 c0 {2,S}
8 R u0 p0 c0 {2,S}
9 R u0 p0 c0 {3,S}
10 X u0 p0 c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.99, -0.77, 1.3, 2.67, 4.29, 5.24, 6.54], 'J/(mol*K)'),
        H298=(-392.61, 'kJ/mol'),
        S298=(-175.14, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCH2CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 29,
    label = "CRCR3",
    group = 
"""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.35, 6.29, 8.83, 10.51, 12.44, 13.49, 14.83], 'J/(mol*K)'),
        H298=(-393.42, 'kJ/mol'),
        S298=(-204.61, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCH3 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 30,
    label = "CRCRCR2-mono",
    group = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {8,D}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {3,S}
7 R u0 p0 c0 {3,S}
8 X u0 p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.76, 7.89, 9.98, 11.39, 13.04, 13.93, 15.06], 'J/(mol*K)'),
        H298=(-349.41, 'kJ/mol'),
        S298=(-189.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCHCH2-mono single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 31,
    label = "CRCRO-mono",
    group = 
"""
1 C u0 p0 c0 {2,S} {4,S} {6,D}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 O u0 p2 c0 {2,D} 
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.13, 0.28, 2.49, 4.02, 5.96, 7.05, 8.08], 'J/(mol*K)'),
        H298=(-408.93, 'kJ/mol'),
        S298=(-168.76, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCHO-mono double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 32,
    label = "RCOR",
    group = 
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.78, 2.03, 4.17, 5.43, 6.75, 7.43, 8.13], 'J/(mol*K)'),
        H298=(-322.53, 'kJ/mol'),
        S298=(-142.98, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HCOH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 33,
    label = "CCO",
    group = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.14, 6.88, 8.38, 9.3, 10.36, 10.96, 11.69], 'J/(mol*K)'),
        H298=(-539.56, 'kJ/mol'),
        S298=(-185.87, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CCO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 34,
    label = "CCR2-mono",
    group = 
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D} {4,S} {5,S}
4 R  u0  p0 c0 {3,S}
5 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.07, 8.05, 10.43, 11.96, 13.73, 14.66, 15.7], 'J/(mol*K)'),
        H298=(-298.78, 'kJ/mol'),
        S298=(-173.97, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CCH2-mono double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 35,
    label = "CCCR2-mono",
    group = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 X u0 p0 c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.62, 3.86, 5.44, 6.28, 7.1, 7.49, 7.91], 'J/(mol*K)'),
        H298=(-451.02, 'kJ/mol'),
        S298=(-146.53, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CCCH2-mono single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 36,
    label = "OR",
    group = 
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.31, 8.06, 9.52, 10.37, 11.23, 11.63, 12.03], 'J/(mol*K)'),
        H298=(-187.76, 'kJ/mol'),
        S298=(-107.07, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from OH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 37,
    label = "RCO3",
    group = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {4,S} {5,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 R u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.13, 12.41, 13.82, 14.68, 15.58, 15.98, 16.35], 'J/(mol*K)'),
        H298=(-301.81, 'kJ/mol'),
        S298=(-198.4, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HCO3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 38,
    label = "RCOO-mono",
    group = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 R u0 p0 c0 {3,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([13.89, 15.27, 15.81, 16.11, 16.49, 16.72, 16.88], 'J/(mol*K)'),
        H298=(-240.63, 'kJ/mol'),
        S298=(-182.45, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HCOO-mono double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 39,
    label = "OCRCR2",
    group = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {3,S}
6 R u0 p0 c0 {3,S}
7 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.49, 12.42, 13.99, 14.85, 15.65, 15.99, 16.31], 'J/(mol*K)'),
        H298=(-141.67, 'kJ/mol'),
        S298=(-201.85, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from OCHCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 40,
    label = "OCR3",
    group = 
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.37, 2.23, 2.86, 3.4, 4.22, 4.83, 6.0], 'J/(mol*K)'),
        H298=(-179.22, 'kJ/mol'),
        S298=(-138.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from OCH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 41,
    label = "OCR2CR3",
    group = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {3,S}
7 R u0 p0 c0 {3,S}
8 R u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.78, 1.84, 2.75, 3.54, 4.75, 5.57, 6.75], 'J/(mol*K)'),
        H298=(-195.06, 'kJ/mol'),
        S298=(-159.38, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from OCH2CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 42,
    label = "OOR",
    group = 
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.21, 11.38, 11.38, 11.02, 10.19, 9.56, 8.77], 'J/(mol*K)'),
        H298=(-134.04, 'kJ/mol'),
        S298=(-120.71, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from OOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 43,
    label = "O",
    group = 
"""
1 X u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.44, 0.14, 1.49, 2.26, 3.07, 3.45, 3.84], 'J/(mol*K)'),
        H298=(-382.56, 'kJ/mol'),
        S298=(-140.6, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from O double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 44,
    label = "CR3CR2CO",
    group = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 C u0 p0 c0 {1,D} {2,S} {10,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 R u0 p0 c0 {3,S}
8 R u0 p0 c0 {3,S}
9 R u0 p0 c0 {3,S}
10 X u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.18, 2.59, 4.42, 5.64, 7.01, 7.65, 8.17], 'J/(mol*K)'),
        H298=(-265.84, 'kJ/mol'),
        S298=(-173.89, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3CH2CO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 45,
    label = "CCRO",
    group = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,T}
4 R u0 p0 c0 {2,S}
5 X u0 p0 c0 {3,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.16, 0.76, 2.61, 3.92, 5.66, 6.69, 7.78], 'J/(mol*K)'),
        H298=(-561.45, 'kJ/mol'),
        S298=(-162.94, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CCHO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 46,
    label = "CCR2OR",
    group = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {7,T}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {1,S}
7 X u0 p0 c0 {3,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.38, -4.1, -1.58, 0.31, 2.75, 4.18, 6.0], 'J/(mol*K)'),
        H298=(-594.41, 'kJ/mol'),
        S298=(-168.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CCH2OH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 47,
    label = "OCR2OR",
    group = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S} 
3 O u0 p2 c0 {1,S} {6,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {3,S}
7 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.18, 2.65, 3.17, 3.67, 4.5, 5.15, 6.29], 'J/(mol*K)'),
        H298=(-173.38, 'kJ/mol'),
        S298=(-151.71, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from OCH2OH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)



    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.84, 4.02, 6.08, 7.46, 9.09, 9.97, 10.96], 'J/(mol*K)'),
        H298=(-331.96, 'kJ/mol'),
        S298=(-169.67, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)