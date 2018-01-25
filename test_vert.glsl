// for my own purposes it uses old glsl version.
// But here also can be newer one:
/*
#version 330
in  vec3 vin_position;
in  vec3 vin_color;
out vec3 vout_color;
void main(void)
{
    vout_color = vin_color;
    gl_Position = vec4(vin_position, 1.0);
}
*/

// Just comment all below this comment and uncomment the part above it from line 3 to use newer one.

#version 120
attribute vec3 vin_position;
attribute vec3 vin_color;
varying   vec3 vout_color;
void main(void)
{
    vout_color = vin_color;
    gl_Position = vec4(vin_position, 1.0);
}
