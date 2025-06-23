import subprocess
import os
import base64
import requests
import re
import random

# 下载图片并转换为 Base64 编码
def get_base64_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content_type = response.headers['Content-Type']
        image_type = 'jpeg' if 'jpeg' in content_type else 'png' if 'png' in content_type else 'gif'
        return f"data:image/{image_type};base64,{base64.b64encode(response.content).decode()}"
    except Exception as e:
        print(f"下载图片失败: {url}, 错误: {e}")
        return ""

# 替换 HTML 中的图片链接
def replace_images_with_base64(html):
    img_tag_pattern = r'<img\b[^>]*?src=(["\'])(.*?)\1'

    # 缓存已下载的图片
    image_cache = {}

    def replace_src(match):
        quote = match.group(1)
        original_url = match.group(2).strip()

        # 跳过已经是 base64 或非外链图片
        if original_url.startswith("data:") or not original_url.startswith(("http://", "https://")):
            return match.group(0)

        # 清理URL中的多余空格和参数
        clean_url = original_url.split('?')[0].strip()

        # 检查缓存
        if clean_url in image_cache:
            base64_data = image_cache[clean_url]
        else:
            base64_data = get_base64_image(clean_url)
            if base64_data:
                image_cache[clean_url] = base64_data
            else:
                return match.group(0)  # 转换失败则保留原图

        # 替换为base64编码
        return match.group(0).replace(
            f'src={quote}{original_url}{quote}',
            f'src={quote}{base64_data}{quote}'
        )

    return re.sub(img_tag_pattern, replace_src, html)

# 将 HTML 转换为 Word 文档
def html_to_word_pandoc(html_content, output_path):
    temp_html = "temp.html"
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    try:
        subprocess.run(
            [r"C:\Program Files\Pandoc\pandoc.exe", temp_html, "-o", output_path],
            check=True
        )
        print(f"使用Pandoc成功生成Word文档: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Pandoc转换失败: {e}")
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)

html_content ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-family: Arial, sans-serif;
        }
        th, td {
            border: 1px solid #dddddd;
            padding: 12px;
            text-align: center;
            vertical-align: middle;
        }
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        img {
            max-width: 150px;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        .caption {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }
    </style>
</head>
<body>
 <h1>产品展示表</h1>

    <table>
        <thead>
            <tr>
                <th>产品ID</th>
                <th>产品图片</th>
                <th>产品名称</th>
                <th>价格</th>
                <th>描述</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>001</td>
                <td>
                    <img src="https://img95.699pic.com/xsj/0e/g8/qf.jpg?query=1" alt="产品1">
                    <div class="caption">点击查看大图</div>
                </td>
                <td>高端智能手机</td>
                <td>¥5,999</td>
                <td>最新款旗舰手机，配备顶级摄像头</td>
            </tr>
            <tr>
                <td>002</td>
                <td>
                    <img src="https://img95.699pic.com/xsj/0e/g8/qf.jpg?query=2" alt="产品2">
                    <div class="caption">点击查看大图</div>
                </td>
                <td>无线蓝牙耳机</td>
                <td>¥899</td>
                <td>主动降噪，30小时续航</td>
            </tr>
            <tr>
                <td>003</td>
                <td>
                    <img src="https://img95.699pic.com/xsj/0e/g8/qf.jpg?query=3" alt="产品3">
                    <div class="caption">点击查看大图</div>
                </td>
                <td>智能手表</td>
                <td>¥1,299</td>
                <td>健康监测，50米防水</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="5" style="text-align: right;">更新时间: 2023年11月</td>
            </tr>
        </tfoot>
    </table>

    <h2>技术规格对比</h2>

    <table>
        <tr>
            <th rowspan="2">产品</th>
            <th colspan="3">主要参数</th>
        </tr>
        <tr>
            <th>尺寸</th>
            <th>重量</th>
            <th>电池容量</th>
        </tr>
        <tr>
            <td>
                <img src="https://bpic.588ku.com/element_origin_min_pic/23/07/11/d32dabe266d10da8b21bd640a2e9b611.jpg?query=4" alt="手机" style="max-width: 80px;">
                智能手机
            </td>
            <td>158.3 x 73.6 x 8.2 mm</td>
            <td>189g</td>
            <td>4500mAh</td>
        </tr>
        <tr>
            <td>
                <img src="https://img95.699pic.com/xsj/0e/g8/qf.jpg?query=5" alt="手表" style="max-width: 80px;">
                智能手表
            </td>
            <td>44 x 44 x 10.7 mm</td>
            <td>32g</td>
            <td>300mAh</td>
        </tr>
    </table>
</body>
</html>"""
output_path = r"C:\Users\XG1001001\Downloads\test.docx"

if __name__ == "__main__":
    processed_html = replace_images_with_base64(html_content)
    html_to_word_pandoc(processed_html, output_path)