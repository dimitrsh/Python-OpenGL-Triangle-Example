This example based on https://gist.github.com/deepankarsharma/3494203 
but contains additional code for old glsl shaders
and uses actual glfw version with appropriate function calls.
Also glfw example was used from https://github.com/FlorianRhiem/pyGLFW - look here in code if you can't find some variables. 

It is the simple example with 2 triangles, that are drawn in quite modern opengl.
For those like me, who didn't find the better example ;)

PyOpenGL and glfw for Python2/3 should also be installed!

I use Debian-linux, so instructions will work on Debian/Ubuntu.

It can be built with both python2 and python3, f.e. for python3 - install glfw for python3 and upgrade PyOpenGL with pip3:
    
    sudo pip3 install glfw

    sudo pip3 install --upgrade PyOpenGL

without upgrade it may fail with "AttributeError: module 'OpenGL.GL' has no attribute 'GL_READ_WRITE'" or smth like this

To run, just type in terminal:
    
    python2 triangle_test.py

Or 

    python3 triangle_test.py 
