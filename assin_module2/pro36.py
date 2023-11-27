'''Write a Python program to combine values in python list of dictionaries.Sample data: 
[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]
Expected Output:Counter ({'item1': 1150, 'item2': 300}) '''

data: [{'item': 'item1', 'amount': 400}, 
       {'item': 'item2', 'amount':300}, 
       {'item': 'item1', 'amount': 750}]

value={}
for i in data:
    item=i['item']
    amount=i.get('amount',0)
    value[item]=value.get(item,0)+amount

print("Values:",value)