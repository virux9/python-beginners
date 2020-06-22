class Warehouse:
    """warehouse class"""


class Hardware:
    """hardware class"""

    def __init__(self, name, price, weight, pages_per_sec):
        self.name = name
        self.price = price
        self.weight = weight
        self.pages_per_sec = pages_per_sec


class Printer(Hardware):
    """printer class"""

    def __init__(self, is_color, print_dpi):
        self.is_color = is_color
        self.print_dpi = print_dpi


class Scanner(Hardware):
    """scanner class"""

    def __init__(self, scan_dpi):
        self.scan_dpi = scan_dpi


class Copier(Hardware):
    """copier class"""

    def __init__(self, copy_dpi):
        self.copy_dpi = copy_dpi
