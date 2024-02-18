from manim import *
import numpy as np

# manim -pqh sin_and_cos_function_plot.py SinAndCosFunctionPlot

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )

        cos_label = axes.get_graph_label(
            cos_graph, "\\cos(x)", x_val=-10, direction=UP / 2
        )

        plot = VGroup(axes)

        labels = VGroup(axes_labels, sin_label, cos_label)
        labels = VGroup(axes_labels)

        self.add(plot, labels)

        # Animation code
        self.wait(2)
        self.play(Write(sin_label))
        self.wait(0.5)
        self.play(Create(sin_graph), run_time=3)
        self.wait(1)
        self.play(Write(cos_label))
        self.wait(0.5)
        self.play(Create(cos_graph), run_time=3)
        self.wait(2)
