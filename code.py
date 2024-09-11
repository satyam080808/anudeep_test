def is_palindrome(s):
    return s == s[::-1]

# Example usage
print(is_palindrome("racecar"))  # Should return True
print(is_palindrome("hello"))    # Should return False
