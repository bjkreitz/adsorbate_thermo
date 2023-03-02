#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White transmit 1.0}
camera {perspective
  right -11.37*x up 8.81*y
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
atom(< -4.23,  -3.04,  -2.21>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #0
atom(< -1.39,  -3.01,  -2.22>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #1
atom(<  1.41,  -2.99,  -2.21>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #2
atom(< -2.81,  -2.40,  -4.59>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #3
atom(<  0.02,  -2.36,  -4.53>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #4
atom(<  2.85,  -2.39,  -4.57>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #5
atom(< -1.38,  -1.78,  -6.94>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #6
atom(<  1.46,  -1.72,  -6.94>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #7
atom(<  4.26,  -1.75,  -6.94>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #8
atom(< -4.26,  -1.20,  -0.02>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #9
atom(< -1.45,  -1.17,   0.00>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #10
atom(<  1.46,  -1.24,  -0.01>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #11
atom(< -2.86,  -0.61,  -2.41>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #12
atom(< -0.00,  -0.38,  -2.33>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #13
atom(<  2.84,  -0.57,  -2.38>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #14
atom(< -1.42,   0.07,  -4.76>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #15
atom(<  1.41,   0.06,  -4.74>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #16
atom(<  4.24,   0.05,  -4.75>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #17
atom(<  0.70,   2.85,  -2.70>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #18
atom(< -0.37,   1.24,  -1.21>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #19
atom(< -0.99,   1.07,  -0.13>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20
atom(<  0.80,   3.93,  -2.64>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #21
atom(<  1.68,   2.37,  -2.71>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #22
atom(<  0.12,   2.57,  -3.58>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #23
atom(< -0.02,   2.49,  -1.49>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24

// no constraints
