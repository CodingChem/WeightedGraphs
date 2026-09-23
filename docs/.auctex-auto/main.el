;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt" "a4paper")))
   (TeX-run-style-hooks
    "preamble"
    "sections/01_introduction"
    "sections/02_background"
    "sections/03_writing_style"
    "sections/04_figures_tables"
    "sections/05_algorithms_code"
    "sections/06_citations"
    "sections/07_latex_tips"
    "sections/08_common_mistakes"
    "sections/09_checklist")
   (LaTeX-add-bibliographies
    "references"))
 :latex)

