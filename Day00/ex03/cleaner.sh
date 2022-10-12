#!/bin/bash

replace()
{
  awk -F "\"," 'BEGIN{OFS = FS}{
  if (tolower($3) ~ "junior" && tolower($3) ~ "middle" && tolower($3) ~ "senior")
    $3 = "\"Junior/Middle/Seniori"
  else if (tolower($3) ~ "junior" && tolower($3) ~ "middle")
    $3 = "\"Junior/Middle"
  else if (tolower($3) ~ "junior" && tolower($3) ~ "senior")
    $3 = "\"Junior/Senior"
  else if (tolower($3) ~ "middle" && tolower($3) ~ "senior")
    $3 = "\"Middle/Senior"
  else if (tolower($3) ~ "junior")
    $3 = "\"Junior"
  else if (tolower($3) ~ "middle")
    $3 = "\"Middle"
  else if (tolower($3) ~ "senior")
    $3 = "\"Senior"
  else
    $3 = "\"-"
  print $0}'
}

head -n 1 "../ex02/hh_sorted.csv" > hh_positions.csv
 cat "../ex02/hh_sorted.csv" | while read -r; do replace >> hh_positions.csv; done
