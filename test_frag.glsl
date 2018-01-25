// for my own purposes it uses old glsl version.
// But here also can be newer one:
/*
#version 330
in vec3 vout_color;
out vec4 final_color;
void main(void)
{
    final_color = vec4(vout_color, 1.0);
}
*/

// Just comment all below this comment and uncomment the part above it from line 3 to use newer one.

#version 120
varying vec3 vout_color;
void main(void)
{
    vec3 cur_color = vout_color;
    if (cur_color.r > 0.5) cur_color.r = 0.2;
    gl_FragColor = vec4(cur_color, 1.0);
}