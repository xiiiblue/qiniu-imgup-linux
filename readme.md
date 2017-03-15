# qiniu-imgup-linux

## 简介
qiniu-imgup-linux是一个Linux系统下的七牛云图片上传工具，目标是简化MarkDown写作中的贴图的繁琐步骤。  
qiniu-imgup-linux可以快速将剪贴板中的图片上传至七牛云，并自动粘帖至编辑器。    
适用人群：使用七牛云做为图床的MarkDown编写者。  
平台：Linux （Ubuntu16.04测试通过）

请注意：Linux版本的整体思路及部分代码来自 博客 [77695的自留地](http://nfeng.cc/2016/07/19/markdown-img-tool/) ，主要用于学习及练手使用，如造成侵权，请及时联系我删除。  

另有Mac版本，请移步：[https://github.com/xiiiblue/qiniu-imgup-linux.git](https://github.com/xiiiblue/qiniu-imgup-linux.git)


## 使用方法
在编写MarkDown文档时，如果使用七牛云做图床，插入一张图片需要以下几个繁琐的步骤：
1. 截图
2. 保存为文件
3. 打开浏览器，在七牛云后台上传图片
4. 复制图片的HTTP URL
5. 在编辑器中将URL拼接为MarkDown的链接格式
6. 粘帖链接

qiniu-imgup将整个操作简化为了2个快捷键操作：
- `alt+shift+s`  调用`simg`截图
- `alt+shift+u`  调用`uimg`上传并自动粘帖

## 安装依赖及工具
```
sudo pip3 install qiniu
sudo apt-get install shutter
sudo apt-get install xclip
sudo apt-get install parcellite
sudo apt-get install xdotool
sudo apt-get install libnotify-bin
```

## 应用配置
1. 将程序目录拷贝至/opt/qimg下
2. 设置环境变量 `export PATH=/opt/qimg:$PATH`
3. 在Shutter设置中，将图片自动保存位置设为`/tmp/snap_shutter`
4. 在System Setting - Keyboard中，设置快捷键分别指向`simg`截图和`uimg`上传