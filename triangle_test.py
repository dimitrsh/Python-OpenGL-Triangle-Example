# current date: 24.01.2018
# This example based on https://gist.github.com/deepankarsharma/3494203 
# but contains additional code for old glsl shaders
# and uses actual glfw version with appropriate function calls.
# Also glfw example was used from https://github.com/FlorianRhiem/pyGLFW - look here in glfw/__init__.py if you can't find some variables. 
###############################
# it is the simple example with 2 triangles, that are drawn in quite modern opengl.
# for those like me, who didn't find the better example ;)

import glfw

import numpy as np
from OpenGL.GL import (glCreateProgram, glLinkProgram, glDeleteProgram, glCreateShader, glShaderSource, glCompileShader, glAttachShader, 
                       glDeleteShader, glClear, glClearColor, glGenBuffers, glGenVertexArrays, glGetAttribLocation, 
                       glBufferData, glBindBuffer, glBindVertexArray, glUseProgram, glVertexAttribPointer, glGetProgramiv, 
                       glGetUniformLocation, glGetShaderInfoLog, glEnableVertexAttribArray, glGetProgramInfoLog, glDrawArrays,
                       GL_FLOAT, GL_TRUE, GL_FALSE, GL_COMPILE_STATUS, GL_LINK_STATUS, GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, 
                       GL_ARRAY_BUFFER, GL_COLOR_BUFFER_BIT, GL_STATIC_DRAW, GL_TRIANGLES, GL_LINES, GL_POINTS)


# This module will draw triangles in modern opengl style.

from shader_program import ShaderProgram
# first triangle vertex and color data 
vertex_data = np.array([0.75, 0.75, 0.0,
                        0.75, -0.75, 0.0,
                        -0.75, -0.75, 0.0], dtype=np.float32)

color_data = np.array([1, 0, 0,
                        0, 1, 0,
                        0, 0, 1], dtype=np.float32)

def getTriangleVAO(program):
    # it is a container for buffers
    vao_id = glGenVertexArrays(1)
    glBindVertexArray(vao_id)
    vbo_id = glGenBuffers(2)
    # bind some GL_ARRAY_BUFFER to generated one id
    # it's a position buffer
    glBindBuffer(GL_ARRAY_BUFFER, vbo_id[0])
    # fill it with values
    glBufferData(GL_ARRAY_BUFFER, vertex_data, GL_STATIC_DRAW)
    # tell, how to interpret it
    glVertexAttribPointer(program.attrib_location('vin_position'), 3, GL_FLOAT, GL_FALSE, 0, None)
    # open the valve, let it to be used.
    glEnableVertexAttribArray(0) # (N.B.!) this indices are in VAO object. In another VAO it will start from 0 again
    # repeat it for colors.
    glBindBuffer(GL_ARRAY_BUFFER, vbo_id[1])
    glBufferData(GL_ARRAY_BUFFER, color_data, GL_STATIC_DRAW)
    glVertexAttribPointer(program.attrib_location('vin_color'), 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(1)
    # there we unbind current buffer and vertex array object
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    # will bind VAO's at every draw action.
    return vao_id
# second triangle vertex and color data 
vertex_data1 = np.array([0.0, 0.75, 0.0,
                        -0.75, 0.5, 0.0,
                        0.5, -0.95, 0.0], dtype=np.float32)

color_data1 = np.array([0, 1, 0,
                        1, 0, 0,
                        0, 0, 1], dtype=np.float32)

def getTriangleVAO1(program):
    # it is a container for buffers
    vao_id = glGenVertexArrays(1)
    glBindVertexArray(vao_id)
    vbo_id = glGenBuffers(2)
    # bind some GL_ARRAY_BUFFER to generated one id
    # it's a position buffer
    glBindBuffer(GL_ARRAY_BUFFER, vbo_id[0])
    # fill it with values
    glBufferData(GL_ARRAY_BUFFER, vertex_data1, GL_STATIC_DRAW)
    # tell, how to interpret it
    glVertexAttribPointer(program.attrib_location('vin_position'), 3, GL_FLOAT, GL_FALSE, 0, None)
    # open the valve, let it to be used.
    glEnableVertexAttribArray(0)
    # repeat it for colors.
    glBindBuffer(GL_ARRAY_BUFFER, vbo_id[1])
    glBufferData(GL_ARRAY_BUFFER, color_data1, GL_STATIC_DRAW)
    glVertexAttribPointer(program.attrib_location('vin_color'), 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(1)
    # there we unbind current buffer and vertex array object
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    # will bind VAO's at every draw action.
    return vao_id


def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Triangle_test", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3) # didn't find it in docs, just in __init__.py of glfwpy in git.
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2) # works, ofc, well with 120 shaders and 330.
    glClearColor(0.85, 0.9, 0.85, 0) # background color
    program = ShaderProgram(vertpath="test_vert.glsl", fragpath="test_frag.glsl")
    vao_id  = getTriangleVAO (program) 
    vao_id1 = getTriangleVAO1(program)
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClear(GL_COLOR_BUFFER_BIT)
        # use our shader program in this part -> make program object to be a part of a rendering process.
        glUseProgram(program.program_id)
        # use vao with coords and colors buffers for triangle
        glBindVertexArray(vao_id)
        # how to draw
        glDrawArrays(GL_TRIANGLES, 0, 3)
        # unbind shader program
        glUseProgram(0)
        # unbind vao
        glBindVertexArray(0)
        # here we can draw something another 
        # some more objects in another vao.
        glUseProgram(program.program_id)
        # use vao with coords and colors buffers for triangle
        glBindVertexArray(vao_id1)
        # how to draw
        glDrawArrays(GL_TRIANGLES, 0, 3)
        # unbind shader program
        glUseProgram(0)
        # unbind vao
        glBindVertexArray(0)
        # Swap front and back buffers
        glfw.swap_buffers(window)
        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()