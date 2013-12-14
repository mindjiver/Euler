#!/usr/bin/env elixir

seq = [1,2,3]

defmodule Fib do
  def fib([h|t]) do
    elem = Enum.at(t, -1) + Enum.at(t, -2)
    if elem < 4000000 do
      fib([h] ++ t ++ [elem])
    else
      [h] ++ t
    end
  end
end

list = Fib.fib(seq)
even = lc n inlist list, rem(n, 2) == 0, do: n
sum = Enum.reduce(even, 0, fn(x, acc) -> x + acc end)

IO.puts "Sum: #{sum}"
