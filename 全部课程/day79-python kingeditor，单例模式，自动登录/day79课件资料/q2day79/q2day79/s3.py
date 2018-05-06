# __author:  Administrator
# date:  2017/2/9
import requests

response = requests.get(
    url='https://i.cnblogs.com/EditDiary.aspx',
    cookies={'.CNBlogsCookie': '8F3B9333580034B7CEA8BFE4DCA62D6600D965470C3A4EC3C03194975E4EF2FAC74AF4A7271FA5312D92BE2D701FB2267EF2E1F10B19B489EE5B4C6748DDC96D98AC74A2D9DE44CAE68756F6ABD2BD2A3EA5916D'},
    # cert='证书文件',
    # verify=True
)
print(response.text)


