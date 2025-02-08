import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.font as tkfont


class ChatDisplay(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # 创建一个框架来包装聊天区域，用于设置边框效果
        self.chat_frame = tk.Frame(
            self,
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#E0E0E0"
        )
        self.chat_frame.pack(expand=True, fill='both')

        # 创建聊天显示区域
        self.chat_area = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            width=40,
            height=20,
            font=('Arial', 11),
            bd=0,  # 移除边框
            padx=10,
            pady=10,
            background="#FFFFFF",
            selectbackground="#A6D5FA"
        )
        self.chat_area.pack(expand=True, fill='both')

        # 设置聊天区域为只读
        self.chat_area.configure(state='disabled')

        # 圆角效果（通过Canvas实现）
        self.round_corners()

    def round_corners(self):
        """添加圆角效果"""
        radius = 10
        self.chat_frame.configure(bg="#E0E0E0")

    def add_message(self, message, sender="User"):
        """添加新消息到聊天区域"""
        self.chat_area.configure(state='normal')

        # 设置发送者名称的样式
        sender_font = tkfont.Font(family='Arial', size=11, weight='bold')
        self.chat_area.tag_configure('sender', font=sender_font, foreground='#2B5278')

        # 插入发送者名称和消息
        self.chat_area.insert(tk.END, f"{sender}: ", 'sender')
        self.chat_area.insert(tk.END, f"{message}\n\n")

        self.chat_area.configure(state='disabled')
        self.chat_area.see(tk.END)

    def clear_chat(self):
        """清空聊天区域"""
        self.chat_area.configure(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.configure(state='disabled')