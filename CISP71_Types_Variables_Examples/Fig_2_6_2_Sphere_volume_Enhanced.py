#Given sphere_radius and pi, compute the volume of a sphere and 
#assign sphere_volume with the volume. Volume of sphere = (4.0 / 3.0) π r3

pi = 3.14159
sphere_volume = 0.0

sphere_radius = float(input('Enter sphere radius:'))

sphere_volume = pi * (sphere_radius * sphere_radius * sphere_radius) * (4 / 3)

print('Sphere volume: {:.2f}'.format(sphere_volume))

