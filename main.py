import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from PyPDF2 import PdfMerger

window= tk.Tk()
window.title("PDF 병합기")
window.resizable(False,False)
window.geometry("200x80")
window.wm_attributes("-topmost", 1)

global selectedFloder
selectedFloder=[]
def select_folder():
    folder_selected = filedialog.askdirectory()
    selectedFloder.append(folder_selected)
    tkinter.messagebox.showinfo("알림",folder_selected+" 가 정상적으로 추가되었습니다.")


def merge_pdfs_in_folder(folder_path, output_filename="merged.pdf"):
    merger = PdfMerger()
    global selectedFloder
    for i in range(len(selectedFloder)):
        pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
        pdf_files.sort()  # 파일명을 기준으로 내림차순 정렬

        for pdf in pdf_files:
            pdf_path = os.path.join(folder_path, pdf)
            merger.append(pdf_path)

        output_path = os.path.join(folder_path, output_filename)
        merger.write(output_path)
        select_folder.pop(0)
    
    merger.close()
    
    tkinter.messagebox.showinfo("알림","병합이 완료되었습니다.")


#폴더 선택 컴포넌트
select_folder_button=tk.Button(window,text="폴더 선택",command=lambda:select_folder())
select_folder_button.pack()
#변환 버튼 컴포넌트
merge_start_button=tk.Button(window,text="변환",command=lambda:merge_pdfs_in_folder())
merge_start_button.pack()

window.mainloop()