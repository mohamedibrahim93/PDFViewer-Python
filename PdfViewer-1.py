# import modules
import tkinter as tk
import tkPDFViewer as pdf
import argparse
import sys
import os
from PIL import ImageTk, Image

# set global variable v2
global v2, frame_pdf, args, zoomDPI, zoomDPIDefault
v2 = None
zoomDPIDefault = 72


def zoomIn():
    try:
        global zoomDPI, v2, args
        zoomDPI = int(zoomDPI * 1.5)
        if v2:
            v2.destroy()
        v1 = pdf.ShowPdf()
        v1.img_object_li.clear()
        v2 = v1.pdf_view(frame_pdf, pdf_location=f"{args['path']}", zoomDPI=zoomDPI)
        v2.pack()
    except:
        pass


def zoomOut():
    try:
        global zoomDPI, v2, args
        zoomDPI = int(zoomDPI * 0.5)
        if v2:
            v2.destroy()
        v1 = pdf.ShowPdf()
        v1.img_object_li.clear()
        v2 = v1.pdf_view(frame_pdf, pdf_location=f"{args['path']}", zoomDPI=zoomDPI)
        v2.pack()
    except:
        pass


def zoomRestore():
    try:
        global zoomDPI, zoomDPIDefault, v2, args
        zoomDPI = zoomDPIDefault
        if v2:
            v2.destroy()
        v1 = pdf.ShowPdf()
        v1.img_object_li.clear()
        v2 = v1.pdf_view(frame_pdf, pdf_location=f"{args['path']}", zoomDPI=zoomDPI)
        v2.pack()
    except:
        pass


def show_pdf():
    try:
        global v2, args
        if v2:
            v2.destroy()

        v1 = pdf.ShowPdf()
        v1.img_object_li.clear()
        v2 = v1.pdf_view(frame_pdf, pdf_location=f"{args['path']}", zoomDPI=zoomDPIDefault)
        v2.pack()
    except:
        pass


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, 'resources', relative_path)


def center_window(root, width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2) - 50
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def parse_args():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-p', '--path', dest='path', type=str, help="Enter the path of the pdf file",
                        default="C:\\Users\\KING\\Downloads\\151471.pdf")
    parser.add_argument('-t', '--title', dest='title', type=str, help="Enter the title", nargs='?', default="PDFViewer")
    parser.add_argument('-x', '--width', dest='width', type=int, help="Enter the width", nargs='?', default=620)
    parser.add_argument('-y', '--height', dest='height', type=int, help="Enter the height", nargs='?', default=700)
    parser.add_argument('-z', '--zoomDPI', dest='zoomDPI', type=int, help="Enter the zoomDPI", nargs='?', default=72)
    parsed_args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    # print("## Command Arguments #################################################")
    # print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    # print("######################################################################")
    return parsed_args


def main():
    global args, zoomDPI, frame_pdf
    args = parse_args()
    zoomDPI = args['zoomDPI']
    # tkinter root window
    window = tk.Tk()
    # window.geometry('800x600')
    center_window(window, args['width'], args['height'])
    # window.minsize(800, 600)
    window.title(args['title'])
    window.wm_iconbitmap(resource_path('icon.ico'))

    root = tk.PanedWindow(window, orient="horizontal")
    frame_pdf = tk.Frame(root)
    root.add(frame_pdf)
    root.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    # root.bind("<Configure>", handle_configure)

    frame3 = tk.Frame(frame_pdf)
    frame3.pack(side="bottom", fill="both", expand=True)

    # Load button images
    BzoomINimg = Image.open(resource_path("zoomin.png"))
    BzoomINimg = BzoomINimg.resize((40, 40), Image.ANTIALIAS)  # (height, width)
    BzoomINimg = ImageTk.PhotoImage(BzoomINimg)  # convert to PhotoImage

    BzoomRestoreimg = Image.open(resource_path("fullscreen.png"))
    BzoomRestoreimg = BzoomRestoreimg.resize((35, 40), Image.ANTIALIAS)  # (height, width)
    BzoomRestoreimg = ImageTk.PhotoImage(BzoomRestoreimg)  # convert to PhotoImage

    BzoomOUTimg = Image.open(resource_path("zoomout.png"))
    BzoomOUTimg = BzoomOUTimg.resize((40, 40), Image.ANTIALIAS)  # (height, width)
    BzoomOUTimg = ImageTk.PhotoImage(BzoomOUTimg)  # convert to PhotoImage

    # Buttons
    BzoomIN = tk.Button(frame3, text="+", command=zoomIn, image=BzoomINimg)
    BzoomRestore = tk.Button(frame3, text="z", command=zoomRestore, image=BzoomRestoreimg)
    BzoomOUT = tk.Button(frame3, text="-", command=zoomOut, image=BzoomOUTimg)

    frame3.configure(background='black')
    BzoomIN.configure(background='black')
    BzoomRestore.configure(background='black')
    BzoomOUT.configure(background='black')

    # pack buttons
    BzoomIN.pack(side='left', anchor='e', expand=True)
    BzoomRestore.pack(side='left', ipadx=5)
    BzoomOUT.pack(side='right', anchor='w', expand=True)

    show_pdf()

    # %% mainloop
    window.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
