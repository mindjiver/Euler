#!/usr/bin/env elixir
#
# First baby steps in Elixir, will most likely be horrible code to
# look at.
#

range = 1..1000

s = Stream.filter(range, fn(x) -> rem(x, 3) == 0 or rem(x, 5) == 0 end)
{_, sum} = Enum.map_reduce(s, 0, fn(x, acc) -> { x, x + acc } end)

IO.puts "Sum: #{sum}"
