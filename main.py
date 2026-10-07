from manim import *
import numpy as np
from random import choice

class Minecraft(Scene):
    def construct(self):
        # Set up the moving background panorama loop
        video_tape, image_width = self.create_panorama()
        self.play(DrawBorderThenFill(video_tape))

        # Build the menu items and save a clean copy of the splash text for the bounce logic
        minecraft_name, minecraft, menu_buttons, splash_text = self.create_gui()
        self.splash_reference = splash_text.copy()

        # Split up the panorama width to match each animation's runtime so the scroll speed stays constant
        slide_step_1 = image_width * (8 / 10)
        slide_step_2 = image_width * (1 / 10)
        slide_step_3 = image_width * (1.5 / 10)
        slide_step_4 = image_width * (2 / 10) 

        # Intro phase: Scroll the background for 8 seconds while drawing the title logo
        self.play(
            video_tape.animate.shift(LEFT * slide_step_1),
            AnimationGroup(
                Write(minecraft_name, run_time=1.25),
                DrawBorderThenFill(minecraft, run_time=1.25),
                Wait(run_time=1),
                lag_ratio=0.5
            ),
            run_time=8, 
            rate_func=linear
        )

        # Morph phase: Turn the main logo block into the menu buttons over 1 second
        self.play(
            video_tape.animate.shift(LEFT * slide_step_2),
            ReplacementTransform(minecraft, menu_buttons, run_time=0.5),
            run_time=1,
            rate_func=linear
        )
        
        # Text phase: Write out the yellow splash text over 2 seconds
        self.play(
            video_tape.animate.shift(LEFT * slide_step_3),
            Write(splash_text, run_time=0.5),
            run_time=2,
            rate_func=linear
        )
        
        # Idle phase: Start the infinite yellow text bounce loop and let the scene roll for 2 more seconds
        splash_text.add_updater(lambda mob, dt: self.bounce_splash(mob, dt))
        self.play(
            video_tape.animate.shift(LEFT * slide_step_4),
            run_time=2,
            rate_func=linear
        )

    def create_panorama(self):
        """Stitches the background SVGs side-by-side into a continuous scrolling ribbon."""
        base_image = SVGMobject("panorama.svg").scale_to_fit_height(config.frame_height)
        left_mirror = base_image.copy().flip(Y_AXIS)
        right_mirror = base_image.copy().flip(Y_AXIS)
        video_tape = VGroup(left_mirror, base_image, right_mirror).arrange(RIGHT, buff=-0.02)
        video_tape.shift(ORIGIN - base_image.get_center()).set_z_index(0)
        return video_tape, base_image.get_width()

    def create_gui(self):
        """Creates the logos, text, buttons, and layouts for the screen overlay."""
        minecraft_name = SVGMobject("minecraft_name.svg").move_to(UP * 2).set_z_index(2)
        minecraft = SVGMobject("minecraft.svg").scale(2).move_to(DOWN * 1.5).set_z_index(2)
        
        # Set up the text words for the menu buttons
        texts = [
            Text("Play", font_size=44, color=GREEN),
            Text("Multiplayer", font_size=44, color=BLUE),
            Text("Options", font_size=44, color=YELLOW),
            Text("Quit", font_size=44, color=RED)
        ]
        
        # Fit a background button SVG behind each individual word with a little padding
        button_pairs = []
        for txt in texts:
            bg_svg = SVGMobject("button.svg")
            
            bg_svg.scale_to_fit_width(txt.get_width() + 1.0)
            bg_svg.scale_to_fit_height(txt.get_height() + 0.4)
            
            # Put the text on top of the button background layer
            bg_svg.set_z_index(2)
            txt.set_z_index(3) 
            
            txt.move_to(bg_svg.get_center())
            
            combined_button = VGroup(bg_svg, txt)
            button_pairs.append(combined_button)

        # Stack the completed button pairs vertically below the title
        menu_buttons = VGroup(*button_pairs)
        menu_buttons.arrange(DOWN, buff=0.2)
        menu_buttons.move_to(DOWN * 1.5)

        # Dynamic file loader for reading splashes.txt safely
        try:
            with open("splashes.txt", "r", encoding="utf-8") as f:
                all_splashes = [line.strip() for line in f if line.strip()]
            chosen_splash = choice(all_splashes)
        except FileNotFoundError:
            # Safe backup text if your flashes.txt document is missing
            chosen_splash = "Missing splashes.txt!"

        # Set up the classic yellow splash text positioning and tilt angle
        splash_text = Text(chosen_splash, color=YELLOW)
        splash_text.set_z_index(3)
        splash_text.move_to(UP*(config.frame_height/6)+RIGHT*(config.frame_width/3.2))
        splash_text.rotate(20 * DEGREES)

        return minecraft_name, minecraft, menu_buttons, splash_text

    def bounce_splash(self, mobject, dt):
        # Use a sine wave to calculate the heartbeat pulse factor over time
        bounce_factor = 1.0 + 0.08 * np.sin(self.time * 5)
        
        # Clear previous transform distortions so scales don't accumulate and blow up
        mobject.matrix = None 
        
        # Reset the text back to its original size, position, and rotation baseline
        mobject.match_points(self.splash_reference)
        
        # Scale the text dynamically around its own center point to create the pulse
        mobject.scale(bounce_factor, about_point=self.splash_reference.get_center())
