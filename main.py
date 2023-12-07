from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format= "A4")
pdf.set_auto_page_break(margin=0, auto=False)
df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
        pdf.set_text_color(100, 100, 100)
        pdf.line(10, 21, 200, 21)


        #set the footer

        pdf.ln(265)
        pdf.set_font(family='Times', size=8, style='I')
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")


pdf.output("output.pdf")