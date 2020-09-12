OPENING = """<!DOCTYPE html>
<html>
<head>
<style>
table, td {
  border: 1px solid black;
}

table {
  white-space: pre;
  border-collapse: collapse;
  width: 100%;
}

th {
  height: 50px;
}
</style>
</head>
<body>

<h2>Translating Sentences</h2>
<p>LANGUAGE - left is original, right is translated:</p>
<table>
"""

CODE_TITLE = """<tr>
    <th>ENTER_FUNCTION_NAME</th>
    <th></th>
  </tr>"""

CODE = """<tr>
    <td>origin code: <br><br> ORIGIN_CODE</td>
    <td>translated code: <br><br> TRANSLATED_CODE</td>
  </tr>"""

ENDING = """</table>
</body>
</html>
"""