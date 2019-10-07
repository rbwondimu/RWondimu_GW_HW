#!/usr/bin/env python3
# -*- coding: utf-8 -*-
shopping = 'y'

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun","Blueberry", "Buko", "Burek", "Tamale", "Steak"]
			
pie_purchases = {
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0,
	6: 0,
	7: 0,
	8: 0,
	9: 0,
	10: 0
}

print("Welcome to the House of Pies! Here are our pies:")

while shopping == "y":
  print("---------------------------------------------------------------------")
  print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " + " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " + " (9) Tamale, (10) Steak ")
  
  pie_choice = input("Which would you like? ")
  
  pie_purchases[int(pie_choice)] += 1
  
  print("------------------------------------------------------------------------")
  
  print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")
  
  shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

print("------------------------------------------------------------------------")
print("You purchased:")
# print pies from dict
for purchase_key in pie_purchases:
  pie_list_key = purchase_key - 1
  print(f'{pie_purchases[purchase_key]} {pie_list[pie_list_key]}')