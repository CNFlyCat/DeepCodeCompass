import tkinter as tk
from tkinter import ttk


class MessageInput(ttk.Frame):
    def __init__(self, parent, send_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # 创建输入框和发送按钮的容器
        self.input_container = tk.Frame(self)
        self.input_container.pack(fill='x', expand=True)

        # 创建带边框的框架来包装文本输入框
        self.input_frame = tk.Frame(
            self.input_container,
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#E0E0E0"
        )
        self.input_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        # 创建文本输入框
        self.input_field = tk.Text(
            self.input_frame,
            height=3,
            width=40,
            wrap=tk.WORD,
            font=('Arial', 11),
            bd=0,
            padx=10,
            pady=10,
            background="#FFFFFF",
            selectbackground="#A6D5FA"
        )
        self.input_field.pack(fill='both', expand=True)

        # 创建自定义样式的发送按钮
        self.send_button = tk.Button(
            self.input_container,
            text="发送",
            font=('Arial', 11, 'bold'),
            command=self._on_send,
            bg='#2B5278',  # 蓝色背景
            fg='white',  # 白色文字
            width=10,
            height=2,
            relief='flat',
            cursor='hand2'  # 鼠标悬停时显示手型
        )
        self.send_button.pack(side='right', pady=5)

        # 按钮悬停效果
        self.send_button.bind('<Enter>', self._on_enter)
        self.send_button.bind('<Leave>', self._on_leave)

        # 存储回调函数
        self.send_callback = send_callback

        # 绑定回车键发送消息
        self.input_field.bind("<Return>", self._handle_return)

    def _on_enter(self, e):
        """鼠标进入按钮时的效果"""
        self.send_button['bg'] = '#1D3557'  # 深蓝色

    def _on_leave(self, e):
        """鼠标离开按钮时的效果"""
        self.send_button['bg'] = '#2B5278'  # 恢复原来的蓝色

    def _handle_return(self, event):
        """处理回车键事件"""
        if not event.state & 0x1:  # 如果没有按下Shift键
            self._on_send()
            return 'break'

    def _on_send(self):
        """发送消息的处理函数"""
        message = self.input_field.get("1.0", tk.END).strip()
        if message and self.send_callback:
            self.send_callback(message)
            self.clear_input()

    def clear_input(self):
        """清空输入框"""
        self.input_field.delete("1.0", tk.END)

    def get_input(self):
        """获取输入框内容"""
        return self.input_field.get("1.0", tk.END).strip()