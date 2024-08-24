from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", size=24, style='B')
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 21, 200, 21)

    pdf.ln(265)
    pdf.set_font(family="Times", size=12)
    pdf.cell(w=0, h=0, txt=row["Topic"], align='R')

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=0, h=0, txt=row["Topic"], align='R')

pdf.output("test.pdf")
