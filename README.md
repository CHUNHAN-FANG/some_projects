## 图像识别应用
**艾灸穴位图像识别**<br>
实现脸部部分穴位（阳白穴、鱼腰穴、印堂穴、攒竹穴、丝竹穴、承泣穴、太阳穴、迎香穴、水沟穴、兑端穴、承浆穴、地仓穴、颊车穴、大迎穴等）动态识别，及手部部分穴位（十宣穴、劳宫穴、少府学、鱼际穴等）识别。
[成果报告](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/02d4d280-bfed-481d-a5b1-4ee6f7ba3016/%E6%96%B9%E7%BA%AF%E6%B6%B5_%E5%9F%BA%E4%BA%8E%E5%9B%BE%E5%83%8F%E8%AF%86%E5%88%AB%E6%8A%80%E6%9C%AF%E7%9A%84%E8%89%BE%E7%81%B8%E6%99%BA%E8%83%BD%E5%8F%96%E7%A9%B4.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220521T150742Z&X-Amz-Expires=86400&X-Amz-Signature=45ed3e344b3e90c21340329b02af9734c22f97719a0eedd36a5cc1736b93c417&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E6%2596%25B9%25E7%25BA%25AF%25E6%25B6%25B5_%25E5%259F%25BA%25E4%25BA%258E%25E5%259B%25BE%25E5%2583%258F%25E8%25AF%2586%25E5%2588%25AB%25E6%258A%2580%25E6%259C%25AF%25E7%259A%2584%25E8%2589%25BE%25E7%2581%25B8%25E6%2599%25BA%25E8%2583%25BD%25E5%258F%2596%25E7%25A9%25B4.pdf%22&x-id=GetObject)

**百度图像识别API调取**<br>
首先登录[百度智能云官网](https://cloud.baidu.com/)，进入控制台总览“产品服务-人工智能-图像识别”，在应用列表中创建新应用，生成AppID, API Key, Secret Key（调取接口创建客户端时的必要参数）；
python可实现本地图片（或网络图片）批量读取调用接口、返回识别结果。
