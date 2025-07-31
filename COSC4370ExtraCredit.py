import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

Dx = 1/10 # X displacement
Dy = 1/2 # Y displacement
Dt = 0.053 # Additional Y displacement to center the triangles

def Tetrahedron():
    vertices = (
        (math.sqrt(8/9), 0, -1/3),
        (-math.sqrt(2/9), math.sqrt(2/3), -1/3),
        (-math.sqrt(2/9), -math.sqrt(2/3), -1/3),
        (0, 0, 1),
        )
    
    edges = (
        (0,1), (0,2), (0,3),
        (1,2), (1,3),
        (2,3)
        )
    
    faces = ((0,1,2), (3,0,1), (3,1,2), (3,2,0))
    
    texture_coords = [
        ((1/20, 1/2 + Dt), (1/10, 0 + Dt), (0, 0 + Dt)),                     
        ((1/10 + Dx, 0 + Dt), (1/20 + Dx, 1/2 + Dt), (0 + Dx, 0 + Dt)),        
        ((1/10 + 2 * Dx, 0 + Dt), (1/20 + 2 * Dx, 1/2 + Dt), (0 + 2 * Dx, 0 + Dt)), 
        ((1/10 + 3 * Dx, 0 + Dt), (1/20 + 3 * Dx, 1/2 + Dt), (0 + 3 * Dx, 0 + Dt))  
        ]
    
    vertex_colors = [
        (1, 0, 0),  # Red for vertex 0
        (0, 1, 0),  # Green for vertex 1
        (0, 0, 1),  # Blue for vertex 2
        (1, 1, 0)   # Yellow for vertex 3
    ]
    

    glColor(1,1,1) # Draw the Icosahedron outline in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd() 
    
    for face_index, face in enumerate(faces):
        glBegin(GL_TRIANGLES)
        for vertex_index, vertex in enumerate(face):
           glColor3fv(vertex_colors[vertex])  # Set color for each vertex
           glTexCoord2fv(texture_coords[face_index][vertex_index])
           glVertex3fv(vertices[vertex])
        glEnd()
        
def Cube(vx, vy, vz, texture):
    d = 1/math.sqrt(3) # 1 divided by space diagonal
    vertices = [
        (d, -d, -d), (d, d, -d), (-d, d, -d), (-d, -d, -d), 
        (d, -d, d), (d, d, d), (-d, -d, d), (-d, d, d)
        ]
    
    edges = [
        (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
        (6,3), (6,4), (6,7), (5,1), (5,4), (5,7)
        ]
    
    texture_coords = [
        ((0, 0), (0, 1/2), (1/10, 1/2), (1/10, 0)),
        ((0 + Dx, 0), (0 + Dx, 1/2), (1/10 + Dx, 1/2), (1/10 + Dx, 0)),
        ((0 + 2 * Dx, 0), (0 + 2 * Dx, 1/2), (1/10 + 2 * Dx, 1/2), (1/10 + 2 * Dx, 0)),
        ((0 + 3 * Dx, 0), (0 + 3 * Dx, 1/2), (1/10 + 3 * Dx, 1/2), (1/10 + 3 * Dx, 0)),
        ((0 + 4 * Dx, 0), (0 + 4 * Dx, 1/2), (1/10 + 4 * Dx, 1/2), (1/10 + 4 * Dx, 0)),
        ((0 + 5 * Dx, 0), (0 + 5 * Dx, 1/2), (1/10 + 5 * Dx, 1/2), (1/10 + 5 * Dx, 0)),  
    ]
    
    vertex_colors = [
        (1, 0, 0), 
        (0, 1, 0),  
        (0, 0, 1),  
        (1, 1, 0),   
        (1, 0, 1),  
        (0, 1, 1),  
        (0, 0.5, 1),  
        (1, 0.5, 0)  
        
    ]
    
    faces = ((0,1,2,3), 
             (3,2,7,6), 
             (6,7,5,4), 
             (4,5,1,0), 
             (1,5,7,2), 
             (4,0,3,6))
    
    glColor(1,1,1) 
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd() 
    
    for face_index, face in enumerate(faces):
        glBegin(GL_QUADS)
        for vertex_index, vertex in enumerate(face):
           glColor3fv(vertex_colors[vertex])  # Set color for each vertex
           glTexCoord2fv(texture_coords[face_index][vertex_index])
           glVertex3fv(vertices[vertex])
        glEnd()
  
def Octahedron(): 
    d = 1
    
    vertices = [
        (d, 0, 0),
        (0, d, 0),
        (0, 0, d),
        (-d, 0, 0),
        (0, -d, 0),
        (0, 0, -d)
        ]

    edges = [
        (0,1), (0,2), (0,4), (0,5), 
        (1,2), (1,3), (1,5),
        (2,3), (2,4),
        (3,4), (3,5),
        (4,5)
        ]
    
    texture_coords = [
        ((0, 0 + Dt), (1/10, 0 + Dt), (1/20, 1/2 + Dt)),                     
        ((1/20 + Dx, 1/2 + Dt), (1/10 + Dx, 0 + Dt),(0 + Dx, 0 + Dt)),        
        ((1/20 + 2 * Dx, 1/2 + Dt), (1/10 + 2 * Dx, 0 + Dt), (0 + 2 * Dx, 0 + Dt)), 
        ( (1/10 + 3 * Dx, 0 + Dt), (1/20 + 3 * Dx, 1/2 + Dt), (0 + 3 * Dx, 0 + Dt)),
        ((1/20 + 4 * Dx, 1/2 + Dt), (1/10 + 4 * Dx, 0 + Dt), (0 + 4 * Dx, 0 + Dt)),
        ((1/10 + 5 * Dx, 0 + Dt), (1/20 + 5 * Dx, 1/2 + Dt), (0 + 5 * Dx, 0 + Dt)),
        ((1/10 + 6 * Dx, 0 + Dt), (1/20 + 6 * Dx, 1/2 + Dt), (0 + 6 * Dx, 0 + Dt)),
        ((1/10 + 7 * Dx, 0 + Dt), (1/20 + 7 * Dx, 1/2 + Dt), (0 + 7 * Dx, 0 + Dt)),
        ]
    
    vertex_colors = [
        (1, 0, 0), 
        (0, 1, 0),  
        (0, 0, 1),  
        (1, 1, 0),   
        (1, 0, 1),  
        (0, 1, 1),  
        (0, 0.5, 1),  
        (1, 0.5, 0)   
        ]
    
    faces = ((2,4,0), 
             (0,2,1), 
             (1,2,3), 
             (2,3,4), 
             (3,5,4), 
             (4,5,0), 
             (0,5,1), 
             (1,5,3),
             )
    
    glColor(1,1,1) # Draw the Octahedron outline in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    for face_index, face in enumerate(faces):
        glBegin(GL_TRIANGLES)
        for vertex_index, vertex in enumerate(face):
           glColor3fv(vertex_colors[vertex])  # Set color for each vertex
           glTexCoord2fv(texture_coords[face_index][vertex_index])
           glVertex3fv(vertices[vertex])
        glEnd()

def Dodecahedron():
    d = 1/math.sqrt(3)
    p = 1.618/math.sqrt(3)
    s = 1/(1.618 * math.sqrt(3)) #phi divided by sqrt 3
    
    vertices = [
        (d,d,d),
        (-d,d,d),
        (d,-d,d),
        (-d,-d,d),
        (d,d,-d),
        (-d,d,-d),
        (d,-d,-d),
        (-d,-d,-d),
        (0,p,s),
        (0,-p,s),
        (0,p,-s),
        (0,-p,-s),
        (p,s,0),
        (p,-s,0),
        (-p,s,0),
        (-p,-s,0),
        (s,0,p),
        (s,0,-p),
        (-s,0,p),
        (-s,0,-p)
        ]

    edges = [
        (0,8),(0,12),(0,16),
        (1,8), (1,14), (1,18),
        (2,9), (2,13), (2,16),
        (3,9), (3,15), (3,18),
        (4,10), (4,12), (4,17), 
        (5,10), (5,14), (5,19),
        (6,11), (6,13), (6,17),
        (7,11), (7,15), (7,19),
        (8,10),
        (9,11),
        (12,13),
        (14,15),
        (16,18),
        (17,19),
        ]
    
    b = (455+10+480)
    texture_coords = [
        # face 1
        ((0, 1 - 655/960), (1/20, 1 - 492.5/960), (1/10, 1 - 655/960), (387/4800, 1 - b/960), (91/4800, 1 - b/960)),
        # face 2
        ((0 + Dx, 1 - 655/960), (1/20 + Dx, 1 - 492.5/960), (1/10 + Dx, 1 - 655/960), (387/4800 + Dx, 1 - b/960), (91/4800 + Dx, 1 - b/960)),
        # face 3
        ((0 + 2*Dx, 1 - 655/960), (1/20 + 2*Dx, 1 - 492.5/960), (1/10 + 2*Dx, 1 - 655/960), (387/4800 + 2*Dx, 1 - b/960), (91/4800 + 2*Dx, 1 - b/960)),
        # face 4
        ((0 + 3*Dx, 1 - 655/960), (1/20 + 3*Dx, 1 - 492.5/960), (1/10 + 3*Dx, 1 - 655/960), (387/4800 + 3*Dx, 1 - b/960), (91/4800 + 3*Dx, 1 - b/960)),
        # face 5
        ((0 + 4*Dx, 1 - 655/960), (1/20 + 4*Dx, 1 - 492.5/960), (1/10 + 4*Dx, 1 - 655/960), (387/4800 + 4*Dx, 1 - b/960), (91/4800 + 4*Dx, 1 - b/960)),
        # face 6
        ((0 + 5*Dx, 1 - 655/960), (1/20 + 5*Dx, 1 - 492.5/960), (1/10 + 5*Dx, 1 - 655/960), (387/4800 + 5*Dx, 1 - b/960), (91/4800 + 5*Dx, 1 - b/960)),
        # face 7
        ((0 + 6*Dx, 1 - 655/960), (1/20 + 6*Dx, 1 - 492.5/960), (1/10 + 6*Dx, 1 - 655/960), (387/4800 + 6*Dx, 1 - b/960), (91/4800 + 6*Dx, 1 - b/960)),
        # face 8
        ((0 + 7*Dx, 1 - 655/960), (1/20 + 7*Dx, 1 - 492.5/960), (1/10 + 7*Dx, 1 - 655/960), (387/4800 + 7*Dx, 1 - b/960), (91/4800 + 7*Dx, 1 - b/960)),
        # face 9
        ((0 + 8*Dx, 1 - 655/960), (1/20 + 8*Dx, 1 - 492.5/960), (1/10 + 8*Dx, 1 - 655/960), (387/4800 + 8*Dx, 1 - b/960), (91/4800 + 8*Dx, 1 - b/960)),
        # face 10
        ((0 + 9*Dx, 1 - 655/960), (1/20 + 9*Dx, 1 - 492.5/960), (1/10 + 9*Dx, 1 - 655/960), (387/4800 + 9*Dx, 1 - b/960), (91/4800 + 9*Dx, 1 - b/960)),
        # face 11 
        ((0, 1 - 175/960), (1/20, 1 - 12.5/960), (1/10, 1 - 175/960), (387/4800, 1 - (b-480)/960), (91/4800, 1 - (b-480)/960)),
        # face 12 
        ((0 + Dx, 1 - 175/960), (1/20 + Dx, 1 - 12.5/960), (1/10 + Dx, 1 - 175/960), (387/4800 + Dx, 1 - (b-480)/960), (91/4800 + Dx, 1 - (b-480)/960))
        ]
    
    vertex_colors = [
        (1, 0, 0), 
        (0, 1, 0),  
        (0, 0, 1),  
        (1, 1, 0),   
        (1, 0, 1),  
        (0, 1, 1),  
        (0, 0.5, 1),  
        (1, 0.5, 0),  
        (1, 0, 0), 
        (0, 1, 0),  
        (0, 0, 1),  
        (1, 1, 0),   
        (1, 0, 1),  
        (0, 1, 1),  
        (0, 0.5, 1),  
        (1, 0.5, 0),  
        (1, 0, 1),  
        (0, 1, 1),  
        (0, 0.5, 1),  
        (1, 0.5, 0),  
    ]
    
    faces = (
                # Face 1
                (18,16,2,9,3), 
                # Face 2
                (18,3,15,14,1), 
                # Face 3
                (18,1,8,0,16), 
                # Face 4
                (16,0,12,13,2),  
                # Face 5
                (15,3,9,11,7), 
                # Face 6
                (9,2,13,6,11), 
                # Face 7
                (13,12,4,17,6), 
                # Face 8
                (0,8,10,4,12), 
                # Face 9
                (8,1,14,5,10),   
                # Face 10
                (14,15,7,19,5), 
                # Face 11
                (17,19,7,11,6),
                # Face 12
                (19,17,4,10,5)
                )
    
    glColor(1,1,1) # Draw the Dodecahedron in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()       
    
    for face_index, face in enumerate(faces):
        glBegin(GL_POLYGON)
        for vertex_index, vertex in enumerate(face):
           glColor3fv(vertex_colors[vertex])  # Set color for each vertex
           glTexCoord2fv(texture_coords[face_index][vertex_index])
           glVertex3fv(vertices[vertex])
        glEnd()
    

    
def Icosahedron():
    
    a = 0.8507 #derived from pythagorean theorem; solved for quadratic equation
    b = a / ((1 + math.sqrt(5)) / 2) # The divisor is the golden ratio
    vertices = [
        (a, b, 0),
        (-a, b, 0),
        (a, -b, 0),
        (-a, -b, 0),
        (0, a, b),
        (0, -a, b),
        (0, a, -b),
        (0, -a, -b),
        (b, 0, a),
        (-b, 0, a),
        (b, 0, -a),
        (-b, 0, -a)
        ]

    edges = [
        (0,2), (0,4), (0,6), (0,8), (0,10), 
        (1,3), (1,4), (1,6), (1,9), (1, 11),
        (2,5), (2,7), (2,8), (2,10),
        (3,5), (3,7), (3,9), (3,11),
        (4,6), (4,8), (4,9),
        (5,7), (5,8), (5,9),
        (6,10), (6,11),
        (7,10), (7,11),
        (8,9),
        (10, 11)
        ]
    
    texture_coords = [
        # 1
        ((0, 0 + Dt), (1/10, 0 + Dt), (1/20, 1/2 + Dt)), 
        # 2                 
        ((0 + Dx, 0 + Dt),(1/10 + Dx, 0 + Dt), (1/20 + Dx, 1/2 + Dt)),   
        # 3
        ((1/20 + 2 * Dx, 1/2 + Dt), (1/10 + 2 * Dx, 0 + Dt), (0 + 2 * Dx, 0 + Dt)), 
        # 4
        ((1/10 + 3 * Dx, 0 + Dt), (1/20 + 3 * Dx, 1/2 + Dt), (0 + 3 * Dx, 0 + Dt)),
        # 5
        ((1/10 + 4 * Dx, 0 + Dt), (1/20 + 4 * Dx, 1/2 + Dt), (0 + 4 * Dx, 0 + Dt)),
        # 6
        ((1/20 + 5 * Dx, 1/2 + Dt), (1/10 + 5 * Dx, 0 + Dt), (0 + 5 * Dx, 0 + Dt)),
        # 7
        ((1/20 + 6 * Dx, 1/2 + Dt), (1/10 + 6 * Dx, 0 + Dt), (0 + 6 * Dx, 0 + Dt)),
        # 8
        ((1/10 + 7 * Dx, 0 + Dt), (1/20 + 7 * Dx, 1/2 + Dt), (0 + 7 * Dx, 0 + Dt)),
        # 9
        ((1/20 + 8 * Dx, 1/2 + Dt), (1/10 + 8 * Dx, 0 + Dt), (0 + 8 * Dx, 0 + Dt)),
        #10
        ((1/20 + 9 * Dx, 1/2 + Dt), (1/10 + 9 * Dx, 0 + Dt),  (0 + 9 * Dx, 0 + Dt)),
        
        # 11
        ((1/20, 1/2 + Dy + Dt), (1/10, 0 + Dy + Dt), (0, 0 + Dy + Dt)),       
        # 12              
        ((1/10 + Dx, 0 + Dy + Dt), (1/20 + Dx, 1/2+ Dy + Dt), (0 + Dx, 0 + Dy + Dt)),      
        # 13
        ((1/20 + 2 * Dx, 1/2 + Dy + Dt), (1/10 + 2 * Dx, 0 + Dy + Dt), (0 + 2 * Dx, 0 + Dy + Dt)), 
        # 14
        ((1/20 + 3 * Dx, 1/2 + Dy + Dt), (1/10 + 3 * Dx, 0 + Dy + Dt), (0 + 3 * Dx, 0 + Dy + Dt)),
        # 15
        ((1/20 + 4 * Dx, 1/2 + Dy + Dt), (1/10 + 4 * Dx, 0 + Dy + Dt), (0 + 4 * Dx, 0 + Dy + Dt)),
        # 16
        ((1/10 + 5 * Dx, 0 + Dy + Dt), (1/20 + 5 * Dx, 1/2 + Dy + Dt), (0 + 5 * Dx, 0 + Dy + Dt)),
        # 17
        ((1/20 + 6 * Dx, 1/2 + Dy + Dt), (1/10 + 6 * Dx, 0 + Dy + Dt),  (0 + 6 * Dx, 0 + Dy + Dt)),
        # 18 
        ((1/10 + 7 * Dx, 0 + Dy + Dt), (1/20 + 7 * Dx, 1/2 + Dy + Dt), (0 + 7 * Dx,  0+ Dy + Dt)),
        # 19
        ((1/10 + 8 * Dx, 0 + Dy + Dt), (1/20 + 8 * Dx, 1/2 + Dy + Dt), (0 + 8 * Dx, 0 + Dy + Dt)),
        # 20
        ((1/10 + 9 * Dx, 0 + Dy + Dt), (1/20 + 9 * Dx, 1/2 + Dy + Dt), (0 + 9 * Dx, 0 + Dy + Dt))
        ]
    
    vertex_colors = [
        (1, 0, 0), 
        (0, 1, 0),  
        (0, 0, 1),  
        (1, 1, 0),   
        (1, 0, 1),  
        (0, 1, 1),  
        (0, 0.5, 1),  
        (1, 0.5, 0),  
        (1, 0, 0), 
        (0, 1, 0),  
        (0, 0, 1),  
        (1, 1, 0)  
    ]
    
    faces = (
        (9,3,5),
        (9,5,8),
        (5,8,2),
        (8,2,0),
        (8,0,4),
        (4,8,9),
        (4,9,1),
        (1,9,3),
        (0,4,6),
        (6,4,1),
        (6,1,11),
        (1,11,3),
        (11,3,7),
        (3,5,7),
        (7,5,2), 
        (7,10,2),
        (2,0,10),
        (0,10,6),
        (10,7,11),
        (10,11,6)
        )
    
    glColor(1,1,1) # Draw the Icosahedron outline in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()    
    
    for face_index, face in enumerate(faces):
        glBegin(GL_TRIANGLES)
        for vertex_index, vertex in enumerate(face):
           glColor3fv(vertex_colors[vertex])  # Set color for each vertex
           glTexCoord2fv(texture_coords[face_index][vertex_index])
           glVertex3fv(vertices[vertex])
        glEnd()
    
def Axes():
    glBegin(GL_LINES)
    glColor(1,0,0) # Red for the x-axis
    glVertex3fv((0,0,0))
    glVertex3fv((1.5,0,0))
    glColor(0,1,0) # Green for the y-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,1.5,0))
    glColor(0,0,1) # Blue for the z-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,0,1.5))
    glEnd()


def Circle():
    glPushMatrix()
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -2, 2)
    glColor(1,0,1) # Purple for the limits
    glBegin(GL_LINE_LOOP)
    for i in range(36):
        angle = 2.0 * math.pi * i / 36
        x = math.cos(angle)
        y = math.sin(angle)
        glVertex3fv((x, y, 0))
    glEnd()
    glPopMatrix()

def loadTexture():
    textureSurface = pygame.image.load('Numbers.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid    

def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Dice-Rolling Simulation')
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])
    glLight(GL_LIGHT0, GL_POSITION,  (0, -5.0, 0, 1))  # point light from below

    # Rotation angle
    rotationAngle = 0
    rotationAngle2 = 0
    isRotating = True
    
    name = 0
    texture = loadTexture()
    controlRotate = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    rotationAngle = 0 # resets dice position
                    rotationAngle2 = 0 # resets dice position
                    controlRotate = 0 # stops dice from rotating
                if event.key == pygame.K_r:
                    controlRotate = 1 # restarts ambient rotate
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Axes() # Draw the axes
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            name = 1 #Draw the Cube
        elif keys[pygame.K_2]:           
            name = 2 #Draw the Tetrahedron
        elif keys[pygame.K_3]:
            name = 3 #Draw the Octahedron
        elif keys[pygame.K_4]:
            name = 4 #Draw the Dodecahedron
        elif keys[pygame.K_5]:
            name = 5 #Draw the Icosahedron
            
        if  name == 1:
            Tetrahedron()
        elif name == 2:
            Cube(1, 1, 1, texture)
        elif name == 3:
            Octahedron()
        elif name == 4:
            Dodecahedron()
        elif name == 5:
            Icosahedron()
        Circle() # Draw the limit circle
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if rotationAngle > -360:
                rotationAngle -= 1
                glRotate(1,1,0,0)
        elif keys[pygame.K_DOWN]:
            if rotationAngle < 360:
                rotationAngle += 1
                glRotate(-1,1,0,0)
        elif keys[pygame.K_LEFT]:
            if rotationAngle2> -360:
                rotationAngle2-= 1
                rotationAngle2 = 1
                glRotate(1,0,1,0)
        elif keys[pygame.K_RIGHT]:
            if rotationAngle2< 360:
                rotationAngle2+= 1
                glRotate(-1,0,1,0)
        else:
            glRotate(controlRotate,controlRotate,controlRotate,controlRotate) # As a default the dice is rotating ambiently
        
        glRotatef(rotationAngle, 1, 0, 0)
        glRotatef(rotationAngle2, 0, 1, 0)



    
        pygame.display.flip()
        pygame.time.wait(10)
        

main()