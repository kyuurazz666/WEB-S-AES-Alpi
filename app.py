
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import send_file
from saes.validator import Validator
from saes.cipher import SAES
from saes.inv_cipher import InvSAES
from saes.key_expansion import KeyExpansion

app = Flask(__name__)
app.secret_key = "saes_secret_key_unibba"

@app.route("/", methods=["GET", "POST"])
def index():


    if request.method == "GET":

        return render_template("index.html")

    try:

        plaintext = request.form["plaintext"]
        key = request.form["key"]
        operation = request.form["operation"]

        plaintext_value = Validator.parse(plaintext)
        key_value = Validator.parse(key)

        key_schedule = KeyExpansion(key_value)
        key_result = key_schedule.generate()

        if operation == "encrypt":

            engine = SAES(key_value)

            result = engine.encrypt(plaintext_value)

            logs = engine.get_logs()

            session["mode"] = "Encryption"
            session["input_text"] = plaintext
            session["key_text"] = key
            session["output_text"] = format(result, "04X")

            session["round_keys"] = {
                k: format(v, "04X")
                for k, v in key_result["round_keys"].items()
            }

            session["words"] = {
                k: format(v, "02X")
                for k, v in key_result["words"].items()
            }

            session["logs"] = logs

            return render_template(

                "result.html",

                mode="Encryption",

                input_text=plaintext,

                key_text=key,

                output_text=format(result, "04X"),

                logs=logs,

                key_schedule=key_result

            )

        else:

            engine = InvSAES(key_value)

            result = engine.decrypt(plaintext_value)

            logs = engine.get_logs()

            session["mode"] = "Decryption"
            session["input_text"] = plaintext
            session["key_text"] = key
            session["output_text"] = format(result, "04X")

            session["round_keys"] = {
                k: format(v, "04X")
                for k, v in key_result["round_keys"].items()
            }

            session["words"] = {
                k: format(v, "02X")
                for k, v in key_result["words"].items()
            }

            session["logs"] = logs

            return render_template(

                "result.html",

                mode="Decryption",

                input_text=plaintext,

                key_text=key,

                output_text=format(result, "04X"),

                logs=logs,

                key_schedule=key_result

            )

    except Exception as e:

        return render_template(

            "index.html",

            error=str(e)

        )
    
@app.route("/export_pdf")
def export_pdf():

    from saes.pdf_export import PDFExporter

    filename = "SAES_Report.pdf"

    PDFExporter.export(

        filename=filename,

        mode=session["mode"],

        input_text=session["input_text"],

        key_text=session["key_text"],

        output_text=session["output_text"],

        key_schedule={
            "round_keys": session["round_keys"],
            "words": session["words"]
        },

        logs=session["logs"]

    )

    return send_file(
        filename,
        as_attachment=True
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )