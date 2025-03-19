from manim import *

config.tex_template = TexTemplate()
config.tex_template.add_to_preamble(r"\usepackage{mathrsfs}")

class GradientDescent(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 7, 1], 
            y_range=[0, 10, 2],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE}
        )

        axes.center()

        function = lambda x: (x - 1)**2
        graph = axes.plot(function, color=GREEN)
        
        y_label = MathTex(r"\mathscr{L}(h(x), y)")
        x_label = MathTex("w")
        
        x_label.next_to(axes.x_axis.get_end(), RIGHT)
        y_label.next_to(axes.y_axis.get_end(), UP)
        
        x_start = 5.5
        learning_rate = 0.2  
        steps = 10  
        
        dot = Dot(axes.c2p(x_start, function(x_start)), color=RED)
        self.add(axes, graph, x_label, y_label, dot)
        
        w_label = MathTex("w = ")
        w_value = MathTex(f"{x_start:.2f}")
        
        loss_label = MathTex(r"\mathscr{L}(h(x), y) = ")
        loss_value = MathTex(f"{function(x_start):.2f}")
        
        w_group = VGroup(w_label, w_value).arrange(RIGHT, buff=0.1)
        w_group.move_to(axes.c2p(-4, 8))
        
        loss_group = VGroup(loss_label, loss_value).arrange(RIGHT, buff=0.1)
        loss_group.next_to(w_group, DOWN, aligned_edge=LEFT)
        
        self.add(w_label, w_value, loss_label, loss_value)
        
        for _ in range(steps):
            y_value = function(x_start)
            slope = 2 * (x_start - 1) 
            x_next = x_start - learning_rate * slope 
            y_next = function(x_next)
            
            start_point = axes.c2p(x_start, y_value)
            end_point = axes.c2p(x_next, y_next)
            
            line = Line(
                start_point,
                end_point,
                color=ORANGE,
                stroke_width=5
            )
            
            tip = ArrowTriangleFilledTip(
                length=0.2,
                width=0.2,
                fill_color=ORANGE
            )
            
            line.add_tip(tip)

            self.play(Create(line), run_time=0.7)
            self.wait(0.7)
            
            
            new_w_value = MathTex(f"{x_next:.2f}")
            new_loss_value = MathTex(f"{y_next:.2f}")
            
            new_w_value.move_to(w_value)
            new_loss_value.move_to(loss_value)
        
            self.play(
                dot.animate.move_to(axes.c2p(x_next, y_next)),
                Transform(w_value, new_w_value),
                Transform(loss_value, new_loss_value),
                run_time=1.0
            )
            
            self.play(FadeOut(line), run_time=0.3)
            self.remove(line)
            self.wait(1)

            x_start = x_next
            
        self.wait(2)