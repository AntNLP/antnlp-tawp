#prerequest: texlive, inkscape
#usage:   %python2 latex2emf.py 'latex-formula' output-emf-file
#example: %python2 latex2emf.py '$\\mathcal{M}_\\text{seq}$' M_seq

import sys
import os
import subprocess


latex_begin = '\\begin{document}'
latex_end = '\\end{document}'
latex_preamble = r'''
        \documentclass[20pt, border=2pt]{standalone}
        \usepackage{amsmath}
        \usepackage{xcolor}
        '''

if __name__ == '__main__':
    content = sys.argv[1]
    print content
    tex_string = latex_preamble + latex_begin + content + latex_end

    with open("tmp.tex", 'w') as f:
        f.write(tex_string)

    outputfile = sys.argv[2] + ".emf"
    subprocess.check_output(["pdflatex", "tmp.tex"])
    subprocess.check_output(["pdf2svg", "tmp.pdf", "tmp.svg"])
    subprocess.check_output(["inkscape", "-T", "tmp.svg", "--export-emf", outputfile])
    os.remove("tmp.tex")
    os.remove("tmp.pdf")
    os.remove("tmp.aux")
    os.remove("tmp.log")
    os.remove("tmp.svg")






