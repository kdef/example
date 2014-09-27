open Core.Std (* for String.to_list *)

let permute str =
  let rec prmt lst_in lst_out =
    match lst_in with
    | [] ->  print_endline lst_out (* base case: add string to list of permutations *)
    | hd :: tl -> prmt tl (hd :: lst_out)
  in
  prmt (String.to_list str) []

let () =
  permute Sys.argv.(1)
