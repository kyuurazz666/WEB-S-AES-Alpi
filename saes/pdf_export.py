from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


class PDFExporter:

    @staticmethod
    def export(
        filename,
        mode,
        input_text,
        key_text,
        output_text,
        key_schedule,
        logs
    ):

        doc = SimpleDocTemplate(filename)

        story = []

        story.append(
            Paragraph("<b>SIMPLIFIED AES REPORT</b>", styles["Title"])
        )

        story.append(
            Paragraph(f"Mode : {mode}", styles["Normal"])
        )

        story.append(
            Paragraph(f"Input : {input_text}", styles["Normal"])
        )

        story.append(
            Paragraph(f"Master Key : {key_text}", styles["Normal"])
        )

        story.append(
            Paragraph(f"Output : {output_text}", styles["Normal"])
        )

        story.append(
            Paragraph("<br/><b>ROUND KEYS</b>", styles["Heading2"])
        )

        for name, value in key_schedule["round_keys"].items():

            story.append(

                Paragraph(

                    f"{name} = {value}",

                    styles["Normal"]

                )

            )

        story.append(

            Paragraph(

                "<br/><b>KEY EXPANSION</b>",

                styles["Heading2"]

            )

        )

        for name, value in key_schedule["words"].items():

            story.append(

                Paragraph(

                    f"{name} = {value}",

                    styles["Normal"]

                )

            )

        story.append(

            Paragraph(

                "<br/><b>PROCESS</b>",

                styles["Heading2"]

            )

        )

        for step in logs:

            story.append(

                Paragraph(

                    f"<b>{step['title']}</b>",

                    styles["Heading3"]

                )

            )

            story.append(

                Paragraph(

                    f"Binary : {step['binary']}",

                    styles["Normal"]

                )

            )

            story.append(

                Paragraph(

                    f"Hex : {step['hex']}",

                    styles["Normal"]

                )

            )

            story.append(

                Paragraph("<br/>", styles["Normal"])

            )

        doc.build(story)