# 📂 目录遍历器 (Directory Explorer)

[![Release](https://img.shields.io/github/v/release/CNFlyCat/DeepCodeCompass?style=for-the-badge)](https://github.com/CNFlyCat/DeepCodeCompass/releases)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-brightgreen?style=for-the-badge&logo=tkinter&logoColor=white)](https://docs.python.org/3/library/tkinter.html)

**一款简洁易用的图形界面工具，用于快速遍历指定目录，并将目录结构以文本或 JSON 格式导出。**

---

## ✨ 功能特性

*   **可视化目录树**:  以清晰的树状结构展示目录和文件，一目了然。
*   **快捷复制**:  可以直接从输出窗口复制目录文本，拿去询问AI或用在您的演示文档上。
*   **忽略规则**: 支持 `.gitignore` 和自定义 `fileignore.txt` 规则，灵活排除不需要的文件和文件夹。
*   **多种输出格式**:  可选择导出为纯文本 (`.txt`) 或 JSON (`.json`) 格式，满足不同需求。
*   **操作简便**:  直观的图形界面，只需几步即可完成目录遍历和导出。
*   **跨平台**:  基于 Python 和 Tkinter 开发，理论上可在支持 Python 的平台上运行 (已打包为 Windows `.exe` 可执行文件)。

## ⚙️ 使用方法

1.  **下载程序**:  从 [**[发布页面](https://github.com/CNFlyCat/DeepCodeCompass/releases)**]下载最新版本的 `.exe` 文件。

2.  **运行程序**:  双击下载的 `.exe` 文件 `DirectoryExplorer.exe` 启动程序。

3.  **选择项目目录**:
    *   在 "项目目录" 输入框中，手动输入要遍历的根目录路径。
    *   或点击 "浏览" 按钮，在弹出的对话框中选择目录。
       
    ![image](https://github.com/user-attachments/assets/43b2ac71-a579-446f-b6ce-72409ecb905d)

4.  **选择忽略文件 (可选)**:
    *   如果你有 `.gitignore` 或 `fileignore.txt` 类型的忽略规则文件，可以在 "忽略文件" 输入框中指定文件路径。
    *   点击 "浏览" 按钮选择忽略文件。
    *   **留空则不使用忽略规则。**

    ![image](https://github.com/user-attachments/assets/ba277897-4f3e-4309-a5ed-a63aed3a63bf)

5.  **选择导出格式**:
    *   在 "导出格式" 下拉菜单中，选择 **TXT** 或 **JSON**。
    *   **TXT**:  导出为类似 `tree` 命令的纯文本树状结构。
    *   **JSON**:  导出为结构化的 JSON 数据。

   ![image](https://github.com/user-attachments/assets/528e3b12-7a61-4b36-8f07-b41cded5a72a)

6.  **开始遍历**:  点击 "开始遍历" 按钮，程序将开始遍历目录，并在下方的文本框中显示目录结构。

7.  **保存文件**:
    *   点击 "保存文件" 按钮。
    *   在弹出的目录选择对话框中，选择要保存文件的位置。
    *   程序将根据你选择的导出格式，将目录结构保存为 `.txt` 或 `.json` 文件。
    *   保存成功或失败，都会有弹窗提示。


## 📦 安装 (对于开发者或需要源码运行的用户)

如果你需要从源代码运行或修改程序，请确保你的系统已安装 Python 3.x 和 `pip`。

1.  **克隆仓库** (如果你是从代码仓库获取的):
    ```bash
    git clone [你的仓库地址]
    cd [项目目录]
    ```

2.  **安装依赖** (本项目没有额外的第三方依赖，Tkinter 是 Python 标准库):
    ```bash
    # 本项目无额外依赖，无需安装
    ```

3.  **运行程序**:
    ```bash
    python main.py
    ```

## 📂 输出格式示例

### TXT 文本格式

├── src
│ ├── core
│ │ ├── directorytree.py
│ │ ├── ignorefilereader.py
│ │ ├── jsonwriter.py
│ │ └── texttreewriter.py
│ ├── gui
│ │ └── pycache
│ └── main.py
├── README.md
└── FileDirectory.json 

![image](https://github.com/user-attachments/assets/2da71d0b-0d81-4d55-ac52-c2a07af0042b)

