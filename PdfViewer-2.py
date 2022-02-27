import os
import argparse
import tkPDFViewer as PDFViewer
from tkinter import *


def parse_args():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-p', '--path', dest='path', type=str, help="Enter the path of the pdf file",
                        default="C:\\Users\\KING\\Downloads\\151471.pdf")
    parser.add_argument('-t', '--title', dest='title', type=str, help="Enter the title", nargs='?', default="PDFViewer")
    parser.add_argument('-x', '--width', dest='width', type=int, help="Enter the width", nargs='?', default=650)
    parser.add_argument('-y', '--height', dest='height', type=int, help="Enter the height", nargs='?', default=750)
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    # print("## Command Arguments #################################################")
    # print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    # print("######################################################################")
    return args


def center_window(root, width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


global v2
v2 = None


def main():
    args = parse_args()
    # if not os.path.isfile(args['path']):
    #     print('path is not file')
    #     exit()
    root = Tk()
    root.title("PDFViewer")
    root.focus()
    center_window(root, args['width'], args['height'])
    v1 = PDFViewer.ShowPdf()
    v2 = v1.pdf_view(root, pdf_location=args['path'], width=100, height=100, zoomDPI=72)
    v2.pack()

    def handle_configure(event):
        print("window geometry:\n" + root.geometry())
        #v1 = PDFViewer.ShowPdf()
        #v2 = v1.pdf_view(root, pdf_location=args['path'], width=300, height=100, zoomDPI=72 * 3)
        #root.update()

    root.bind("<Configure>", handle_configure(root))
    # root.state('zoomed')
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
