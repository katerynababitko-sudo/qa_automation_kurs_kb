class Rhombus:
    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("side_a must be > 0")

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("angle_a must be between 0 and 180")

            # Set angle_a
            super().__setattr__(name, value)

            # Automatically update angle_b
            super().__setattr__("angle_b", 180 - value)
            return

        elif name == "angle_b":
            raise AttributeError("angle_b is calculated automatically")

        super().__setattr__(name, value)


rhombus = Rhombus()
rhombus.side_a = 10
rhombus.angle_a = 100

print(f"A new rhombus is added with:\n "
      f"side_a = {rhombus.side_a}\n angle_a = {rhombus.angle_a}\n angle_b = {rhombus.angle_b}")

