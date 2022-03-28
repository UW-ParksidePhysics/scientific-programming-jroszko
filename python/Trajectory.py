from math import pi, tan, cos

standard_gravity = 9.80665  # m/s/s
initial_velocity = 15.      # km/h
launch_angle = 60           # °
horizontal_range = 0.5      # m
initial_height = 1.0        # m

print(f'v0    = {initial_velocity:.1f} km/h')
print(f'theta = {launch_angle:.0f} °')
print(f'x     = {horizontal_range:.1f} m')
print(f'y0    = {initial_height:.1f} m')


# Convert initial velocity to m/s
initial_velocity = initial_velocity * 3600 / 1000
# Convert angle to radians
launch_angle = launch_angle * pi / 180


def calculate_height(horizontal_displacement, angle, starting_velocity, starting_height):
    height = horizontal_displacement * tan(angle) \
             - 1 / (2 * initial_velocity ** 2) * standard_gravity * horizontal_displacement ** 2 / ((cos(launch_angle)) ** 2) \
             + initial_height
    return height


projectile_height = calculate_height(horizontal_range, launch_angle, initial_velocity, initial_height)
print(f'y     = {projectile_height:.1f} m')