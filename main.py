import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from PyPDF2 import PdfMerger

window= tk.Tk()
window.title("PDF 병합기")
window.resizable(False,False)
window.wm_attributes("-topmost", 1)
window.geometry("+200+100")

global selectedFloder
selectedFloder=[]
def select_folder():
    folder_selected = filedialog.askdirectory()
    selectedFloder.append("0"+folder_selected)
    if(folder_selected in selectedFloder and folder_selected):
        tkinter.messagebox.showinfo("알림",folder_selected+" 가 정상적으로 추가되었습니다.")


def merge(output_filename="merged.pdf"):

    global selectedFloder
    if(len(selectedFloder)==0):
        tkinter.messagebox.showinfo("알림","병합할 폴더가 선택되지 않았습니다.")
        return

    merger = PdfMerger()
    for i in selectedFloder:
        pdf_files = [f for f in os.listdir(i) if f.lower().endswith(".pdf")]
        pdf_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))) if any(c.isdigit() for c in f) else float('inf'))

        for pdf in pdf_files:
            pdf_path = os.path.join(i, pdf)
            merger.append(pdf_path)

        output_path = os.path.join(selectedFloder[0], output_filename)
        merger.write(output_path)

    
    merger.close()
    
    tkinter.messagebox.showinfo("알림",output_path+" 에 병합 파일이 저장되었습니다.")



# 폴더 선택 컴포넌트
select_folder_button = tk.Button(window, text="폴더 선택", command=lambda: select_folder(), width=10, height=5)
select_folder_button.pack(side="left", padx=10)  # 왼쪽에 배치

# 소개 컴포넌트
info = tk.Label(window, text="PDF MERGER", font=("Arial", 12))
info.pack(side="left", padx=10)  # 왼쪽에 배치되도록 설정

# 변환 버튼 컴포넌트
merge_start_button = tk.Button(window, text="변환", command=lambda: merge, width=10, height=5)
merge_start_button.pack(side="left", padx=10)  # 왼쪽에 배치

window.mainloop()


window.mainloop()