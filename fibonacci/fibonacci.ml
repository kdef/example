let rec fib_num n =
  match n with
  | 0 | 1 -> n
  | _ -> fib_num (n - 1) + fib_num (n - 2)

let () =
  int_of_string Sys.argv.(1)
  |> fib_num
  |> string_of_int
  |> print_endline
