from manim import *

# manim -pqh matrix_operation_2D_plane.py MatrixOperation2DPlane

class MatrixOperation2DPlane(Scene):
    def construct(self):
        self.wait(2)

        # Linear transform
        grid = NumberPlane((-10, 10), (-5, 5))
        matrix = [[1, 1], [0, 1]]
        linear_transform_words = VGroup(
            Text("This is what the matrix"),
            IntegerMatrix(matrix, include_background_rectangle=True),
            Text("looks like")
        )
        linear_transform_words.arrange(RIGHT)
        linear_transform_words.to_edge(UP)
        linear_transform_words.set_stroke(BLACK, 10, background=True)

        self.play(
            Create(grid),
            Write(linear_transform_words)
        )
        self.wait()
        self.play(grid.animate.apply_matrix(matrix), run_time=3)
        self.wait(2)
