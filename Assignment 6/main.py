# One and Seven digit pipeline
one_seven_generator = Augmentor.Pipeline()
one_seven_generator.rotate(
    probability=p, max_left_rotation=7.5, max_right_rotation=7.5
)  # Rotating
one_seven_generator.shear(
    probability=p, max_shear_left=7.5, max_shear_right=7.5
)  # Sheering
one_seven_generator.random_distortion(
    probability=p, grid_width=3, grid_height=3, magnitude=7
)  # Elastic distortion

# Other digits pipeline
other_generator = Augmentor.Pipeline()
other_generator.rotate(
    probability=p, max_left_rotation=15.0, max_right_rotation=15.0
)  # Rotating
other_generator.shear(
    probability=p, max_shear_left=15.0, max_shear_right=15.0
)  # Sheering
one_seven_generator.random_distortion(
    probability=p, grid_width=3, grid_height=3, magnitude=7
)  # Elastic distortion

