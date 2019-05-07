% Author: Santiago Valencia A01206738

% This file is part of Mondrian.
%
% Mondrian is free software: you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
%
% Mondrian is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.
%
% You should have received a copy of the GNU General Public License
% along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

% Library: Constraint Logic Programming over Finite Domains
:- use_module(library(clpfd)).

% Knowledge Base

% Colors of the painting
color(red).
color(w_1).
color(blue).
color(black).
color(w_2).
color(yellow).
color(w_3).

% Squares of the painting
square(a).
square(b).
square(c).
square(d).
square(e).
square(f).

% Edges of the painting
edge(a,b).
edge(a,c).
edge(b,c).
edge(c,d).
edge(c,e).
edge(c,f).
edge(d,e).
edge(e,f).

% ------------------------------------
% mondrian

% Function that returns a list pairs
mondrian(List) :-
  % Find all pairs that matches with an existing edge
  findall((X, Y), edge(X, Y), Edges),
  % Find all squares that matches with an existing square
  findall(X, square(X), Squares),
  % Find all pairs that their edge is a square
  findall((X, _), member(X, Squares), List),
  % Add Mondrian constraint
  constraint(Edges,List),
  % Add pairs to the list
  addColor(List).

% ------------------------------------
% constraint

% Helper function that returns the pair that has different edges
constraint([],_).
constraint([(P1,P2)|RL],List):-
  % Create two pairs from existing pair and check if their edges are different
  member((P1,C1),List),
  member((P2,C2),List),
  dif(C1,C2),
  % If pairs are different, append to the rest of the list
  constraint(RL,List).

% ------------------------------------
% addColor

% Helper function that appends a pair to the final list
addColor([]).
addColor([(_,C2)|List]) :-
  color(C2),
  addColor(List).

% Tests:
% ?- mondrian([ (a, A), (b, B), (c, C), (d, D), (e, E), (f, F)]).
% {'A': 'red', 'B': 'w_1', 'C': 'blue', 'D': 'w_1', 'E': 'w_3', 'F': 'black'}
