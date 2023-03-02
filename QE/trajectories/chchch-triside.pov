#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White transmit 1.0}
camera {perspective
  right -9.44*x up 7.06*y
  direction 100.00*z
  location <0,0,100.00> look_at <0,0,0>}


light_source {<  2.00,   3.00,  40.00> color White
  area_light <0.70, 0, 0>, <0, 0.70, 0>, 3, 3
  adaptive 1 jitter}
// no fog
#declare simple = finish {phong 0.7}
#declare pale = finish {ambient 0.5 diffuse 0.85 roughness 0.001 specular 0.200 }
#declare intermediate = finish {ambient 0.3 diffuse 0.6 specular 0.1 roughness 0.04}
#declare vmd = finish {ambient 0.0 diffuse 0.65 phong 0.1 phong_size 40.0 specular 0.5 }
#declare jmol = finish {ambient 0.2 diffuse 0.6 specular 1 roughness 0.001 metallic}
#declare ase2 = finish {ambient 0.05 brilliance 3 diffuse 0.6 metallic specular 0.7 roughness 0.04 reflection 0.15}
#declare ase3 = finish {ambient 0.15 brilliance 2 diffuse 0.6 metallic specular 1.0 roughness 0.001 reflection 0.0}
#declare glass = finish {ambient 0.05 diffuse 0.3 specular 1.0 roughness 0.001}
#declare glass2 = finish {ambient 0.01 diffuse 0.3 specular 1.0 reflection 0.25 roughness 0.001}
#declare Rcell = 0.050;
#declare Rbond = 0.100;

#macro atom(LOC, R, COL, TRANS, FIN)
  sphere{LOC, R texture{pigment{color COL transmit TRANS} finish{FIN}}}
#end
#macro constrain(LOC, R, COL, TRANS FIN)
union{torus{R, Rcell rotate 45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
     torus{R, Rcell rotate -45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
     translate LOC}
#end

// no cell vertices
atom(< -1.55,  -2.13,  -8.50>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #0
atom(< -1.53,  -2.16,  -5.62>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #1
atom(< -1.57,  -2.16,  -2.83>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #2
atom(<  0.89,  -2.14,  -7.09>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #3
atom(<  0.88,  -2.15,  -4.24>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #4
atom(<  0.87,  -2.16,  -1.42>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #5
atom(<  3.32,  -2.19,  -5.64>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #6
atom(<  3.34,  -2.21,  -2.82>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #7
atom(<  3.30,  -2.18,   0.00>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #8
atom(< -3.27,   0.15,  -8.44>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #9
atom(< -3.18,   0.10,  -5.62>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #10
atom(< -3.34,   0.09,  -2.83>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #11
atom(< -0.80,   0.17,  -6.99>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #12
atom(< -0.74,   0.34,  -4.18>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #13
atom(< -0.95,   0.26,  -1.30>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #14
atom(<  1.65,   0.17,  -5.67>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #15
atom(<  1.75,   0.17,  -2.84>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #16
atom(<  1.60,   0.34,  -0.06>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #17
atom(< -0.86,   1.83,  -2.81>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #18
atom(<  0.04,   2.24,  -1.79>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #19
atom(<  1.41,   1.75,  -1.63>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #20
atom(< -1.74,   2.46,  -2.95>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #21
atom(< -0.26,   3.10,  -1.18>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #22
atom(<  2.18,   2.51,  -1.49>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #23

// no constraints
