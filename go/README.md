# pan-prime-check
> Verify if a payment card PAN is a prime number.

This tool allows users to determine if their credit or debit card number 
is a prime number without having to share the card number with anyone. 
Additionally, users can inspect the source code to ensure that no suspicious activities occur with their card number. 

### Usage

```go
go run .
    1 - Check single PAN
    'quit' to exit
    Select option:
```
Select the menu option `1`
```
Enter PAN:
```
Enter a credit/debit card number to verify if it satisfies the Luhn algorithm and is also a prime number. 
Output is one of these options:
1. Not a valid PAN
2. Valid PAN but not a prime number
3. Valid PAN and a prime number

### Requirements

- [Go](https://go.dev/) 1.22 or later