def fractional_part(numerator, denominator):
    if numerator != 0 and denominator != 0:
        div = (numerator / denominator) % 1
        if div != 0:
            return div
    return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0