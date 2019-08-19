import pandas as pd
import datetime
import csv

orders = pd.read_csv("orders.csv", encoding = "latin-1")
no_notes = pd.DataFrame(columns = ("order_id", "status", "market", "pickup_location", "delivery_date", "vendor", "customer", "product", "amount", "price", "note", "subtotal", "removed"))
yes_notes = pd.DataFrame(columns = ("order_id", "status", "market", "pickup_location", "delivery_date", "vendor", "customer", "product", "amount", "price", "note", "subtotal", "removed"))

# TOTAL
array1 = ['Crave', 'NEMIC', 'eMoney', 'Verizon 12:10pm', 'Virgin Pulse 12:00pm', 'Brown Physicians 375 Wamp. Trl.', 'Brown Physicians 110 Elm St.', 'NHPRI 12:15pm', 'Endoscopy Center 62 Amaral St']
orders1= orders.loc[orders['market'].isin(array1)]
total_groupby_vendor1 = orders1.groupby("vendor")
vendors1 = []

for k0, item0 in total_groupby_vendor1:
	vendors1.append(k0)

for i in range(len(orders)):
	if pd.isnull(orders["note"][i]):
		no_notes = no_notes.append(orders.iloc[i])
	else:
		yes_notes = yes_notes.append(orders.iloc[i])

# NO NOTE
no_notes1 = no_notes.loc[no_notes['market'].isin(array1)]
nn_groupby_vendor1 = no_notes1.groupby("vendor")

nn_vendors1 = []
nn_orders_byVendor1 = []
nn_total_amount1 = []

#for k1, item1 in nn_groupby_vendor1:
	#nn_vendors1.append(k1)
	#nn_orders_byVendor1.append(item1.reset_index(drop=True))
	#nn_total_amount1.append(sum(item1["amount"]))

for k1, item1 in nn_groupby_vendor1:
	nn_vendors1.append(k1)
	nn_groupby_product1 = item1.groupby("product")
	products = []
	amounts = []
	for k2, item2 in nn_groupby_product1:
		products.append(k2)
		amounts.append(sum(item2["amount"]))
	nn_total_amount1.append(sum(amounts))
	nn_product_amt_map1 = dict(zip(products, amounts))
	nn_orders_byVendor1.append(nn_product_amt_map1)

# YES NOTE
yes_notes1 = yes_notes.loc[yes_notes['market'].isin(array1)]
yn_groupby_vendor1 = yes_notes1.groupby("vendor")

yn_vendors1 = []
yn_orders_byVendor1 = []
yn_total_amount1 = []

for k3, item3 in yn_groupby_vendor1:
	yn_vendors1.append(k3)
	yn_orders_byVendor1.append(item3.reset_index(drop=True))
	yn_total_amount1.append(sum(item3["amount"]))

today = datetime.datetime.now().strftime("%Y-%m-%d")

for i in range(len(vendors1)):
	ticket = open(str(vendors1[i]) + str(1130) + ".txt", "w+")
	ticket.write("!!! Please Scroll ALL THE WAY down !!!\n\n")
	ticket.write(str(vendors1[i]))
	ticket.write("\n\n")
	ticket.write(str(today) + "\n")
	ticket.write("*Please REPLY YES to confirm this order\n")
	ticket.write("*Our driver will be there by 11:30 a.m. !!!\n\n")
	tot = 0
	if vendors1[i] in nn_vendors1:
		tot += int(nn_total_amount1[nn_vendors1.index(vendors1[i])])
	if vendors1[i] in yn_vendors1:
		tot += int(yn_total_amount1[yn_vendors1.index(vendors1[i])])
	ticket.write(str(tot) + "  <- Total # of Order\n")
	ticket.write("-------------------------------------------------\n")
	ticket.write("#     Main Menu $\n")
	if vendors1[i] in yn_vendors1:
		index = yn_vendors1.index(vendors1[i])
		for j in range(len(yn_orders_byVendor1[index])):
			ticket.write(str(int(yn_orders_byVendor1[index]["amount"][j]))+ '   ' + str(yn_orders_byVendor1[index]["product"][j]) + "\n")
			ticket.write(" NOTE:    " + str(yn_orders_byVendor1[index]["note"][j]) + "\n\n")
	if vendors1[i] in nn_vendors1:
		index = nn_vendors1.index(vendors1[i])
		for key in nn_orders_byVendor1[index]:
			if int(nn_orders_byVendor1[index][key]) > 1:
				for i in range(int(nn_orders_byVendor1[index][key])):
					ticket.write("1   " + str(key) + "\n\n")
			else:
				ticket.write("1   " + str(key) + "\n\n")




array2 = ['Verizon 12:55pm', 'Virgin Pulse 12:45pm', 'NHPRI 1:00pm']
orders2= orders.loc[orders['market'].isin(array2)]
total_groupby_vendor2 = orders2.groupby("vendor")
vendors2 = []

for k0, item0 in total_groupby_vendor2:
	vendors2.append(k0)


# NO NOTE
no_notes2 = no_notes.loc[no_notes['market'].isin(array2)]
nn_groupby_vendor2 = no_notes2.groupby("vendor")

nn_vendors2 = []
nn_orders_byVendor2 = []
nn_total_amount2 = []

#for k4, item4 in nn_groupby_vendor2:
	#nn_vendors2.append(k4)
	#nn_orders_byVendor2.append(item4.reset_index(drop=True))
	#nn_total_amount2.append(sum(item4["amount"]))

for k4, item4 in nn_groupby_vendor2:
	nn_vendors2.append(k4)
	nn_groupby_product2 = item4.groupby("product")
	products = []
	amounts = []
	for k5, item5 in nn_groupby_product2:
		products.append(k5)
		amounts.append(sum(item5["amount"]))
	nn_total_amount2.append(sum(amounts))
	nn_product_amt_map2 = dict(zip(products, amounts))
	nn_orders_byVendor2.append(nn_product_amt_map2)

# YES NOTE
yes_notes2 = yes_notes.loc[yes_notes['market'].isin(array2)]
yn_groupby_vendor2 = yes_notes2.groupby("vendor")

yn_vendors2 = []
yn_orders_byVendor2 = []
yn_total_amount2 = []

for k6, item6 in yn_groupby_vendor2:
	yn_vendors2.append(k6)
	yn_orders_byVendor2.append(item6.reset_index(drop=True))
	yn_total_amount2.append(sum(item6["amount"]))

today = datetime.datetime.now().strftime("%Y-%m-%d")

for g in range(len(vendors2)):
	ticket = open(str(vendors2[g]) + str(1210) + ".txt", "w+")
	ticket.write("!!! Please Scroll ALL THE WAY down !!!\n\n")
	ticket.write(str(vendors2[g]))
	ticket.write("\n\n")
	ticket.write(str(today) + "\n")
	ticket.write("*Please REPLY YES to confirm this order\n")
	ticket.write("*Our driver will be there by 12:10 p.m. !!!\n\n")
	tot = 0
	if vendors2[g] in nn_vendors2:
		tot += int(nn_total_amount2[nn_vendors2.index(vendors2[g])])
	if vendors2[g] in yn_vendors2:
		tot += int(yn_total_amount2[yn_vendors2.index(vendors2[g])])
	ticket.write(str(tot) + "  <- Total # of Order\n")
	ticket.write("-------------------------------------------------\n")
	ticket.write("#     Main Menu $\n")
	if vendors2[g] in yn_vendors2:
		index = yn_vendors2.index(vendors2[g])
		for h in range(len(yn_orders_byVendor2[index])):
			ticket.write(str(int(yn_orders_byVendor2[index]["amount"][h]))+ '   ' + str(yn_orders_byVendor2[index]["product"][h]) + "\n")
			ticket.write(" NOTE:    " + str(yn_orders_byVendor2[index]["note"][h]) + "\n\n")
	if vendors2[g] in nn_vendors2:
		index = nn_vendors2.index(vendors2[g])
		for key in nn_orders_byVendor2[index]:
			if int(nn_orders_byVendor2[index][key]) > 1:
				for i in range(int(nn_orders_byVendor2[index][key])):
					ticket.write("1   " + str(key) + "\n\n")
			else:
				ticket.write("1   " + str(key) + "\n\n")



"""
!!! Please Scroll ALL THE WAY down !!!	

PieZoni's	

Monday, March 18, 	
*Please REPLY to confirm this order	
*Our driver will be there by 12:00 p.m. !!!	

1	← Total # of Order	
---------------------------------------------------------------------------------------------		
#	Main Menu	$

1	Steak Tip Salad
"""

orders.sort_values(['market','vendor'], inplace=True)

orders.to_csv("orderstotal.csv")