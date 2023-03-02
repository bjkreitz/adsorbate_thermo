#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White transmit 1.0}
camera {perspective
  right -9.33*x up 8.45*y
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
atom(< -1.62,  -2.86,  -8.49>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #0
atom(< -1.61,  -2.84,  -5.65>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #1
atom(< -1.61,  -2.82,  -2.85>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #2
atom(<  0.84,  -2.86,  -7.07>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #3
atom(<  0.80,  -2.80,  -4.24>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #4
atom(<  0.82,  -2.85,  -1.41>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #5
atom(<  3.27,  -2.87,  -5.64>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #6
atom(<  3.29,  -2.81,  -2.80>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #7
atom(<  3.28,  -2.84,   0.00>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #8
atom(< -3.27,  -0.52,  -8.52>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #9
atom(< -3.27,  -0.48,  -5.70>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #10
atom(< -3.29,  -0.56,  -2.80>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #11
atom(< -0.80,  -0.56,  -7.12>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #12
atom(< -0.82,  -0.33,  -4.26>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #13
atom(< -0.82,  -0.52,  -1.42>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #14
atom(<  1.64,  -0.52,  -5.68>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #15
atom(<  1.63,  -0.53,  -2.85>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #16
atom(<  1.63,  -0.53,  -0.01>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #17
atom(<  0.37,   2.70,  -3.56>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #18
atom(< -1.48,   1.53,  -4.63>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #19
atom(< -2.57,   1.65,  -5.25>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20
atom(<  0.59,   3.76,  -3.46>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #21
atom(<  0.26,   2.23,  -2.58>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #22
atom(<  1.15,   2.20,  -4.14>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #23
atom(< -0.89,   2.67,  -4.28>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24

// no constraints
