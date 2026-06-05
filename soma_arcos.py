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

        linha_BD = Line(B, D)

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
        
        self.play(Create(base_t3), Create(linha_t3_perpendicular))

        self.wait(2)

        angulo_alfa = Angle(linha_T2, linha_diagonal, radius=0.6, other_angle=False, color=BLUE_E)

        angulo_reto1 = RightAngle(linha_perpendicular, linha_T2, length=0.4,quadrant=(-1, -1), color=YELLOW)

        self.play(Create(angulo_alfa), Create(angulo_reto1))

        angulo_beta = Angle(linha_BD, linha_T2, radius=0.6, other_angle=False, color=ORANGE)

        angulo_reto2 = RightAngle(linha_t3_perpendicular, base_t3, length=0.4,quadrant=(-1, -1), color=YELLOW)

        self.play(Create(angulo_beta), Create(angulo_reto2))

        self.wait(2)

        print(ponto_perpendicular)