function sumSquares(numbers) {
  return numbers.reduce((prev, curr) => prev + curr ** 2, 0);
}

const numbersArray = [1, 2, 2];

console.log(sumSquares(numbersArray));
