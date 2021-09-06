(* ::Package:: *)

BeginPackage["Przyklad`"];


przykladowaFunkcja::usage = "przykladowaFunkcja[x] zwr\[OAcute]ci \!\(\*SuperscriptBox[\(x\), \(2\)]\).";


Begin["`Private`"];


a = 123;


przykladowaFunkcja[x_]:= x^2;


End[];


EndPackage[];
