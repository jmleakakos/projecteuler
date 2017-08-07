# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import Kernel
import Enum

defmodule Euler do
  def reduceFunction(number, accumulator) do
    if (rem(number, 3) == 0 || rem(number, 5) == 0), do: number + accumulator, else: accumulator
  end
end

IO.puts reduce(to_list(1..999), 0, &Euler.reduceFunction/2)
