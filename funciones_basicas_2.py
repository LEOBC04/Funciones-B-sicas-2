# Multiplica por 2:

# def multiplication_per_two (num):
  
#   multiples_list = []
  
#   for i in range(num+1):
    
#     multiples_list.append(i*2)
    
#   return multiples_list

# print(multiplication_per_two(5))


# ===========================================================

# Suma y resta:

# def sum_and_subtraction (numbers):
  
#   print(f"La suma de los dos números es {numbers[0] + numbers[1]}")
  
#   return numbers[0] - numbers[1]

# print(sum_and_subtraction([5,1]))


# ===========================================================

# Sumatoria menos longitud:

# def sum_minus_length(numbers):
  
#   sum_numbers = 0
  
#   for number in numbers:
#     sum_numbers += number
  
#   return f"La suma menos la longitud es {sum_numbers - len(numbers)}"

# print(sum_minus_length([1,2]))


# ===========================================================

# Valores multiplicados por el segundo: 

# def values_multiplied_by_the_second(numbers):
  
#   new_list = []
  
#   if len(numbers) < 2:
#     print(f"La longitud de la lista es {len(numbers)}")
#     return []
#   else:
#     for number in numbers:
#       new_list.append(number * numbers[1])
      
#     print(f"La longitud de la lista es {len(numbers)}")
#     return new_list
  
# print(values_multiplied_by_the_second([1]))


# ===========================================================

# Valores multiplicados y longitud

# def value_multiplied_and_length(value,lenght):
  
#   repeated_value = value * lenght
  
#   return [repeated_value] * lenght

# print(value_multiplied_and_length(7,5))