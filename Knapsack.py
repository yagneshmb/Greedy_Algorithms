class Item:
    def __init__ (self, weight, value):
        self.weight = int(weight)
        self.value = int(value)
        self.val_wei = self.value / self.weight
        self.val_wei = float(self.val_wei)

def zero_one_knapsack(list_items, capacity:int):
    total_value = 0
    total_value = int(total_value)
    capacity_weight = capacity
    capacity_value = capacity
    list_items_weight = list_items.copy()
    list_items_value = list_items.copy()

    print('############################################## Value/Weight decreasing ####################################################')
    list_items.sort(key=lambda x : float(x.val_wei), reverse=True)
    for i1 in range(len(list_items)):
        if(capacity > 0):
            if(list_items[i1].weight <= capacity):
                print('item with weight :', list_items[i1].weight, "and value: ", list_items[i1].value, "is taken fully")
                total_value = total_value + list_items[i1].value
                capacity = capacity - list_items[i1].weight
                #print(capacity)
            #elif(list_items[i1].weight > capacity):
             #   print('item with weight :', list_items[i1].weight, "and value : ", list_items[i1].value, "is taken partially", end = " ")
              ## total_value = total_value +  (capacity/list_items[i1].weight)*list_items[i1].value
               # break
    print('total value : ',total_value)
    print('total capacity not filled: ', capacity)

    print('############################################## Weight increasing ####################################################')
    total_value = 0
    list_items_weight.sort(key=lambda x : float(x.weight), reverse=False)
    for i1 in range(len(list_items_weight)):
        if(capacity_weight > 0):
            if(list_items_weight[i1].weight <= capacity_weight):
                print('item with weight :', list_items_weight[i1].weight, "and value: ", list_items_weight[i1].value, "is taken fully")
                total_value = total_value + list_items_weight[i1].value
                capacity_weight = capacity_weight - list_items_weight[i1].weight
                #print(capacity_weight)
    
    print('total value : ',total_value)
    print('total capacity not filled: ', capacity_weight)
    print('############################################## value decreasing ####################################################')
    total_value = 0
    list_items_value.sort(key=lambda x : float(x.value), reverse=True)
    for i1 in range(len(list_items_value)):
        if(capacity_value > 0):
            if(list_items_value[i1].weight <= capacity_value):
                print('item with weight :', list_items_value[i1].weight, "and value: ", list_items_value[i1].value, "is taken fully")
                total_value = total_value + list_items_value[i1].value
                capacity_value = capacity_value - list_items_value[i1].weight
                #print(capacity_value)
    print('total value : ',total_value)
    print('total capacity not filled: ', capacity_value)

def fractional_knapsack(list_items, capacity:int):
    total_value = 0
    total_value = int(total_value)
    capacity_weight = capacity
    capacity_value = capacity
    list_items_weight = list_items.copy()
    list_items_value = list_items.copy()

    print('############################################## Value/Weight decreasing ####################################################')
    list_items.sort(key=lambda x : float(x.val_wei), reverse=True)
    for i1 in range(len(list_items)):
        if(capacity > 0):
            if(list_items[i1].weight <= capacity):
                print('item with weight :', list_items[i1].weight, "and value: ", list_items[i1].value, "is taken fully")
                total_value = total_value + list_items[i1].value
                capacity = capacity - list_items[i1].weight
            elif(list_items[i1].weight > capacity):
                print('item with weight :', list_items[i1].weight, "and value : ", list_items[i1].value, "is taken partially", end = " ")
                print('with weight = ', (capacity/list_items[i1].weight)*list_items[i1].value)
                total_value = total_value +  (capacity/list_items[i1].weight)*list_items[i1].value
                break
    
    print('total value : ',total_value)

    print('############################################## Weight increasing ####################################################')
    list_items_weight.sort(key=lambda x : float(x.weight), reverse=False)
    total_value = 0
    for i1 in range(len(list_items_weight)):
        if(capacity_weight > 0):
            if(list_items_weight[i1].weight <= capacity_weight):
                print('item with weight :', list_items_weight[i1].weight, "and value: ", list_items_weight[i1].value, "is taken fully")
                total_value = total_value + list_items_weight[i1].value
                capacity_weight = capacity_weight - list_items_weight[i1].weight
            elif(list_items_weight[i1].weight > capacity_weight):
                print('item with weight :', list_items_weight[i1].weight, "and value : ", list_items_weight[i1].value, "is taken partially", end = " ")
                print('with weight = ', (capacity_weight/list_items_weight[i1].weight)*list_items_weight[i1].value)
                total_value = total_value +  (capacity_weight/list_items_weight[i1].weight)*list_items_weight[i1].value
                break
    
    print('total value : ',total_value)

    print('############################################## value decreasing ####################################################')
    list_items_value.sort(key=lambda x : float(x.value), reverse=True)
    total_value = 0
    for i1 in range(len(list_items_value)):
        if(capacity_value > 0):
            if(list_items_value[i1].weight <= capacity_value):
                print('item with weight :', list_items_value[i1].weight, "and value: ", list_items_value[i1].value, "is taken fully")
                total_value = total_value + list_items_value[i1].value
                capacity_value = capacity_value - list_items_value[i1].weight
            elif(list_items_value[i1].weight > capacity_value):
                print('item with weight :', list_items_value[i1].weight, "and value : ", list_items_value[i1].value, "is taken partially", end = " ")
                print('with weight = ', (capacity_value/list_items_value[i1].weight)*list_items_value[i1].value)
                total_value = total_value +  (capacity_value/list_items_value[i1].weight)*list_items_value[i1].value
                break
    
    print('total value : ',total_value)





if __name__ == "__main__":
    capacity = input('Enter knapsack capacity: ')
    capacity = int(capacity)
    n_items = input('Enter number of items: ')
    n_items = int(n_items)
    list_items = []
    for i in range(n_items):
        temp_weight, temp_value = input("Enter weight and value as space saparated input: ").split()
        temp_item = Item(temp_weight, temp_value)
        list_items.append(temp_item)
    
    list_fractioal = list_items.copy()
    print('############################ FRACTIONAL KNAPSACK #########################')
    fractional_knapsack(list_fractioal, capacity)
    list_zero_one = list_items.copy()
    print('############################ 0/1 KNAPSACK #################################')
    zero_one_knapsack(list_zero_one, capacity)
