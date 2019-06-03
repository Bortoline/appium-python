from behave import *
from hamcrest import assert_that, equal_to

use_step_matcher("re")


@step('que eu precise buscar um veículo')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    """
    creates a dictionary of arguments (**kwargs) from a behave
    table row.
    """
    for row in context.table:
        cells = [cell if cell != '' else None for cell in row.cells]
        context.values = dict(zip(row.headings, cells))


@step("realizo a busca de carros usados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.buscar_veiculos.tap_jump_login_btn()
    context.buscar_veiculos.tap_want_buy_btn()
    context.buscar_veiculos.tap_radio_used()

    context.buscar_veiculos.tap_state_filter()
    context.buscar_veiculos.select_option_from_filter(context.values['Estado'])

    context.buscar_veiculos.tap_city_filter()
    context.buscar_veiculos.select_option_from_filter(context.values['Cidade'])

    context.buscar_veiculos.tap_vendor_filter()
    context.buscar_veiculos.select_option_from_filter(context.values['Fabricante'])

    context.buscar_veiculos.tap_model_filter()
    context.buscar_veiculos.select_option_from_filter(context.values['Modelo'])

    # context.buscar_veiculos.tap_year_filter()
    # context.buscar_veiculos.select_year_from_filter(context.values['Ano'])

    context.buscar_veiculos.tap_filter_btn()


@step("devo ver a lista de anúncios")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.buscar_veiculos.get_model_name(),
                equal_to("{0} {1}".format(
                    context.values['Fabricante'],
                    context.values['Modelo']).upper()))
