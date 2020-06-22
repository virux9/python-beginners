class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    """warehouse class"""

    def __init__(self):
        self.wh_list = []
        self.offices = dict()

    def add_unit(self, class_instance, quantity):
        """add unit to warehouse"""
        class_found = False
        for el in self.wh_list:
            if class_instance.__hash__() == el["class_instance"].__hash__():
                el["quantity"] += quantity
                class_found = True
                break
        if not class_found:
            self.wh_list.append({"class_instance": class_instance, "quantity": quantity})

    def add_unit_to_office(self, class_instance, quantity, office_name):
        """add unit to a specific office"""
        if office_name in self.offices:
            # office exists
            # check if class_instance exists in given office:
            class_found = False
            for el in self.offices[office_name]:
                if class_instance.__hash__() == el["class_instance"].__hash__():
                    el["quantity"] += quantity
                    class_found = True
                    break
            if not class_found:
                self.offices[office_name].append({"class_instance": class_instance, "quantity": quantity})

        else:
            # office does not exits, add one
            self.offices[office_name] = [{"class_instance": class_instance, "quantity": quantity}]

    def move_unit(self, class_instance, move_quantity, office_name):
        """move a unit from the warehouse to an office"""
        self.remove_unit(class_instance, move_quantity)
        self.add_unit_to_office(class_instance, move_quantity, office_name)

    def remove_unit(self, class_instance, r_quantity):
        """remove unit from the warehouse"""
        for el in self.wh_list:
            if class_instance.__hash__() == el["class_instance"].__hash__():
                if el["quantity"] - r_quantity < 0:
                    el["quantity"] = 0
                else:
                    el["quantity"] -= r_quantity
                break

    def get_class_by_name(self, name_str):
        for el in self.wh_list:
            if el["class_instance"].name == name_str:
                return el["class_instance"]
        return None

    def print_wh_contents(self):
        print("Warehouse contents:")
        for el in self.wh_list:
            print("  " + el["class_instance"].name, end="\t")
            print("qty: " + str(el["quantity"]))

    def print_offices(self):
        for val in self.offices:
            print(f"Office name: {val}")
            for el in self.offices[val]:
                print("  " + el["class_instance"].name, end="\t")
                print("qty: " + str(el["quantity"]))


class Hardware:
    """hardware class"""

    def __init__(self, name, price, weight, pages_per_sec):
        self.name = name
        self.price = price
        self.weight = weight
        self.pages_per_sec = pages_per_sec

    @staticmethod
    def validate_number(in_str, val_from, val_to):
        if not in_str.isnumeric():
            raise OwnError("must be a number!")
        else:
            num = int(in_str)
            if num < val_from or num > val_to:
                raise OwnError(f"must be in range {val_from} - {val_to}")

    @staticmethod
    def validate_truefalse(in_str):
        if in_str != "y" and in_str != "n":
            raise OwnError(f"must be 'y' or 'n' lowercase!")

    def __str__(self):
        out_str = f"  name: {self.name}\n"
        out_str += f"  price: {self.price}\n"
        out_str += f"  weight: {self.weight}\n"
        out_str += f"  pages/sec: {self.pages_per_sec}\n"
        return out_str


class Printer(Hardware):
    """printer class"""

    def __init__(self, name, price, weight, pages_per_sec, is_color, print_dpi):
        super().__init__(name, price, weight, pages_per_sec)
        self.is_color = is_color
        self.print_dpi = print_dpi

    def __str__(self):
        out_str = f"Printer\n"
        out_str += super().__str__()
        out_str += f"  color: {self.is_color}\n"
        out_str += f"  print dpi: {self.print_dpi}\n"
        return out_str


class Scanner(Hardware):
    """scanner class"""

    def __init__(self, name, price, weight, pages_per_sec, scan_dpi):
        super().__init__(name, price, weight, pages_per_sec)
        self.scan_dpi = scan_dpi

    def __str__(self):
        out_str = f"Scanner\n"
        out_str += super().__str__()
        out_str += f"  scan dpi: {self.scan_dpi}\n"
        return out_str


class Copier(Hardware):
    """copier class"""

    def __init__(self, name, price, weight, pages_per_sec, copy_dpi):
        super().__init__(name, price, weight, pages_per_sec)
        self.copy_dpi = copy_dpi

    def __str__(self):
        out_str = f"Copier\n"
        out_str += super().__str__()
        out_str += f"  copy dpi: {self.copy_dpi}\n"
        return out_str


wh = Warehouse()

printer_1 = Printer("epson printer", 20, 3, 10, True, 1200)
printer_2 = Printer("hp printer", 30, 1, 11, True, 1900)
scanner_1 = Scanner("hp scanner", 21, 2, 14, 1200)
scanner_2 = Scanner("canon scanner", 19, 2, 14, 1200)
copier_1 = Copier("canon copier", 22, 10, 10, 3000)
copier_2 = Copier("xerox copier", 21, 10, 10, 3200)

wh.add_unit(printer_1, 2)
wh.add_unit(printer_1, 3)
wh.add_unit(printer_2, 10)
wh.add_unit(scanner_1, 3)
wh.add_unit(scanner_2, 7)
wh.add_unit(copier_1, 3)
wh.add_unit(copier_2, 5)
wh.add_unit(copier_1, 3)
wh.add_unit(scanner_1, 3)

wh.print_wh_contents()
wh.print_offices()

wh.move_unit(printer_1, 2, "main")
wh.move_unit(scanner_1, 2, "main")
wh.move_unit(copier_2, 2, "main")
wh.move_unit(printer_2, 1, "offshore")
wh.move_unit(scanner_2, 1, "offshore")
wh.move_unit(copier_1, 1, "offshore")
wh.move_unit(copier_2, 1, "main")
wh.move_unit(copier_1, 1, "offshore")

print("-------------------------------------")
wh.print_wh_contents()
wh.print_offices()

while True:
    try:
        hw_type = input("Type of hardware to add(1=printer, 2=scanner, 3=copier) :")
        Hardware.validate_number(hw_type, 1, 3)
        qty = input("How much items of this type to add to the warehouse? :")
        Hardware.validate_number(qty, 1, 1000000)
        qty = int(qty)
        hw_name = input("name: ")
        hw_price = input("price: ")
        Hardware.validate_number(hw_price, 1, 1000000)
        hw_price = int(hw_price)
        hw_weight = input("weight: ")
        Hardware.validate_number(hw_weight, 1, 1000)
        hw_weight = int(hw_weight)
        hw_pages_sec = input("pages/sec: ")
        Hardware.validate_number(hw_pages_sec, 1, 100)
        hw_pages_sec = int(hw_pages_sec)
        if hw_type == "1":
            p_is_color = input("is color(y/n): ")
            Hardware.validate_truefalse(p_is_color)
            if p_is_color == "y":
                p_is_color = True
            else:
                p_is_color = False
            p_dpi = input("printer dpi: ")
            Hardware.validate_number(p_dpi, 1, 10000)
            p_dpi = int(p_dpi)
            wh.add_unit(Printer(hw_name, hw_price, hw_weight, hw_pages_sec, p_is_color, p_dpi), qty)
        if hw_type == "2":
            s_dpi = input("scanner dpi: ")
            Hardware.validate_number(s_dpi, 1, 10000)
            s_dpi = int(s_dpi)
            wh.add_unit(Scanner(hw_name, hw_price, hw_weight, hw_pages_sec, s_dpi), qty)
        if hw_type == "3":
            c_dpi = input("copier dpi: ")
            Hardware.validate_number(c_dpi, 1, 10000)
            c_dpi = int(c_dpi)
            wh.add_unit(Copier(hw_name, hw_price, hw_weight, hw_pages_sec, c_dpi), qty)

        s = input("want to add more? (y/n): ")
        Hardware.validate_truefalse(s)
        if s == "n":
            break

    except OwnError as err:
        print(err)
        print("Try again:")
        continue

wh.print_wh_contents()

while True:
    try:
        item_name = input("enter the name of warehouse item you want to move: ")
        item_class = wh.get_class_by_name(item_name)
        if item_class is None:
            raise OwnError("item of this name not exists in the warehouse.")
        item_qty = input("enter the quantity of items you want to move: ")
        Hardware.validate_number(item_qty, 1, 100000)
        item_qty = int(item_qty)
        office_name = input("enter the name of the office you want to move the item to (new name creates new office): ")

        wh.move_unit(item_class, item_qty, office_name)
        print("done moving.")
        print()
        wh.print_wh_contents()
        wh.print_offices()

        s = input("want to move more? (y/n): ")
        Hardware.validate_truefalse(s)
        if s == "n":
            break

    except OwnError as err:
        print(err)
        print("Try again:")
        continue

print("program ended.")
