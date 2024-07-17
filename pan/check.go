package pan

import "math/big"

type CheckResult int

const (
	CheckResultNotPAN = iota
	CheckResultPAN
	CheckResultPrimePAN
)

func Check(n int64) CheckResult {
	if isPrimeCandidate(n) {
		chkDigit := calculateMod10Checksum(n / 10)
		if chkDigit == n%10 {
			if isPrime(n, 20) {
				return CheckResultPrimePAN
			}
			return CheckResultPAN
		}
	}
	return CheckResultNotPAN
}

func isPrimeCandidate(n int64) bool {
	last := n % 10
	return last == 1 || last == 3 || last == 7 || last == 9
}

func isPrime(n int64, passes int) bool {
	return big.NewInt(n).ProbablyPrime(passes)
}

func calculateMod10Checksum(number int64) int64 {
	var sum int64
	for i := 0; number > 0; i++ {
		digit := number % 10
		if i%2 == 0 {
			digit *= 2
			if digit > 9 {
				digit -= 9
			}
		}
		sum += digit
		number /= 10
	}
	check := sum % 10
	if check != 0 {
		check = 10 - check
	}
	return check
}
