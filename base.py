import sqlite3
con = sqlite3.connect('python.db')
con
cur = con.cursor()
cur
sql1 = """


CREATE TABLE USUARIO (
  ID int NOT NULL PRIMARY KEY,
  NOMBRE varchar(255), -- Adjust varchar size if needed,
  EMAIL varchar(255),
  CLAVE varchar(255), 
  GUIAID int,
  FOREIGN KEY (GUIAID) REFERENCES GUIA(GUIAID)
    ON UPDATE RESTRICT
    ON DELETE RESTRICT
);


"""
sql2 = """
CREATE TABLE GUIA (
  GUIAID int NOT NULL PRIMARY KEY,
  TITULO varchar(255), -- Adjust varchar size if needed
  PRECIO int,
  DESCRIPCION varchar(255), -- Adjust varchar size if needed
  FECHA date,
  AUTOR varchar(255) -- Adjust varchar size if needed
);"""

cur.execute(sql1)
cur.execute(sql2)

