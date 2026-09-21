# This module contains the information about the products
products=[{"product_name":"PC","          price_per_product":114999," stock_Qty":17,"     category":" Electronics"},
          {"product_name":"Laptop","      price_per_product":107999," stock_Qty":23,"     category":" Electronics"},
          {"product_name":"Water Pump","  price_per_product":2499,"   stock_Qty":52,"     category":" Hardware"},
          {"product_name":"Note Book","   price_per_product":50,"     stock_Qty":48,"     category":" Stationary"},
          {"product_name":"Paracetamol"," price_per_product":30,"     stock_Qty":103,"    category":" Medical"},
          {"product_name":"Calpol","      price_per_product":8,"      stock_Qty":79,"     category":" Medical"}]

def get_products():
    print("Available Stock: ")
    for i in products:
        print(i)
    return i