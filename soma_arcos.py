from manim import *
import numpy as np

class SomaArcos(MovingCameraScene):
    def construct(self):

        self.play(self.camera.frame.animate.scale(1.3))

        # plano = NumberPlane(
        #     background_line_style={'stroke_opacity': 0.4}
        # )
        # self.add(plano)
        
        A = np.array([-2, 3, 0])
        B = np.array([-2, -3, 0])
        C = np.array([2, 3, 0])
        D = np.array([2, -3, 0])

        E = np.array([3.5, -3, 0])

        G = np.array([-2, -3.1, 0])
        H = np.array([2, -3.1, 0])

        I = np.array([4, 3, 0])
        J = np.array([4, -3, 0])

        K = np.array([3.5, 3, 0])

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

        self.wait(2)

        grupo_tri_1 = VGroup()
        tri_1_2 = tri_1.copy()
        alfa_label3 = alfa_label.copy()
        angulo_reto1_2 = angulo_reto1.copy()
        label_linha_diagonal3 = label_linha_diagonal.copy()
        angulo_alfa3 = angulo_alfa.copy()
        grupo_tri_1.add(tri_1_2, alfa_label3, angulo_reto1_2, label_linha_diagonal3, angulo_alfa3)

        self.play(grupo_tri_1.animate.shift(7*RIGHT))

        self.wait(2)

        label_m = MathTex(r'm', color=BLUE).shift(2*UP + 10.3*RIGHT)
        label_n = MathTex(r'n', color=BLUE).shift(1*DOWN + 8.5*RIGHT)

        self.play(FadeIn(label_m), FadeIn(label_n))

        self.wait()

        seno_alfa = MathTex(r"\sin(\alpha)=\frac{m}{1}", color=BLUE).shift(12.5*RIGHT + 2*UP)

        self.play(FadeIn(seno_alfa))

        self.wait(2)

        seno_alfa2 = MathTex(r"\sin(\alpha) = m", color=BLUE).shift(12.5*RIGHT + 2*UP)

        self.play(Transform(seno_alfa, seno_alfa2))

        self.wait(2)

        seno_alfa3 = MathTex(r"\sin(\alpha)", color=BLUE).rotate(125*DEGREES).shift(2.5*RIGHT + 1.8*UP).scale(0.7)

        self.play(FadeIn(seno_alfa3))

        self.wait()

        cos_alfa = MathTex(r"\cos(\alpha)=\frac{n}{1}", color=BLUE).shift(12.5*RIGHT)

        self.play(FadeIn(cos_alfa))

        self.wait(2)

        cos_alfa2 = MathTex(r"\cos(\alpha) = n", color=BLUE).shift(12.5*RIGHT)

        self.play(Transform(cos_alfa, cos_alfa2))

        self.wait()

        cos_alfa3 = MathTex(r"\cos(\alpha)", color=BLUE).rotate(35*DEGREES).shift(1*RIGHT + 0.5*DOWN).scale(0.7)

        self.play(FadeIn(cos_alfa3))

        self.wait()

        self.play(FadeOut(grupo_tri_1, seno_alfa, cos_alfa, label_m, label_n))

        self.wait()

        grupo_tri_2 = VGroup()

        tri_2_2 = tri_2.copy()
        beta_label_3 = beta_label.copy()
        angulo_beta3 = angulo_beta.copy()
        angulo_reto2_2 = angulo_reto2.copy()
        cos_alfa4 = cos_alfa3.copy()
        grupo_tri_2.add(tri_2_2, beta_label_3, angulo_beta3, angulo_reto2_2, cos_alfa4)

        self.play(grupo_tri_2.animate.shift(7*RIGHT))

        self.wait()

        label_r = MathTex(r'r', color=GREEN).shift(1*DOWN + 11*RIGHT)
        label_s = MathTex(r's', color=GREEN).shift(3.3*DOWN + 8*RIGHT)

        self.play(FadeIn(label_r), FadeIn(label_s))

        self.wait()

        sen_beta = MathTex(r"\sin(\beta)=\frac{r}{\cos(\alpha)}", color=GREEN).shift(2*UP + 7*RIGHT)

        self.play(FadeIn(sen_beta))

        self.wait()

        sen_beta2 = MathTex(r"r = \cos(\alpha)\cdot\sin(\beta)", color=GREEN).shift(2*UP + 7*RIGHT)

        self.play(Transform(sen_beta, sen_beta2))

        self.wait()

        sen_beta3 = MathTex(r"\cos(\alpha)\cdot\sin(\beta)", color=GREEN).rotate(90*DEGREES).scale(0.7).shift(1.2*DOWN + 3.2*RIGHT)

        self.play(FadeIn(sen_beta3))

        self.wait()

        cos_beta = MathTex(r"\cos(\beta)=\frac{s}{\cos(\alpha)}", color=GREEN).shift(2*UP + 11.5*RIGHT)

        self.play(FadeIn(cos_beta))

        self.wait()

        cos_beta2 = MathTex(r"s = \cos(\alpha)\cdot\cos(\beta)", color=GREEN).shift(2*UP + 11.5*RIGHT)

        self.play(Transform(cos_beta, cos_beta2))

        self.wait()

        cos_beta3 = MathTex(r"\cos(\alpha)\cdot\cos(\beta)", color=GREEN).scale(0.7).shift(2.8*DOWN + 1*RIGHT)

        self.play(FadeIn(cos_beta3))

        self.wait()

        self.play(FadeOut(grupo_tri_2, label_r, label_s, sen_beta, cos_beta))

        self.wait()

        tri_4 = Polygon(C, ponto_perpendicular, K, color=PINK, fill_color = PINK, fill_opacity = 0.3)

        self.play(Create(tri_4))

        linha_tri_rosa = Line(ponto_perpendicular, K, color=PINK)

        linha_perpendicular2 = Line(ponto_perpendicular, C)

        angulo_beta_rosa = Angle(
            linha_tri_rosa,
            linha_perpendicular2,
            radius=0.6,
            color=PINK
        )

        beta_rosa_label = MathTex(r"\beta").scale(0.5).shift(1.7*UP, 3.3*RIGHT)

        linha_tri_rosa2 = Line(C, K, color=PINK)

        angulo_reto4 = RightAngle(linha_tri_rosa2, linha_tri_rosa,length=0.4, quadrant=(-1, -1), color = YELLOW)

        self.play(FadeIn(angulo_beta_rosa, beta_rosa_label, angulo_reto4))

        self.wait(2)

        grupo_tri_4 = VGroup()

        tri_4_2 = tri_4.copy()
        angulo_beta_rosa2 = angulo_beta_rosa.copy()
        beta_rosa_label2 = beta_rosa_label.copy()
        angulo_reto4_2 = angulo_reto4.copy()
        seno_alfa3_2 = seno_alfa3.copy()

        grupo_tri_4.add(tri_4_2, angulo_beta_rosa2, beta_rosa_label2, angulo_reto4_2, seno_alfa3_2)

        self.play(grupo_tri_4.animate.shift(5.5*RIGHT))

        self.wait()

        label_u = MathTex(r"u", color=PINK).shift(3.3*UP + 8.2*RIGHT)
        label_v = MathTex(r"v", color=PINK).shift(2*UP + 9.3*RIGHT)

        self.play(FadeIn(label_u, label_v))

        self.wait()

        seno_beta_rosa = MathTex(r"\sin(\beta)=\frac{u}{\sin(\alpha)}", color = PINK).shift(9*RIGHT)

        self.play(FadeIn(seno_beta_rosa))

        self.wait()

        seno_beta_rosa2 = MathTex(r"u = \sin(\beta)\cdot\sin(\alpha)", color=PINK).shift(9*RIGHT)

        self.play(Transform(seno_beta_rosa, seno_beta_rosa2))

        self.wait()

        seno_beta_rosa3 = MathTex(r"\sin(\beta)\cdot\sin(\alpha)", color=PINK).scale(0.7).shift(3.3*UP + 2.8*RIGHT)

        self.play(FadeIn(seno_beta_rosa3))

        self.wait()

        cos_beta_rosa = MathTex(r"\cos(\beta)=\frac{v}{\sin(\alpha)}", color=PINK).shift(9*RIGHT + 2*DOWN)

        self.play(FadeIn(cos_beta_rosa))

        self.wait()

        cos_beta_rosa2 = MathTex(r"v = \sin(\alpha)\cdot\cos(\beta)", color=PINK).shift(9*RIGHT + 2*DOWN)

        self.play(Transform(cos_beta_rosa, cos_beta_rosa2))

        self.wait()

        cos_beta_rosa3 = MathTex(r"\sin(\alpha)\cdot\cos(\beta)", color=PINK).shift(3.8*RIGHT + 2*UP).scale(0.7).rotate(90*DEGREES)

        self.play(FadeIn(cos_beta_rosa3))

        self.wait()

        self.play(FadeOut(grupo_tri_4, seno_beta_rosa, cos_beta_rosa, label_u, label_v))

        self.wait()

        sen_alfa_beta3_2 = label_cos_alfa_beta3.copy()
        self.play(sen_alfa_beta3_2.animate.rotate(-90*DEGREES))
        self.play(sen_alfa_beta3_2.animate.shift(1*UP + 3*RIGHT))
        igual1 = MathTex(r"=").shift(1*UP + 8.8*RIGHT)
        self.play(FadeIn(igual1))

        cos_beta_rosa3_2 = cos_beta_rosa3.copy()
        sen_beta3_2 = sen_beta3.copy()

        self.play(FadeIn(cos_beta_rosa3_2, sen_beta3_2))

        self.play(cos_beta_rosa3.animate.rotate(-90*DEGREES), sen_beta3.animate.rotate(-90*DEGREES))
        self.play(cos_beta_rosa3.animate.shift(2*DOWN + 2.5*RIGHT), sen_beta3.animate.shift(1.225*UP + 6*RIGHT))

        mais1 = MathTex(r"+").shift(7.7*RIGHT)
        self.play(FadeIn(mais1))

        cos_alfa_beta3_2 = sen_alfa_beta3.copy()

        self.play(cos_alfa_beta3_2.animate.shift(7.3*RIGHT + 2*UP))

        igual2 = igual1.copy()
        igual2.shift(2.4*DOWN)
        self.play(FadeIn(igual2))

        cos_beta3_2 = cos_beta3.copy()
        seno_beta_rosa3_2 = seno_beta_rosa3.copy()

        self.play(cos_beta3_2.animate.shift(0.25*UP + 5*RIGHT), seno_beta_rosa3_2.animate.shift(5.85*DOWN + 6*RIGHT))

        menos = MathTex(r"-").shift(7.35*RIGHT + 2.55*DOWN)

        self.play(FadeIn(menos))