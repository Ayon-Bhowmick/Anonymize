from sys import modules

def cli(argv: list) -> list[int, int]:
    argv = argv[1:]
    if len(argv) == 0 or len(argv) > 2:
        print("Invalid number of arguments")
        return [-1, -1]
    elif "-h" in argv or "--help" in argv:
        print("""Usage: py FaceBlur.py <type of anonymity> <output method>
        <type of anonymity>: [-b] or [--blur] for blurring the face,
        [-p] or [--pixelate] for pixelating the face, [-k] or [--black]
        for blacking out the face
        <output>: [-v] or [--video] for video output, [-c] or [--camera]
        for virtual camera output""")
        return [-1, -1]
    ret = []
    if "-b" in argv or "--blur" in argv:
        ret.append(0)
    elif "-p" in argv or "--pixelate" in argv:
        ret.append(1)
    elif "-k" in argv or "--black" in argv:
        ret.append(2)
    else:
        print("Invalid type of anonymity")
        return [-1, -1]
    if "-v" in argv or "--video" in argv:
        ret.append(0)
    elif "-c" in argv or "--camera" in argv:
        ret.append(1)
    else:
        print("Invalid output method")
        return [-1, -1]
    return ret

modules[__name__] = cli
