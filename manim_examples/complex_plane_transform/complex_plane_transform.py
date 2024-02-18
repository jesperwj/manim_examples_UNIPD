from manim import *

# manim -pqh complex_plane_transform.py ComplexPlaneTransform

class ComplexPlaneTransform(Scene):
    def construct(self):
        # Complex map
        c_grid = ComplexPlane()
        moving_c_grid = c_grid.copy()
        moving_c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, 1)
        c_grid.add_coordinates(font_size=24)
        complex_map_words = MathTex(r"""
            \text{The plane is the complex plane }\mathbb{C},\\
            \text{and this is the map } z \rightarrow z^2
        """)
        complex_map_words.to_corner(UR)
        complex_map_words.set_stroke(BLACK, 5, background=True)

        self.play(
            Write(c_grid, run_time=3),
            FadeIn(moving_c_grid),
            Write(complex_map_words),
        )
        self.wait()
        self.play(
            moving_c_grid.animate.apply_complex_function(lambda z: z**2),
            run_time=6,
        )
        self.wait(2)
