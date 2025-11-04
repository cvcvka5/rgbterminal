# examples/example.py

from rgbterminal import RGBText, RGBTextFactory

def demo_rgbterminal():
    print("=== RGBText Demo ===")

    # Direct RGBText usage
    text1 = RGBText("Hello 256-color!", rgb=(120, 200, 80), truecolor=False)
    print(text1)  # 256-color output

    text2 = RGBText("Hello Truecolor!", rgb=(120, 200, 80), truecolor=True)
    print(text2)  # Truecolor output

    # Access properties
    print("RGB values:", text2.r, text2.g, text2.b)
    print("Cube levels:", text2.r_level, text2.g_level, text2.b_level)
    print("256-color code:", text2.code)
    print("256-color string:", text2.in_256color)

def demo_factory():
    print("\n=== RGBTextFactory Demo ===")

    # Create a factory with a preset color
    factory = RGBTextFactory((255, 100, 50))

    # Generate multiple texts with same color
    t1 = factory.t("Factory 256-color text")
    t2 = factory.t_truecolor("Factory Truecolor text")
    t3 = factory.text("Another 256-color text")

    print(t1)
    print(t2)
    print(t3)

    # Access factory properties
    print("Factory RGB:", factory.r, factory.g, factory.b)
    print("Factory cube levels:", factory.r_level, factory.g_level, factory.b_level)
    print("Factory 256-color code:", factory.code)

if __name__ == "__main__":
    demo_rgbterminal()
    demo_factory()