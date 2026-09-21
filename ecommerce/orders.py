#Taking orders from customers
import products
import customers
list=[]
def orders():
    for i in products:
        product_name=input("Enter name of the products: ")
        Qty=int(input("Enter Quantity:"))
        list.append(product_name,Qty,customers.id)
    return list


