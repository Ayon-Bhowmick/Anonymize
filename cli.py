from sys import modules

def cli(argv: list):
    argv = argv[1:]
    if len(argv) == 0 or len(argv) > 2:
        print("Invalid number of arguments")
        return -1
    elif "-h" in argv or "--help" in argv:
        print("""Usage: py FaceBlur.py <type of anonymity> <output>
        <type of anonymity>: [-b] or [--blur] for blurring the face,
        [-p] or [--pixelate] for pixelating the face, [-k] or [--black]
        for blacking out the face
        <output>: [-v] or [--video] for video output, [-c] or [--camera]
        for virtual camera output""")
        return 0
    elif

modules[__name__] = cli
