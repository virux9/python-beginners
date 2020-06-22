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


class Printer(Hardware):
    """printer class"""

    def __init__(self, name, price, weight, pages_per_sec, is_color, print_dpi):
        super().__init__(name, price, weight, pages_per_sec)
        self.is_color = is_color
        self.print_dpi = print_dpi


class Scanner(Hardware):
    """scanner class"""

    def __init__(self, name, price, weight, pages_per_sec, scan_dpi):
        super().__init__(name, price, weight, pages_per_sec)
        self.scan_dpi = scan_dpi


class Copier(Hardware):
    """copier class"""

    def __init__(self, name, price, weight, pages_per_sec, copy_dpi):
        super().__init__(name, price, weight, pages_per_sec)
        self.copy_dpi = copy_dpi


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
