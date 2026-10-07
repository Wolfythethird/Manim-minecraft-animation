# Manim Minecraft Animation

NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.

This is a quick Manim script that recreates the classic Minecraft main menu screen. It includes the continuous scrolling background loop, custom button placement, and a basic sine-wave script to handle the yellow splash text bouncing heartbeat loop.

## Preview


https://github.com/user-attachments/assets/5d3334c0-b53d-4127-adc3-05ec59c32a13



## Setup & Running the Code
Because official game assets are copyrighted by Mojang/Microsoft, I did not include the official logos or block graphics in this repository. 

If you want to run the scene exactly as-is, you'll need to drop your own vector assets into the root folder:
1. Save your title logo as `minecraft_name.svg`
2. Save your central dirt block graphic as `minecraft.svg`

Once those are in place, make sure you have Manim installed and run:

```bash
manim -pql main.py Minecraft
```

## Files in this Repo
* `main.py` - The animation script containing the scene logic.
* `button.svg` - A basic grey pixelated button base.
* `panorama.svg` - Silhouette winter forest banner for the background loop.
* `splashes.txt` - Text file with a list of the random splash screen quotes.
* `Minecraft.mp4` - A pre-rendered video file showing how the final animation looks.
