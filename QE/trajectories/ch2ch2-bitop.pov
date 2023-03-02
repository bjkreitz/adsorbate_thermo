#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White transmit 1.0}
camera {perspective
  right -12.10*x up 9.34*y
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
atom(< -4.59,  -1.60,  -4.89>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #0
atom(< -1.78,  -1.62,  -4.92>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #1
atom(<  1.03,  -1.60,  -4.89>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #2
atom(< -3.19,   0.81,  -4.91>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #3
atom(< -0.37,   0.81,  -4.91>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #4
atom(<  2.47,   0.82,  -4.93>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #5
atom(< -1.78,   3.29,  -4.95>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #6
atom(<  1.04,   3.27,  -4.95>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #7
atom(<  3.89,   3.27,  -4.95>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #8
atom(< -4.61,  -3.25,  -2.62>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #9
atom(< -1.78,  -3.29,  -2.65>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #10
atom(<  1.05,  -3.25,  -2.62>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #11
atom(< -3.16,  -0.81,  -2.44>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #12
atom(< -0.40,  -0.81,  -2.43>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #13
atom(<  2.46,  -0.80,  -2.59>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #14
atom(< -1.78,   1.69,  -2.64>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #15
atom(<  1.05,   1.64,  -2.61>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #16
atom(<  3.88,   1.64,  -2.61>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #17
atom(< -2.53,  -0.81,  -0.41>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #18
atom(< -1.04,  -0.81,  -0.41>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #19
atom(< -2.98,  -1.72,  -0.01>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #20
atom(<  5.50,   0.09,  -0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #21
atom(< -0.58,  -1.71,  -0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #22
atom(< -0.59,   0.10,   0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #23

// no constraints
