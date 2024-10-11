# PictureFetcher 

## 项目概述

**PictureFetcher** 是一个自动抓取图片的工具，通过百度图片搜索，根据用户输入的关键词获取图片，并将图片保存到本地。程序以用户指定的关键词命名文件夹并存储相应数量的图片。

---

## 目录

- [项目概述](#项目概述)
- [环境配置](#环境配置)
  - [依赖项](#依赖项)
  - [Python 环境](#python-环境)
  - [安装步骤](#安装步骤)
- [使用方法](#使用方法)
- [错误处理](#错误处理)
- [许可协议](#许可协议)

---

## 环境配置

### 依赖项

运行此项目需要以下主要依赖：

- `beautifulsoup4` >= 4.10.0
- `colorama` >= 0.4.4
- `requests` >= 2.25.1
- `tqdm` >= 4.62.0

### Python 环境

建议使用 **Python 3.8** 或更高版本。

### 安装步骤

1. 克隆项目代码：

    ```
    git clone https://github.com/your_username/PictureFetcher2.git
    cd PictureFetcher2
    ```

2. 使用虚拟环境（推荐）：

    ```
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. 安装项目依赖：

    ```
    pip install -r requirements.txt
    ```

---

## 使用方法

1. 运行 `main.py` 文件：

    ```
    python main.py
    ```

2. 按提示输入关键词和图片数量，例如：

    ```
    请输入关键词: 小狗
    请输入图片数量: 20
    ```

3. 图片将保存到项目根目录下的 `fetch_小狗/` 文件夹中。

---

## 错误处理

- **网络异常处理**: 若遇到网络请求错误，程序会捕获 `requests` 异常并显示友好提示。

    ```python
    except requests.RequestException as e:
        print(colorama.Fore.RED+f"请求错误: {e}"+colorama.Style.RESET_ALL)
    ```

- **空图片列表处理**: 若未能抓取到图片，程序将自动尝试抓取下一页，确保获取到用户需要的图片数量。

---

感谢您使用此程序！我们期待您的反馈！
