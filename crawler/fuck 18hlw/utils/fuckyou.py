from Crypto.Cipher import AES
import base64
import requests


# 解密base64,使用aes加密算法，密钥和初始向量都是从黑料网的脚本里面得到的。
def decrypt_image(encrypted_base64_data):
    # 定义密钥和初始向量
    key_string = "102_53_100_57_54_53_100_102_55_53_51_51_54_50_55_48"
    iv_string = "57_55_98_54_48_51_57_52_97_98_99_50_102_98_101_49"
    # 解析字符串参数并转换为字节数组
    key_bytes = bytes([int(num) for num in key_string.split("_")])
    iv_bytes = bytes([int(num) for num in iv_string.split("_")])
    # 创建 AES 解密器
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    # 解密 base64 编码的数据
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_base64_data))
    return base64.b64encode(decrypted_data).decode('utf-8')


# url转base64
def urlToBase64(url):
    # 发送请求获取图片二进制数据
    response = requests.get(url)
    image_data = response.content

    # 将图片二进制数据转换为 base64 编码的字符串
    base64_str = base64.b64encode(image_data).decode('utf-8')
    return decrypt_image(base64_str)

# 以下是测试数据
# print(urlToBase64('https://pic.eqiykt.cn/upload/upload/20240430/2024043019495876725.png'))
