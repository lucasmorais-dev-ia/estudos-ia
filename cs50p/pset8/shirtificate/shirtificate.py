from fpdf import FPDF


def main():
    name = input("Name: ")

    # pdf = o documento; "P" = em pé (retrato); A4 = 210 × 297 mm
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()

    # título: fonte, tamanho e uma "caixa" de texto
    # cell(0, ...) = largura toda da página; align="C" = centralizado
    pdf.set_font("helvetica", size=40)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C")

    # camiseta: x = distância da borda esquerda; w = largura da imagem
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    # nome em branco, por cima da camiseta
    pdf.set_font_size(24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(130)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    # salva o PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()