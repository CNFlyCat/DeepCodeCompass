import tkinter as tk
from tkinter import ttk
from chat_display import ChatDisplay
from message_input import MessageInput


class MainWindow:
    def __init__(self):
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("AI Chat Application")
        self.root.geometry("800x600")

        # 设置窗口最小尺寸
        self.root.minsize(600, 400)

        # 创建主框架，使用网格布局
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # 配置主窗口的网格权重
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # 创建主要内容框架（不再需要左右分栏）
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.grid(row=0, column=0, sticky="nsew")

        # 配置main_frame的网格权重
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # 初始化组件
        self.init_components()

    def init_components(self):
        """初始化各个组件"""
        # 创建聊天显示区域
        self.chat_display = ChatDisplay(self.content_frame)
        self.chat_display.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # 创建消息输入区域
        self.message_input = MessageInput(self.content_frame, self.send_message)
        self.message_input.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        # 配置content_frame的网格权重
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(1, weight=0)
        self.content_frame.grid_columnconfigure(0, weight=1)

    def send_message(self, message):
        """处理发送消息的回调函数"""
        self.chat_display.add_message(message, "User")

    def run(self):
        """运行应用程序"""
        self.root.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()