import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None
        self._anno = None
        self._brand = None

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
               anno,
                on_click= self.read_anno
            ))
        pass

    def fill_ddBrand(self):
        self._view.ddBrand.options.append(ft.dropdown.Option("Nessun filtro"))
        for brand in self._model.getBrandProdotti():
            self._view.ddBrand.options.append(ft.dropdown.Option(
                brand,
                on_click = self.read_brand
            ))
        pass


    def fill_ddRetailer(self):
        self._view.ddRetailer.options.append(ft.dropdown.Option("Nessun filtro"))
        for retailer in self._model.getRetailers():
            self._view.ddRetailer.options.append(ft.dropdown.Option(
                key = retailer.Retailer_code,
                text = retailer.__str__(),
                data = retailer,
                on_click = self.read_retailer
            ))
        pass

    def read_retailer(self, e):
        self._retailer = e.control.data

    def read_anno(self, e):
        self._anno = e.control.data

    def read_brand(self, e):
        self._brand = e.control.data

    def handle_btn_top_vendite(self, e):

        if not self._view.ddAnno.value:
            self._view.create_alert("Scegliere un anno oppure l'opzione *Nessun filtro*")
            self._view.update_page()
            return

        if not self._view.ddBrand.value:
            self._view.create_alert("Scegliere un brand oppure l'opzione *Nessun filtro*")
            self._view.update_page()
            return

        if not self._view.ddRetailer.value:
            self._view.create_alert("Scegliere un Retailer oppure l'opzione *Nessun filtro*")
            self._view.update_page()
            return


        anno = self._view.ddAnno.value
        brand = self._view.ddBrand.value
        retailer = self._view.ddRetailer.value

        if anno == "Nessun filtro":
            anno = None

        if brand == "Nessun filtro":
            brand = None

        if retailer == "Nessun filtro":
            retailer = None

        top_vendite = self._model.getTopVendite(anno, brand, retailer)

        if not len(top_vendite):
            self._view.create_alert("Nessuna vendita corrisponde ai filtri selezionati")
            self._view.update_page()

        for vendita in top_vendite:
            self._view.txt_result.controls.append(ft.Text(f"Vendita: {vendita}"))
            self._view.update_page()







