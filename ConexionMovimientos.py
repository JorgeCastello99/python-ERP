import mysql.connector

class DBConn:

    def __init__ (self):
        self.db_host='localhost'
        self.db_user='root'
        self.db_pass=''
        self.db_name='erpy'

    def conectar(self):
        """Crea conexion con la base"""
        dbConnect={
            'host':self.db_host,
            'user':self.db_user,
            'passwd':self.db_pass,
            'database':self.db_name
        }
        self.conexion = mysql.connector.connect(**dbConnect)
        
        
    def abrir_cursor(self):
            """Abrir cursor"""
            self.cursor=self.conexion.cursor()
            

    def ejecutar_consulta(self,query,values=''):
        """Ejecutar consultas"""
        if values !='':
           self.cursor.execute(query,values)
        else:
           self.cursor.execute(query)

    def traer_datos(self):
        """Traer todos los registros"""
        self.datos=self.cursor.fetchall()


  

    def ejecutar(self,query,values=''):
        """Compila todos los procesos"""
        #ejecuta toda la clase solo si las propiedades han sido definidas
        
           
        self.conectar()
        self.abrir_cursor()
        self.ejecutar_consulta(query,values)
        self.traer_datos()
       

        return self.datos,self.cursor
        


