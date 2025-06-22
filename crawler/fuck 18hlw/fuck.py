import requests
from bs4 import BeautifulSoup
import os
from utils.fuckyou import urlToBase64
import base64

# 初始页、最大页码
page = 1
maxPage = 5

# 找到所有带有指定class的div元素
divs = []

# 要保存图片的目录路径
download_dir = r'C:\Users\ldf\Downloads\fuck18hlw'
os.makedirs(download_dir, exist_ok=True)


# 通过遍历列表，进行图片下载
def downloadImg(divs):
    for index in range(0, len(divs)):
        print('正在下载第%s页数据' % (index + 1,))
        for div in divs[index]:
            onload_str = div.find('img')['onload']  # 获取 img 标签的 onload 属性值
            url_start = onload_str.find("('") + 15  # 找到 URL 开始位置
            url_end = onload_str.find("')")  # 找到 URL 结束位置
            if url_start != -1 and url_end != -1:
                img_url = onload_str[url_start:url_end]  # 提取 URL
                base64_data = urlToBase64(img_url)  # 调用函数将 URL 转换为 base64 编码

                # 构建保存图片的文件路径
                image_filename = os.path.join(download_dir, f'image_{index}_{divs[index].index(div)}.png')

                # 将 base64 编码的图片数据解码为二进制数据
                binary_data = base64.b64decode(base64_data)
                # 将二进制数据写入文件
                with open(image_filename, 'wb') as f:
                    f.write(binary_data)
                print(f"Image saved to: {image_filename}")
            continue
        else:
            print("第%s页下载完毕" % (index + 1,))
    else:
        print("it's over!")


# 获取每页的数据
def pageContent():
    global page, maxPage
    # 发送请求并获取页面内容
    while (page <= maxPage):
        print('正在获取第%s页数据' % (page,))
        # 要爬取的网页URL
        url = 'https://18hlw.com/category/2/%s.html' % page
        response = requests.get(url)
        html_content = response.text

        # 使用BeautifulSoup解析页面内容
        soup = BeautifulSoup(html_content, 'html.parser')

        divs.append(soup.find_all('div', class_='placeholder-img'))
        print('第%s页数据获取完毕' % (page,))
        page += 1
    else:
        print('页面数据获取完毕，开始下载数据.....')
        downloadImg(divs)


pageContent()
