from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format= "A4")
df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
        pdf.line(10, 21, 200, 21)
pdf.output("output.pdf")