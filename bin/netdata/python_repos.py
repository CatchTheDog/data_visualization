import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
request = requests.get(url)

print("Status code:", request.status_code)

response_dict = request.json()
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	if repo_dict['description'] and repo_dict['html_url']:
		plot_dict = {
			'value': repo_dict['stargazers_count'],
			'label': repo_dict['description'],
			'xlink': repo_dict['html_url']
		}
	else:
		plot_dict = {
			'value': repo_dict['stargazers_count'],
			'label': 'none',
			'xlink': 'none'
		}
	plot_dicts.append(plot_dict)

# 可视化
my_style = LS("#333366", base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
