# print("=======LAPTOP ON SALE=======")
#
# print("1.Dell(Rs:20000) 2.Toshiva(Rs:30000) 3.Mac(Rs:40000")
# dell_price=20000
# toshiva_price=30000
# mac_price=40000
# total_price=0
# option=int(input("select any option:"))
#
# if option==1:
#     qt=int(input('enter a quantity:'))
#     total_price+=dell_price*qt
# elif option==2:
#     qt = int(input('enter a quantity:'))
#     total_price += toshiva_price*qt
# elif option==3:
#     qt = int(input('enter a quantity:'))
#     total_price += mac_price*qt
# else :
#     exit()
#
# print("1.Home Delivery(Rs 1000) 2.Selfservive(free)")
#
# delivery_option=int(input("enter a delivery:"))
# home_price=0
# if delivery_option==1:
#     home_price+=1000
# elif delivery_option==2:
#     home_price+=0
# else:
#     exit()
#
# print("1.Plastic Bag(Rs 1000) 2.Bag(Rs 2000) 3.Git Box(Rs5000)")
# plasticbag_price=0
# bag_price=0
# gitbox_price=0
# package_option=int(input("enter a option:"))
# if package_option==1:
#     plasticbag_price+=1000
# elif package_option==2:
#     bag_price+=2000
# elif package_option==3:
#     gitbox_price+=5000
# else:
#     exit()
# print("1.13%tax(with in ktm) 2.Outofvalley(free)")
# tat=int(input("enter a location:"))
# tax_amount=0
# if tat==1:
#     tax_amount+=total_price*0.13
# else:
#     exit()
# grand_total=total_price+tax_amount+gitbox_price+bag_price+plasticbag_price+home_price
#
# print('=======Result=======')
# print(f'Total amount={total_price}')
# print(f'Tax amount={tax_amount}')
# print("======FINAL AMOUNT======")
# print(f'Grand total={grand_total}')

