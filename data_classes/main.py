from dataclasses import dataclass, field


def euclidean_norm(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** 0.5


@dataclass
class Point3D:
    x: float
    y: float
    z: float
    _norm: float = field(init=False)

    def __post_init__(self) -> None:
        self._norm = euclidean_norm(self.x, self.y, self.z)

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)


def main() -> None:
    p1 = Point3D(1, 2, 1)
    print(p1)
    p2 = Point3D(2, 0, 0)
    print(p2)
    p3 = p1 + p2
    print(p3)


main()
