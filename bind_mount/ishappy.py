def isHappy(n):
    visited = set()

    while n != 1:
        if n in visited:
            return False

        visited.add(n)

        sum_of_squares = 0

        while n > 0:
            digit = n % 10
            sum_of_squares += digit * digit
            n //= 10

        n = sum_of_squares

    return True

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")