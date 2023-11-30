from flask import Flask, render_template
from flaskext.mysql import MySQL


app=Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='tpocrud'
mysql.init_app(app)




@app.route("/")

def Login():
    sql = "INSERT INTO `tpocrud`.`loginsystem` (`ID`, `User`, `Password`, `Email`, `Rank`) VALUES (NULL, 'Gabriel', 'Mariano', 'mariano.gabriel.persano@gmail.com', '1');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template("Login.html")


if __name__=="__main__":
    app.run(debug=True)

