from manim import *
import numpy as np

class SomaArcos(MovingCameraScene):
    def construct(self):

        self.play(self.camera.frame.animate.scale(1.3))

        plano = NumberPlane(
            background_line_style={'stroke_opacity': 0.4}
        )
        self.add(plano)
        
        A = np.array([-2, 3, 0])
        B = np.array([-2, -3, 0])
        C = np.array([2, 3, 0])
        D = np.array([2, -3, 0])

        E = np.array([3.6, -3, 0])

        G = np.array([-2, -3.1, 0])
        H = np.array([2, -3.1, 0])

        I = np.array([4, 3, 0])
        J = np.array([4, -3, 0])

        linha_BD = Line(B, D)
        linha_CD = Line(C, D)

        retangulo_principal = Polygon(A, C, D, B, color=WHITE)

        self.play(Create(retangulo_principal))

        self.wait(2)

        linha_diagonal = Line(B, C, color=BLUE)
        label_linha_diagonal = MathTex(r'1').shift(0.5*LEFT)

        self.play(Create(linha_diagonal), FadeIn(label_linha_diagonal))

        self.wait(2)

        F = np.array([3.6, 1, 0])

        linha_T2 = Line(B, F, color=BLUE)

        self.play(Create(linha_T2))

        BC_vetor = C-B
        BF_vetor = F-B

        vetor_projecao = np.dot(BC_vetor, BF_vetor) / np.dot(BF_vetor, BF_vetor)

        ponto_perpendicular = B + vetor_projecao*BF_vetor

        linha_perpendicular = Line(C, ponto_perpendicular, color=BLUE)

        base_t3 = Line(B, E, color=GREEN)

        linha_t3_perpendicular = Line(ponto_perpendicular, E, color=GREEN)

        self.play(Create(linha_perpendicular))

        tri_1 = Polygon(B, C, ponto_perpendicular, color=BLUE, fill_color = BLUE, fill_opacity = 0.3)
        
        self.play(Create(base_t3), Create(linha_t3_perpendicular), FadeIn(tri_1))

        tri_2 = Polygon(ponto_perpendicular, E, B, color=GREEN, fill_color = GREEN, fill_opacity = 0.3)

        self.wait(2)

        angulo_alfa = Angle(linha_T2, linha_diagonal, radius=0.6, other_angle=False, color=BLUE_E)

        alfa_label = MathTex(r'\alpha').scale(0.5).shift(1.3*LEFT + 2.3*DOWN)

        angulo_reto1 = RightAngle(linha_perpendicular, linha_T2, length=0.4,quadrant=(-1, -1), color=YELLOW)

        self.play(Create(angulo_alfa), Create(angulo_reto1), FadeIn(alfa_label), FadeIn(tri_2))

        angulo_beta = Angle(linha_BD, linha_T2, radius=0.6, other_angle=False, color=ORANGE)

        beta_label = MathTex(r'\beta').scale(0.5).shift(1.2*LEFT + 2.7*DOWN)

        angulo_reto2 = RightAngle(linha_t3_perpendicular, base_t3, length=0.4,quadrant=(-1, -1), color=YELLOW)

        self.play(Create(angulo_beta), Create(angulo_reto2), FadeIn(beta_label))

        self.wait(2)

        tri_3 = Polygon(B, C, D, color = WHITE, fill_color = WHITE, fill_opacity = 0.3)

        grupo_tri_3 = VGroup()
        angulo_alfa2 = angulo_alfa.copy()
        angulo_beta2 = angulo_beta.copy()
        beta_label2 = beta_label.copy()
        alfa_label2 = alfa_label.copy()
        label_linha_diagonal2 = label_linha_diagonal.copy()
        angulo_reto3 = RightAngle(linha_CD, linha_BD, length=0.4, quadrant=(-1, -1), color=YELLOW)
        grupo_tri_3.add(angulo_alfa2, angulo_beta2, beta_label2, alfa_label2, angulo_reto3, tri_3, label_linha_diagonal2)

        self.play(FadeIn(grupo_tri_3))

        self.wait(2)

        self.play(self.camera.frame.animate.shift(5.3*RIGHT))

        self.play(grupo_tri_3.animate.shift(7*RIGHT))

        label_x = MathTex(r'x').shift(9.3*RIGHT)
        label_y = MathTex(r'y').shift(3.3*DOWN + 7*RIGHT)

        self.play(FadeIn(label_x), FadeIn(label_y))

        sen_alfa_beta = MathTex(r"\sin(\alpha+\beta)=\frac{x}{1}").shift(12*RIGHT + 2*UP)

        self.play(FadeIn(sen_alfa_beta))

        self.wait()

        sen_alfa_beta2 = MathTex(r"\sin(\alpha+\beta) = x ").shift(12*RIGHT + 2*UP)
        
        self.play(Transform(sen_alfa_beta, sen_alfa_beta2))

        self.wait()

        linha_sen_alfa_beta = Line(G, H, color=WHITE)

        linha_tracejada1 = DashedLine(
            start=C,
            end=I
        )

        linha_tracejada2 = DashedLine(
            start=D,
            end=J
        )

        self.play(Create(linha_tracejada1), Create(linha_tracejada2))

        linha_cos_alfa_beta = Line(I, J)

        label_cos_alfa_beta3 = MathTex(r"\sin(\alpha+\beta)").shift(4.3*RIGHT).rotate(90*DEGREES)

        self.play(Create(linha_cos_alfa_beta))

        self.play(FadeIn(label_cos_alfa_beta3))

        self.wait()

        cos_alfa_beta = MathTex(r"\cos(\alpha+\beta)=\frac{y}{1}").shift(12*RIGHT)

        self.play(FadeIn(cos_alfa_beta))

        cos_alfa_beta2 = MathTex(r"\cos(\alpha+\beta) = y").shift(12*RIGHT)

        self.play(Transform(cos_alfa_beta, cos_alfa_beta2))

        self.wait()

        sen_alfa_beta3 = MathTex(r"\cos(\alpha+\beta)").shift(3.4*DOWN)

        self.play(Create(linha_sen_alfa_beta), FadeIn(sen_alfa_beta3))


        self.wait()

        self.play(FadeOut(grupo_tri_3), FadeOut(label_x), FadeOut(label_y), FadeOut(cos_alfa_beta), FadeOut(sen_alfa_beta))