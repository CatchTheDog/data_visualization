import json

from pygal.style import *
from pygal_maps_world.i18n import COUNTRIES as countries
from pygal_maps_world.maps import World


def get_country_code(country_name):
	"""根据指定的国家，返回Pygal使用的两个字母的国别码"""
	for code, name in countries.items():
		if name == country_name:
			return code
	return None


# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		country_code = get_country_code(country_name)
		if country_code:
			cc_populations[country_code] = population

# 根据人口数量将所有的国家进行分组——少于1000万，介于1000万和10亿之间以及超过10亿的国家
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

wm = World()
wm.style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm.title = 'World Population in 2010 , by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
