def generar_tabla_tokens_html(data):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tabla de Tokens</title>
        <style>
            table {
                width: 80%;
                margin: 0 auto;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #000;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <table>
            <tr>
                <th>Tipo</th>
                <th>Lexema</th>
                <th>Fila</th>
                <th>Columna</th>
            </tr>
    """

    for fila in data:
        html_content += f"""
            <tr>
                <td>{fila['tipo']}</td>
                <td>{fila['lexema']}</td>
                <td>{fila['fila']}</td>
                <td>{fila['columna']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """
    
    return html_content

def generar_tabla_errores_html(data):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tabla de Errores</title>
        <style>
            table {
                width: 80%;
                margin: 0 auto;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #000;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <table>
            <tr>
                <th>Tipo</th>
                <th>Error</th>
                <th>Fila</th>
                <th>Columna</th>
            </tr>
    """

    for fila in data:
        html_content += f"""
            <tr>
                <td>{fila['tipo']}</td>
                <td>{fila['error']}</td>
                <td>{fila['fila']}</td>
                <td>{fila['columna']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """
    
    return html_content



def generar_tabla_datos_html(claves, registros):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tabla de Registros</title>
        <style>
            table {
                width: 80%;
                margin: 0 auto;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #000;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <table>
        <tr>
            """
    for columna in claves:
        html_content += f"<th>{columna}</th>"

    html_content += "</tr>"

    for row in registros:
        html_content += "<tr>"
        for value in row:
            html_content += f"<td>{value}</td>"
        html_content += "</tr>"

    html_content += """
        </table>
    </body>
    </html>
    """
    
    return html_content