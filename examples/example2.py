# examples.py
import time
from rgbterminal import RGBText, RGBTextFactory, GradientText, GradientTextFactory  # replace with actual module name

def demo_rgb_text():
    print("=== RGBText Demo ===\n")

    # Single RGB text with truecolor
    text = RGBText("Hello Truecolor!", rgb=(255, 100, 50), truecolor=True)
    print("Truecolor:", text)

    # Single RGB text with 256-color approximation
    text256 = RGBText("Hello 256-color!", rgb=(255, 100, 50), truecolor=False)
    print("256-color:", text256)

    # Using factory
    factory = RGBTextFactory(rgb=(0, 200, 255), truecolor=True)
    print("Factory text:", factory.t("Factory Truecolor!"))
    print("Factory 256-color:", factory.text("Factory 256-color!", truecolor=False))

def demo_gradient_text():
    print("\n=== GradientText Demo ===\n")

    text = "Gradient Example with HLS interpolation"

    # Simple two-color gradient
    simple_gradient = GradientText(
        text=text,
        rgb_stops=[(255, 0, 0), (0, 0, 255)],
        truecolor=True
    )
    print("Two-color gradient:", simple_gradient)

    # Multi-stop gradient
    multi_gradient = GradientText(
        text=text,
        rgb_stops=[
            (255, 0, 0),   # red
            (255, 255, 0), # yellow
            (0, 255, 0),   # green
            (0, 255, 255), # cyan
            (0, 0, 255),   # blue
            (255, 0, 255)  # magenta
        ],
        truecolor=True
    )
    print("Multi-stop gradient:", multi_gradient)

    # 256-color fallback
    fallback_gradient = GradientText(
        text=text,
        rgb_stops=[(255,0,0), (0,0,255)],
        truecolor=False
    )
    print("256-color gradient:", fallback_gradient)

def demo_gradient_factory():
    print("\n=== GradientTextFactory Demo ===\n")

    factory = GradientTextFactory(
        rgb_stops=[(255,0,0), (255,255,0), (0,255,0), (0,255,255), (0,0,255), (255,0,255)],
        truecolor=True
    )

    print("Using factory default gradient:")
    print(factory.t("Rainbow Factory Gradient!"))

    print("\nOverriding gradient stops for this text:")
    custom_stops = [(255, 128, 0), (128, 0, 255)]
    print(factory.t("Custom Gradient Override", rgb_stops=custom_stops))

def demo_animation():
    print("\n=== Animated Gradient Demo ===\n")
    factory = GradientTextFactory(
        rgb_stops=[(255,0,0), (0,255,0), (0,0,255)],
        truecolor=True
    )
    text = "Animating gradient... "

    try:
        for i in range(20):
            # rotate stops
            stops = factory.rgb_stops[i % len(factory.rgb_stops):] + factory.rgb_stops[:i % len(factory.rgb_stops)]
            print(factory.t(text, rgb_stops=stops), end="\r", flush=True)
            time.sleep(0.1)
        print()  # newline at the end
    except KeyboardInterrupt:
        print("\nAnimation stopped.")

if __name__ == "__main__":
    demo_rgb_text()
    demo_gradient_text()
    demo_gradient_factory()
    demo_animation()
