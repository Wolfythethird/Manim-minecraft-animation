# Manim Minecraft Animation

⚠️ **NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.**

This repository contains a Manim (Python) script that programmatically recreates a classic voxel-style main menu. It features a continuous scrolling winter panorama loop, custom grey button layouts, and a sine-wave text bouncing "heartbeat" effect for random splashes.

## 🛠️ Assets Setup Requirement
To comply with copyright laws, **this repository does not include trademarked game assets** (the official text logo or dirt block graphics). 

To run the full `Minecraft` scene animation, you must supply your own source graphics inside the project directory:
1. Provide your main title logo named **`minecraft_name.svg`**
2. Provide your central block asset named **`minecraft.svg`**

## 🚀 How to Run
Make sure you have [Manim](https://manim.community) and its dependencies installed, then run the following command in your terminal:

```bash
manim -pql main.py Minecraft
```

## 📄 Included Community Files
* `main.py` - The complete Python/Manim animation scene code.
* `button.svg` - A custom grey pixelated menu button background asset.
* `panorama.svg` - A custom silhouette winter forest background graphic.
* `splashes.txt` - A text reference file containing randomized menu splash strings.
