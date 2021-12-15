from manim import *

class Cone(ThreeDScene):
    def construct(self):

        # Setup inicial

        axes = ThreeDAxes(
            x_range = [-6, 18, 2], x_length = 7.8,
            y_range = [-14, 14, 2], y_length = 7.8,
            z_range = [-14, 14, 2], z_length = 7.8
        ).rotate(angle = -PI, axis= np.array([1, 0, 1]), about_point= ORIGIN)

        self.renderer.camera.light_source.move_to(3*IN)
        
        
        cone1 = ParametricSurface(
            lambda u, v: axes.c2p(
                v,
                (6.85 - 0.433 * v) * np.cos(u),
                (6.85 - 0.433 * v) * np.sin(u)
                # v, 2.308 * v * np.cos(u), 2.308 * v * np.sin(u)
            ),
            u_range= [0, 2 * PI],
            v_range= [0, 15.81],
            fill_opacity= 0.9
        ).set_color(PURPLE_B)

        cone2 = ParametricSurface(
            lambda u, v: axes.c2p(
                v,
                (6.85 - 0.433 * v) * np.cos(u),
                (6.85 - 0.433 * v) * np.sin(u)
                # v, 2.308 * v * np.cos(u), 2.308 * v * np.sin(u)
            ),
            u_range= [0, 2 * PI],
            v_range= [7.5, 15.81],
            fill_opacity= 0.9
        ).set_color(PURPLE_B)
        
        
        truncatedSurface = ParametricSurface(
            lambda u, v: axes.c2p(
                v,
                (6.85 - 0.433 * v) * np.cos(u),
                (6.85 - 0.433 * v) * np.sin(u)
                # v, 2.308 * v * np.cos(u), 2.308 * v * np.sin(u)
            ),
            u_range= [0, 2 * PI],
            v_range= [0, 7.5],
            fill_opacity= 0.9
        ).set_color(PURPLE_B)

        a = 3.6
        circle1 = Circle(3.6 / a, color= PURPLE_B, fill_opacity= 0.8).move_to((0, 0, 0.45))
        circle2 = Circle(6.85 / a, color= PURPLE_B, fill_opacity= 0.3).move_to((0, 0, -1.95))

        truncatedCone = VGroup(truncatedSurface, circle1, circle2)

        # Parte 1 - Apresentação

        self.set_camera_orientation(phi= PI / 2, theta= PI)


        # Objetos


        function = axes.get_graph(lambda x: 6.85 - 0.433 * x, x_range=[0, 15.81], color= PURPLE_B)
        area = axes.get_area(graph= function, x_range= [0, 15.81], color= [PURPLE_B, PURPLE_B])
        
        line1 = Line((3, 0, self.sectionHeight), (0, -3, self.sectionHeight), color= PINK).move_to((1.5, -1.5, 0.45))
        path = Line((1.5, -1.5, 0.45), (-1.5, 1.5, 0.45))


        self.play(DrawBorderThenFill(axes))
        self.wait(1)
        self.play(DrawBorderThenFill(area))
        self.wait()
        
        self.move_camera(phi=PI * 2 / 5, theta= PI * 4.2 / 4)
        self.play(DrawBorderThenFill(cone1), FadeOut(area))
        self.wait()
        self.play(FadeOut(cone1), FadeIn(cone2, truncatedCone))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        self.move_camera(phi= PI / 3, theta= PI * 5 / 4)
        self.wait()
        self.play(Create(line))
        self.wait()
        self.play(MoveAlongPath(line, path), FadeOut(cone2))
        self.wait()



        # Parte 2 - Medidas

        # Preparando o momento inicial
        self.set_camera_orientation(phi = PI * 2 / 5, theta= PI * 5 / 4)
        self.add(axes, truncatedCone)


        # Objects

        trapezium1 = Polygon((0, 3.6 / a, 0.45), (0, 6.85 / a, -1.95), (0, - 6.85 / a, -1.95), (0, - 3.6 / a, 0.45), color= PURPLE, fill_opacity= 0.75)
        trapezium2 = Polygon((0, 0, -1.95), (0, 0, 0.45), (0, - 3.6 / a, 0.45), (0, - 6.85 / a, -1.95), color= YELLOW)
        triangle = Polygon((0, -3.6 / a - 0.001, 0.45), (0, -3.6 / a + 0.001, 0.45), (0, -3.6 / a, -1.96), (0, -6.85 / a, -1.95))

        height1 = Line((0, - 6.85 / a - 0.3, -1.95), (0, - 6.85 / a - 0.3, 0.45), color= YELLOW).rotate_about_origin(PI / 2, axis= np.array([0, 1, 0]))

        b1 = Brace(height1)
        b1text = b1.get_text("7,5 cm").move_to(b1.get_center() + (0, -0.95, 0))#.rotate(angle= -PI / 2, axis= np.array([0, 0, 1])).rotate(angle= PI, axis= np.array([0, 1, 0]))

        h1Group = VGroup(height1, b1, b1text).rotate(angle= PI / 2, axis= np.array([0, 1, 0])).move_to((0, - 6.85 / a - 0.85, -0.75))
        b1text.rotate(angle= PI, axis= np.array([0, 0, 1])).rotate(angle= - PI / 2, axis= np.array([1, 0, 0]))

        radius1 = BraceBetweenPoints((0, 0, 0.45), (0, 3.6 / a, 0.45)).rotate(angle= - PI / 2, axis= np.array([0, 1, 0])).move_to((0, 3.6 / (2 * a), 0.6))
        b2 = radius1.get_text("3,6 cm").move_to(radius1.get_center() + (0, 0, 0.4)).rotate(-PI / 2, np.array([0, 1, 0])).rotate(PI / 2, np.array([1, 0, 0]))
        radius2 = BraceBetweenPoints((0, 0, -1.95), (0, 6.85 / a, -1.95)).rotate(angle= - PI / 2, axis= np.array([0, 1, 0])).move_to((0, 6.85 / (2 * a), -1.75))
        b3 = radius2.get_text("6,85 cm").move_to(radius2.get_center() + (0, -0.2, 0.4)).rotate(-PI / 2, np.array([0, 1, 0])).rotate(PI / 2, np.array([1, 0, 0]))

        radiuses = VGroup(radius1, b2, radius2, b3)
         

        self.move_camera(phi= PI * 0.47, theta= PI * 4.1 / 4, zoom= 1.4)


        # Trapézios & Triângulo

        self.play(DrawBorderThenFill(trapezium1))
        self.play(FadeOut(truncatedCone, circle1, circle2))
        self.play(Write(h1Group))
        self.play(Write(radius1), Write(b2))
        self.wait()
        self.play(Write(radius2), Write(b3))
        self.wait(1.5)
        self.play(FadeOut(h1Group, radiuses))

        self.play(DrawBorderThenFill(trapezium2))
        self.play(FadeOut(trapezium1))
        self.wait(1)
        self.play(DrawBorderThenFill(triangle))
        self.wait(1)

        pithagoras = MathTex(r"g^2 = h^2 + (R - r)^2").move_to((0, -6.85 / a + 0.5, 1.2)).rotate(-PI / 2, np.array([0, 0, 1])).rotate(-PI / 2, np.array([0, 1, 0])).scale(0.55)
        p1 = pithagoras.copy()
        pith2 = MathTex(r"g^2 = 7,5^2 + 3,25^2").move_to((0, -6.85 / a + 0.6, 0.7)).rotate(-PI / 2, np.array([0, 0, 1])).rotate(-PI / 2, np.array([0, 1, 0])).scale(0.45)
        p2 = pith2.copy()
        pith3 = MathTex(r"g^2 = 56,25 + 10,56").move_to((0, -6.85 / a + 0.37, 0.2)).rotate(-PI / 2, np.array([0, 0, 1])).rotate(-PI / 2, np.array([0, 1, 0])).scale(0.45)
        p3 = pith3.copy()
        pith4 = MathTex(r"g = \sqrt{56,25 + 10,56}").move_to((0, -6.85 / a + 0.15, -0.3)).rotate(-PI / 2, np.array([0, 0, 1])).rotate(-PI / 2, np.array([0, 1, 0])).scale(0.45)
        p4 = pith4.copy()
        pith5 = MathTex(r"g = 8,17").move_to((0, -6.85 / a + 0.45, -0.8)).rotate(-PI / 2, np.array([0, 0, 1])).rotate(-PI / 2, np.array([0, 1, 0])).scale(0.45)
        p5 = pith5.copy()

        equations = VGroup(pithagoras, p1, p2, p3, p4, p5)

        all1 = VGroup(axes, trapezium2, triangle)
        path2 = Line((0, 0, 0), (0, 1.2, 0.8))

        self.play(MoveAlongPath(all1, path2))
        self.move_camera(zoom= 2.5)
        self.wait(1.5)


        # Writing equations

        self.play(Write(pithagoras))
        self.wait()

        self.play(Transform(p1, pith2))
        self.wait()
         
        self.play(Transform(p2, pith3))
        self.wait()
         
        self.play(Transform(p3, pith4))
        self.wait()
         
        self.play(Transform(p4, pith5))
        self.wait()

        self.play(FadeOut(equations, trapezium2, triangle))



        # Parte 2 - Planificação

        self.set_camera_orientation(phi= PI * 0.47, theta= PI * 4.1 / 4, zoom=2.5)

        path3 = Line((0, 1.2, 0.8), (0, 0, 0))

        circle3 = circle1.copy().move_to((- 3.6 / a, - 3.6 / a, -1.95)).set_color(PURPLE).set_fill(color= PURPLE_E , opacity= 1)
        c3 = circle1.copy()
        circle4 = circle2.copy().move_to(((-17.22 - 6.85) / a + 0.255, - 6.85 / a + 0.22, -1.95)).set_color(PURPLE).set_fill(color= PURPLE_E , opacity= 1)
        c4 = circle2.copy()
       
        annulus1 = Sector(outer_radius= 17.22 / a, inner_radius= 8.17 / a, color= PURPLE , fill_opacity= 1).move_to((-3, -2, -1.95)).rotate(angle= PI, axis= (0, 0, 1)).set_fill(PURPLE_E)
        annulus2 = annulus1.copy().rotate_about_origin(-PI * 0.294, axis=(0, 0, 1)).move_to((-3.7, 0.86, -1.95))

        annuluses = VGroup(annulus1, annulus2)
        annuluses.move_to(annuluses.get_center() + (0.85, -1.4, 0))
        all2 = VGroup(c3, c4, annuluses)
        path4 = Line(annuluses.get_center() + (-2, 0, 0), (-0.3, 0, -1.95))

        line2 = Line((3.6, 0.49, 0), (3.6, -0.5, 0))
        line3 = Line((3.6, 0.49, 0), (3, 1.34, 0))
        arc1 = Angle(line2, line3, radius= 0.4, other_angle= True)
        arcV1 = Text("143,2°").rotate(PI, (0, 0, 1)).move_to((2.5, 0.3, 0)).scale(0.6)

        dot1 = Dot((3.6, -0.475, 0), 0.05)
        dot2 = Dot((3, 1.335, 0), 0.05)

        generatrix1 = BraceBetweenPoints((3.6, -1.65, 0), (3.6, -1.63 - 8.17 / a, 0))
        generatrix2 = BraceBetweenPoints((3.6, 0.47, 0), (3.6, -1.65, 0))
        g1 = generatrix1.get_text("8,17 cm").rotate(PI, (1, 0, 0))
        g2 = generatrix2.get_text("9,05 cm").rotate(PI, (1, 0, 0))

        arc2 = Angle(line2, line3, radius= 17.22 / a - 0.4, other_angle= True)
        arc3 = Angle(line2, line3, radius= 9.05 / a - 0.4, other_angle= True)
        arcV2 = MathTex("7,2\pi  cm").rotate(PI, (0, 0, 1)).move_to((0.6, 0, 0)).scale(0.85)
        arcV3 = MathTex("13,7\pi  cm").rotate(PI, (0, 0, 1)).move_to((-1.8, 0, 0)).scale(0.85)


        g1Group = VGroup(generatrix1, g1).rotate(PI, (0, 1, 0)).move_to((4.9, -1.65 - 8.17 / (2 * a), 0))
        g2Group = VGroup(generatrix2, g2).rotate(PI, (0, 1, 0)).move_to((4.9, -0.58, 0))
        arcs = VGroup(arc1, arc2, arc3)
        values = VGroup(g1, g2, arcV1, arcV2, arcV3)
        dots = VGroup(dot1, dot2)

        axes.move_to((1.5, -0.4, 0))
        self.add(axes)

        self.play(MoveAlongPath(axes, path3))
        self.move_camera(phi= PI / 3, zoom= 0.85)
        self.play(FadeIn(truncatedCone))
        self.wait()

        self.play(FadeOut(truncatedCone, axes), Transform(c3, circle3), Transform(c4, circle4), Transform(truncatedSurface, annuluses))
        self.add(annuluses)
        self.play(MoveAlongPath(all2, path4))

        self.move_camera(phi= 0, theta= PI / 2, zoom= 1)
        self.wait(1.5)

        self.play(DrawBorderThenFill(line2), DrawBorderThenFill(line3))
        self.play(Create(dots), Create(generatrix1), Create(generatrix2), Create(arcs), Write(values))


        self.wait()



        # Parte 3 - Áreas

        self.set_camera_orientation(phi= 0, theta= PI / 2, zoom= 1)

        circle1.move_to((- 3.6 / a, - 3.6 / a, -1.95)).set_color(PURPLE).set_fill(color= PURPLE_E , opacity= 1)
        circle2.move_to(((-17.22 - 6.85) / a + 0.255, - 6.85 / a + 0.22, -1.95)).set_color(PURPLE).set_fill(color= PURPLE_E , opacity= 1)

        annulus3 = Sector(outer_radius= 17.22 / a, inner_radius= 8.17 / a, color= PURPLE , fill_opacity= 1).move_to((-3, -2, -1.95)).rotate(angle= PI, axis= (0, 0, 1)).set_fill(PURPLE_E)
        annulus4 = annulus3.copy().rotate_about_origin(-PI * 0.294, axis=(0, 0, 1)).move_to((-3.7, 0.86, -1.95))

        annuluses = VGroup(annulus3, annulus4)
        annuluses.move_to(annuluses.get_center() + (0.85, -1.4, 0))
        all2 = VGroup(circle1, circle2, annuluses).move_to((-0.3, 0, -1.95))

        generatrix3 = BraceBetweenPoints((3.6, 0.47, 0), (3.6, -1.63 - 8.17 / a, 0))
        generatrix4 = BraceBetweenPoints((3.6, 0.47, 0), (3.6, -1.65, 0))
        g3 = generatrix3.get_text("a=17,22 cm").rotate(PI, (1, 0, 0)).scale(0.85)
        g4 = generatrix4.get_text("b=9,05 cm").rotate(PI, (1, 0, 0)).scale(0.85)
    
        g3Group = VGroup(generatrix3, g3).rotate(PI, (0, 1, 0), (3.6, -3.429, 0))
        g4Group = VGroup(generatrix4, g4).rotate(PI, (0, 1, 0), (3.6, -1.16, 0))
        g4Group.move_to(g4Group.get_center() + (0.3, 0, 0))

        area1 = MathTex("\pi r^2").move_to(circle1.get_center()).rotate(PI, (0, 0, 1)).scale(0.8)
        area2 = MathTex("\pi R^2").move_to(circle2.get_center()).rotate(PI, (0, 0, 1)).scale(0.8)
        area3 = MathTex(r"\pi (a^2-b^2) \frac{143,2}{360}").move_to(annuluses.get_center() + (-1, -0.3, 0)).rotate(PI, (0, 0, 1)).scale(0.8)
    
        area1_2 = MathTex("\pi 12,96 cm^2").move_to(circle1.get_center()).rotate(PI, (0, 0, 1)).scale(0.8)
        area2_2 = MathTex("\pi 46,92 cm^2").move_to(circle2.get_center()).rotate(PI, (0, 0, 1)).scale(0.8)
        area3_2 = MathTex("\pi 85,38 cm^2").move_to(annuluses.get_center() + (-1, -0.3, 0)).rotate(PI, (0, 0, 1)).scale(0.8)

        totalArea = MathTex("\pi 85,38 + \pi 46,92 + \pi 12,96 = 145,26\pi cm^2").move_to((-1.6, 3.6, 0)).rotate(PI, (0, 0, 1))

        areas = VGroup(area1, area2, area3, totalArea)

        self.play(DrawBorderThenFill(all2))
        self.wait(2)

        self.play(Write(area1))
        self.wait(1)
        self.play(Write(area2))
        self.wait(1)
        self.play(Write(g3Group), Write(g4Group), Write(area3))
        self.wait(2)

        self.play(Transform(area1, area1_2))
        self.wait(1)
        self.play(Transform(area2, area2_2))
        self.wait(1)
        self.play(Transform(area3, area3_2))
        self.wait(2)
        
        self.play(Write(totalArea))
        self.wait(2)
        self.play(FadeOut(all2, areas, g3Group, g4Group))

        self.play(DrawBorderThenFill(axes))
        self.move_camera(phi = PI * 2 / 5, theta= PI * 5 / 4, zoom= 1.2)
        self.wait(1.5)



        # Parte 3 - Volume

        self.set_camera_orientation(phi = PI * 2 / 5, theta= PI * 5 / 4, zoom= 1.2)

        # Objetos

        trapezium3 = Polygon((0, 3.6 / a, -0.4), (0, 6.85 / a, -2.8), (0, - 6.85 / a, -2.8), (0, - 3.6 / a, -0.4), color= PURPLE_B)
        triangle2 = Polygon((0, 0, 2.25), (0, 0, 2.25), (0, 3.6 / a, -0.4), (0, -3.6 / a, -0.4), color= PURPLE_B)
        triangle3 = Polygon((0, -3.6 / a, -0.4), (0, -3.6 / a, -0.4), (0, -3.6 / a, -2.8), (0, -6.85 / a, -2.8), color= YELLOW_B)
        triangle4 = Polygon((0, 0, 2.25), (0, 0, 2.25), (0, 0, -0.4), (0, -3.6 / a, -0.4), color= BLUE_B)

        t1 = Tex("1").move_to((0, -1.3, -2)).scale(1).rotate(-PI / 2, (0, 1, 0)).rotate(PI / 2, (1, 0, 0))
        t2 = Tex("2").move_to((0, -0.35, 0.5)).scale(1).rotate(-PI / 2, (0, 1, 0)).rotate(PI / 2, (1, 0, 0))

        i_mea_1 = MathTex("h_1").move_to((0, -0.66, -1.6))
        i_mea_2 = MathTex("g_1").move_to((0, -1.85, -1.6))
        i_mea_3 = MathTex("(R - r)").move_to((0, -1.5, -3.15))#.rotate(-PI, (1, 0, 0))#.rotate(PI / 2, (0, 0, 1))
        i_mea_4 = MathTex("h_2").move_to((0, 0.3, 0.8))
        i_mea_5 = MathTex("g_2").move_to((0, -0.9, 0.8))
        i_mea_6 = MathTex("r").move_to((0, -0.5, -0.65))#.rotate(-PI, (1, 0, 0))#.rotate(PI / 2, (0, 0, 1))
         

        f_mea_1 = MathTex("7,5").move_to(i_mea_1.get_center())
        f_mea_2 = MathTex("8,17").move_to(i_mea_2.get_center())
        f_mea_3 = MathTex("3,25").move_to(i_mea_3.get_center())#.rotate(-PI / 2, (1, 0, 0)).rotate(PI / 2, (0, 1, 0))
        f_mea_4 = MathTex("8,3").move_to(i_mea_4.get_center())
        f_mea_5 = MathTex("9,05").move_to(i_mea_5.get_center())
        f_mea_6 = MathTex("3,6").move_to(i_mea_6.get_center())#.rotate(-PI / 2, (1, 0, 0)).rotate(PI / 2, (0, 1, 0))

        kEquation = MathTex(r"\frac{r}{(R-r)} = k").move_to((0, -3.2, 1)).rotate(-PI / 2, (0, 1, 0)).rotate(PI / 2, (1, 0, 0))
        kECopy = kEquation.copy()
        k2 = MathTex(r"\frac{3,6}{3,25} = k").move_to((0, -3.2, -0.5)).scale(0.8).rotate(-PI / 2, (0, 1, 0)).rotate(PI / 2, (1, 0, 0))
        k3 = MathTex(r"1,077 = k").move_to((0, -3.2, -0.5)).scale(0.8).rotate(-PI / 2, (0, 1, 0)).rotate(PI / 2, (1, 0, 0))
        samba = VGroup(iMea3Copy, iMea6Copy)

        initialMeasures = VGroup(i_mea_1, i_mea_2, i_mea_3, i_mea_4, i_mea_5, i_mea_6)
        finalMeasures = VGroup(f_mea_1, f_mea_2, f_mea_3, f_mea_4, f_mea_5, f_mea_6)
        measures = VGroup(i_mea_1, f_mea_1, i_mea_2, f_mea_2, i_mea_3, f_mea_3, i_mea_4, f_mea_4, i_mea_5, f_mea_5, i_mea_6, f_mea_6)

        for i in measures:
            for j in i:
                j.rotate(PI / 2, (1, 0, 0)).rotate(-PI / 2, (0, 0, 1)).scale(0.8)

        all3 = VGroup(axes, trapezium3, triangle2, triangle3, triangle4)

        truncatedCone.move_to(truncatedCone.get_center() + (0, 0, -0.85))

        path5 = Line(axes.get_center(), (0, 0, -0.85))

        self.play(MoveAlongPath(axes, path5))

        self.play(FadeIn(truncatedCone))
        self.move_camera(phi= PI * 1.2 / 3, theta= PI, zoom= 1.2)

        self.play(FadeOut(truncatedCone), Create(trapezium3))
        self.wait()
        self.play(DrawBorderThenFill(triangle2))
        self.wait()
        self.play(DrawBorderThenFill(triangle3))
        self.wait()
        self.play(DrawBorderThenFill(triangle4))

        self.move_camera(zoom=2)

        self.play(Write(initialMeasures))
        self.wait(2)
        self.play(Write(t1), Write(t2))
        self.wait(1)
        self.play(Write(kEquation))
        self.wait(1)
        self.play(Transform(kECopy, k2))
        self.wait()
        self.play(Transform(kECopy, k3))
        self.wait(2)
        for i in range(len(initialMeasures)):
            self.play(Transform(initialMeasures[i - 1], finalMeasures[i - 1].scale(0.8)))
        self.wait(2)
        self.play(Transform(initialMeasures, finalMeasures))
         
        self.play(FadeOut(all3, initialMeasures, kEquation, kECopy, t1, t2))
        self.wait(1)

        
        cone1HeightLine = Line((0, 2, -1.95), (0, 2, 3.2))
        cone1Height = Tex("15,81 cm").move_to((0, 3.15, 0.45)).rotate(-PI / 2, (0, 1, 0)).rotate(PI / 2, (1, 0, 0))

        cone1GeneratrixLine = Line((0, -2, -1.95), (0, -0.075, 3.2))
        cone1Generatrix = Tex("17,22 cm").move_to((0, -2.3, 0.45)).rotate(-PI / 2, (0, 1, 0)).rotate(PI / 2, (1, 0, 0))

        c1H = VGroup(cone1HeightLine, cone1Height)
        c1G = VGroup(cone1GeneratrixLine, cone1Generatrix)

        coneVolFormula = MathTex(r"V = \frac{\pi R^2 h}{3}").rotate(-PI / 2, (0, 0, 1)).scale(2)

        self.set_camera_orientation(phi= PI / 3, theta= PI, zoom= 1.2)

        self.play(FadeIn(cone1))
        self.wait(1)
        self.play(Write(c1H), Write(c1G))
        self.wait(1)

        self.play(FadeOut(cone1, c1H, c1G))


        self.set_camera_orientation(phi= 0, zoom= 1)

        self.play(Write(coneVolFormula))
        self.wait(3)
        self.play(FadeOut(coneVolFormula))

        
        cone1.move_to((0, 3.5, 0)).scale(0.6)
        cone2.move_to(cone1.get_center() + (0, 3.5, 0.6)).scale(0.6)
        truncatedCone.move_to(cone1.get_center() + (0, 0, -0.82)).scale(0.6)

        c1Pos = cone1.get_center()

        path6 = Line((c1Pos[0], c1Pos[1], cone2.get_center()[2]), (0, 0, cone2.get_center()[2]))
        path7 = Line((c1Pos[0], c1Pos[1], truncatedCone.get_center()[2]), (0, -3.5, truncatedCone.get_center()[2]))

        minusT = Tex("-").move_to((0, 1.75, 0)).rotate(PI / 2, (0, 0, 1)).rotate(-PI / 2, (0, 1, 0)).scale(2)
        equalsT = Tex("=").move_to((0, -1.75, 0)).rotate(PI / 2, (0, 0, 1)).rotate(-PI / 2, (0, 1, 0)).scale(2)

        volume = MathTex("247,28\pi - 35,86\pi = 211,42\pi cm^3").scale(1.4).rotate(-PI / 2, (0, 0, 1)).rotate(-PI / 2, (0, 1, 0)).move_to((0, 0, -2.75))

        self.play(FadeIn(cone1, cone2, truncatedCone))
        self.wait(1)
        self.play(MoveAlongPath(cone2, path6), MoveAlongPath(truncatedCone, path7))
        self.wait(1)
        self.play(Write(minusT), Write(equalsT))
        self.wait(1)
        self.play(Write(volume))
        self.wait(2)

        self.play(FadeOut(cone1, cone2, truncatedCone, minusT, equalsT, volume))
