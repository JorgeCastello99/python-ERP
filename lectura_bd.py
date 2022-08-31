from ConexionMovimientos import DBConn

class mov : 
    
    def __init__(self):
        self.conexion=DBConn()
#Select todo
    
    def select_all(self):
        query="Select * from movimientos"
        mensaje,cursor=self.conexion.ejecutar(query)
        
        return mensaje,cursor

#Select where producto
    
    def select_wproducto(self,produc):
        query="SELECT * from movimientos Where producto=%f"%produc
      
        return self.conexion.ejecutar(query)

   
#Select where proveedor

    def select_wproveedor(self,clien):
        query="SELECT * from movimientos Where proveedor=%s"%clien
      
        return self.conexion.ejecutar(query)


#Select where cliente

    def select_wcliente(self,prov):
        query="SELECT * from movimientos Where cliente=%s"%prov
    
        return self.conexion.ejecutar(query)

  
#Select where id
    def select_wid(self,id):
        query="SELECT * from movimientos Where id=%d"%id
    
        return self.conexion.ejecutar(query)

    
       
#Select Where factura
        
    def select_wfactura(self,factura):
        query="SELECT * from movimientos Where factura_compra_venta=%s"%factura
      
        return self.conexion.ejecutar(query)

   

#Select where Cantidad

    def select_wcantidad(self,cantidad):
        query="SELECT * from movimientos Where cantidad=%g"%cantidad
      
        return self.conexion.ejecutar(query)

   


#Select where Precio

    def select_wprecio(self,precio):
        query="SELECT * from movimientos Where precio=%f"%precio
       
        return self.conexion.ejecutar(query)

    