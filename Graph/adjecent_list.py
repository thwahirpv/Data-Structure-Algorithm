import copy

original_list = [1, 2, [3, 4]]
shallow_copy_list = copy.copy(original_list)

# Modifying the inner list of the shallow copy
shallow_copy_list[1]= 99

print("Original list:", original_list)  # Output: [1, 2, [99, 4]]
print("Shallow copy list:", shallow_copy_list)  # Output: [1, 2, [99, 4]]
