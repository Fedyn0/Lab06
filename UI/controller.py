import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fill_ddAnno(self):
        self._view.ddAnno.options.append(ft.dropdown.Option("Nessun filtro"))
        for anno in self._model.getAnniVendite():
            self._view.ddAnno.options.append(ft.dropdown.Option(
               anno
            ))
        pass

    def fill_ddBrand(self):
        self._view.ddBrand.options.append(ft.dropdown.Option("Nessun filtro"))
        for brand in self._model.getBrandProdotti():
            self._view.ddBrand.options.append(ft.dropdown.Option(
                brand
            ))
        pass


    def fill_ddRetailer(self):
        self._view.ddRetailer.options.append(ft.dropdown.Option("Nessun filtro"))
        for retailer in self._model.getRetailers():
            self._view.ddRetailer.options.append(ft.dropdown.Option(
                retailer
            ))
        pass

