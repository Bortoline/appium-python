from features.support.pages.android import buscar_veiculos_page


def add_page_objects_to_android_context(context):
    context.buscar_veiculos = buscar_veiculos_page.BuscarVeiculos(context)
