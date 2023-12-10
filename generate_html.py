from bs4 import BeautifulSoup
import json

# 读取HTML文件
with open('index_dynamic.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# 读取JSON文件
with open('site.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到需要替换的<div>标签
div_tag = soup.find('div', id='dynamicContent')

# 生成新的HTML内容
new_html_content = ''
if div_tag:
    for class_key in data:
        # class_info = data.get('class11', {})
        class_info = data[class_key]
        if class_info:
            class_name = class_info.get('class_name', '')
            link_list = class_info.get('link_list', {})

            new_html_content += f"<!--\n\t\t{class_name}\n\t-->\n"
            new_html_content += '<div class="d-flex flex-fill ">\n'
            new_html_content += f'\t<h4 class="text-gray text-lg mb-4">\n\t\t<i class="site-tag iconfont icon-tag icon-lg mr-1" id="term-{class_key[-2:]}"></i>\n\t\t{class_name}\n\t</h4>\n'
            new_html_content += '\t<div class="flex-fill"></div>\n'
            new_html_content += '\t<!-- <a class=\'btn-move text-xs\' href=\'#\'>more+</a> -->\n</div>\n'

            new_html_content += '<div class="row">\n'
            for key, item in link_list.items():
                new_html_content += f'\t<!-- {item["name"]} -->\n'
                new_html_content += f'\t<div class="url-card col-6 col-sm-6 col-md-4 col-xl-5a col-xxl-6a">\n'
                new_html_content += '\t\t<div class="url-body default">\n'
                new_html_content += f'\t\t\t<a href="{item["link"]}" target="_blank" data-id="{key}" data-url="{item["link"]}" class="card no-c mb-4 site-{key}" data-toggle="tooltip" data-placement="bottom" title="{item["descr"]}">\n'
                new_html_content += '\t\t\t\t<div class="card-body">\n'
                new_html_content += '\t\t\t\t\t<div class="url-content d-flex align-items-center">\n'
                new_html_content += f'\t\t\t\t\t\t<div class="url-img rounded-circle mr-2 d-flex align-items-center justify-content-center">\n\t\t\t\t\t\t\t<img class="lazy" src="{item["img"]}" data-src="{item["img"]}" onerror="javascript:this.src=\'{item["img"]}\'" alt="{item["name"]}">\n\t\t\t\t\t\t</div>\n'
                new_html_content += '\t\t\t\t\t\t<div class="url-info flex-fill">\n'
                new_html_content += f'\t\t\t\t\t\t\t<div class="text-sm overflowClip_1">\n\t\t\t\t\t\t\t\t<strong>{item["name"]}</strong>\n\t\t\t\t\t\t\t</div>\n'
                new_html_content += f'\t\t\t\t\t\t\t<p class="overflowClip_1 m-0 text-muted text-xs">{item["descr"]}</p>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</a>\n'
                new_html_content += f'\t\t\t<a href="{item["link"]}" class="togo text-center text-muted is-views" data-id="{key}" data-toggle="tooltip" data-placement="right" title="直达" rel="nofollow"><i class="iconfont icon-goto"></i></a>\n'
                new_html_content += '\t\t</div>\n\t</div>\n'
            new_html_content += '</div>'

    new_tag = BeautifulSoup(new_html_content, 'html.parser')
    div_tag.replace_with(new_tag)

    # 将替换后的内容写入新的HTML文件
    with open('index.html', 'w', encoding='utf-8') as new_html_file:
        new_html_file.write(str(soup))
