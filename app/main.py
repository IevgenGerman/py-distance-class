from typing import Any, Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | float") -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)

    def __iadd__(self, other: "Distance | float ") -> "Distance":
        if isinstance(other, Distance):
            self.km += + other.km
            return self
        if isinstance(other, (int, float)):
            self.km += + other
            return self

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km * other
            )

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            if other != 0:
                new_km = self.km / other
                return Distance(round(new_km, 2))

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km < other

    def __le__(self, other: Any) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km <= other

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km > other

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km >= other

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == other
