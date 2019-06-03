from features.support.pages.android.base_screen_page import BaseScreen

btn_entrar = 'btnEntrar'
jump_login = 'txtJumpLogin'
txt_button = 'txtButton'

# Search Filters
radio_used = 'radioUsed'
want_buy = '//*[contains(@text, "comprar")]'
btn_filter = 'btnFilter'

# sub filters
state = '//*[contains(@text, "Estado")]'
city = '//*[contains(@text, "Cidade")]'
vendor = '//*[contains(@text, "Marca")]'
model = '//*[contains(@text, "Modelo")]'
year = '//*[contains(@text, "Ano")]'

# Search Text Screen
edt_search_filter = 'edtSearchFilter'

txt_modelo = 'txtModelo'


class BuscarVeiculos(BaseScreen):
    def __init__(self, context):

        super().__init__(context)

    def ensure_visible(self):
        BaseScreen.base_ensure_visible_by_id(self, btn_entrar)

    def tap_jump_login_btn(self):
        BaseScreen.tap_button(self, 'id', jump_login)

    def tap_want_buy_btn(self):
        BaseScreen.tap_button(self, 'xpath', want_buy)

    def tap_radio_used(self):
        BaseScreen.tap_button(self, 'id', radio_used)

    def tap_state_filter(self):
        BaseScreen.tap_button(self, 'xpath', state)

    def tap_city_filter(self):
        BaseScreen.tap_button(self, 'xpath', city)

    def tap_vendor_filter(self):
        BaseScreen.tap_button(self, 'xpath', vendor)

    def tap_model_filter(self):
        BaseScreen.tap_button(self, 'xpath', model)

    def tap_year_filter(self):
        BaseScreen.tap_button(self, 'xpath', year)

    def select_option_from_filter(self, text):
        BaseScreen.send_keys(self, 'id', edt_search_filter, text=text)
        BaseScreen.tap_button(self, 'id', 'txtLineValue')

    def select_year_from_filter(self, year):
        BaseScreen.send_keys(self, 'id', edt_search_filter, text=year)
        BaseScreen.tap_button(self, 'id', 'txtLineValue')

    def tap_filter_btn(self):
        BaseScreen.tap_button(self, 'id', btn_filter)

    def get_model_name(self):
        return BaseScreen.get_element_text(self, 'id', txt_modelo)
