# OCCAM1D-GUI

## Introduction

本项目是为了简便反演大地电磁edi数据文件而开发的图形界面。主要包括gnuplot版本和MTpy版本。

安装需求见requirements。

## Pre work

### install packages

```shell
activate MTpy
pip install -r requirements
```

### change errors in MTpy

Go to the occam1d.py, change the 1849-1851 line:`nonposy` -> `nonpostive`

![截屏2022-06-01 14.01.07](README.assets/%E6%88%AA%E5%B1%8F2022-06-01%2014.01.07.png)

![截屏2022-06-08 16.28.24](README.assets/%E6%88%AA%E5%B1%8F2022-06-08%2016.28.24.png)

## how to use it

```shell
cd OCCAM1D-GUI/code
python main.py
```

Then use GUI interface to inverse edi data.

## 参数解释

|    参数名称    |         意义         |            备注             |
| :------------: | :------------------: | :-------------------------: |
|    edi file    |       输入文件       |      目前只支持edi文件      |
|   Layer nums   |       反演层数       |            大于0            |
| Max iterations |     最大迭代次数     |            大于0            |
|      rms       |          /           |              /              |
|      mode      |       反演模式       |              /              |
|     Depth      | 反演数据显示地下深度 |              /              |
|   Plot type    |       绘制类型       | 目前支持gnuplot和matplotlib |
|   Save Path    |       保存路径       |              /              |

## 备注

如果没有选择保存路径，程序会自动保存到code的result文件夹中。
