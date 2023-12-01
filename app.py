from flask import Flask, render_template, request
from flaskext.mysql import MySQL


app=Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='tpocrud'
mysql.init_app(app)




@app.route("/")

def index():
    return render_template("index.html")

@app.route("/discografia")
def discografia():
   return render_template("discografia.html")

@app.route("/historia")
def historia():
   return render_template("historia.html")

@app.route("/nosotros")
def nosotros():
    # sql = "INSERT INTO `tpocrud`.`msglist` (`ID`, `NombreyApellido`, `Email`, `Mensaje`) VALUES (NULL, 'Roberto Carlos', 'Robert@gmail.com', 'AGUANTE RAMMSTEIN LOCO')"
    # conn = mysql.connect()
    # cursor = conn.cursor()
    # cursor.execute(sql)
    # conn.commit()
    return render_template("nosotros.html")

# /Store de NOSOTROS
@app.route("/storenosotros",methods=["POST"])
def storage():
    NombreyApellido = request.form["fnombre"]
    Email = request.form["fcorreo"]
    Mensaje = request.form["fmensaje"]
    datos = (NombreyApellido,Email,Mensaje)

    sql = "INSERT INTO tpocrud.msglist (ID, NombreyApellido, Email, Mensaje) VALUES (NULL, %s, %s, %s)";
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template("nosotros.html")
# /Store de NOSOTROS
  

@app.route("/login")
def Login():
    sql = "INSERT INTO `tpocrud`.`loginsystem` (`ID`, `User`, `Password`, `Email`, `Rank`) VALUES (NULL, 'Gabriel', 'Mariano', 'mariano.gabriel.persano@gmail.com', '1');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template("Login.html")


@app.route("/adminnosotros")
def AdminNosotros():

    return render_template("adminnosotros.html")



if __name__=="__main__":
    app.run(debug=True)

