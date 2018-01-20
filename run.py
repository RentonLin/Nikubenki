# -*- coding: utf-8 -*-
from farm import rt_farm
from strategy import smartphone_dc_strategy

rt_farm.set_current_strategy(smartphone_dc_strategy())
#rt_farm.farm_exp()
rt_farm.refresh_car_list(False)
#rt_farm.refresh_car_list(True)

