import requests
import json
import datetime
import os

# 网易新闻 军事区 标题爬取
def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果响应状态码不是200，会抛出异常
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_jsonp(jsonp_data):
    # 找到第一个 '(' 和最后一个 ')'
    start_index = jsonp_data.find('(') + 1
    end_index = jsonp_data.rfind(')')
    if start_index == -1 or end_index == -1 or start_index >= end_index:
        print(f"Failed to find matching parentheses in JSONP data: {jsonp_data}")
        return None
    json_data = jsonp_data[start_index:end_index]
    return json_data


def extract_titles(json_data):
    try:
        data = json.loads(json_data)
        titles = [item.get('title') for item in data]
        return titles
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []


def main():
    urls = [
        'https://news.163.com/special/cm_war/?callback=data_callback',
        'https://news.163.com/special/cm_war_02/?callback=data_callback',
        'https://news.163.com/special/cm_war_03/?callback=data_callback'
    ]
    current_date = datetime.datetime.now().strftime('%Y_%m_%d')
    output_file = f"C:\\Users\\XG1001001\\Desktop\\crawler_detail_war_news\\{current_date}.md"
    if os.path.exists(output_file):
        print(f"文件 {output_file} 已经存在. 停止执行 ")
        return
    for url in urls:
        jsonp_data = fetch_webpage(url)
        if jsonp_data:
            json_data = parse_jsonp(jsonp_data)
            if json_data:
                titles = extract_titles(json_data)
                with open(output_file, 'a', encoding='utf-8') as f:
                    for title in titles:
                        f.write(f"- {title}\n")
                print(url, "请求成功")
            else:
                print("转换失败")
                break  # 终止循环
        else:
            print(url, "请求失败，阻塞后续请求")
            break  # 终止循环


if __name__ == '__main__':
    main()
