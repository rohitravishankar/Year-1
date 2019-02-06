/* Rohit Ravishankar rr9105@rit.edu */
% ALL MALES 
male(george).
male(philip).
male(spencer).
male(charles).
male(mark).
male(andrew).
male(edward).
male(william).
male(harry).
male(peter).
male(james).


% ALL FEMALES
female(mum).
female(kydd).
female(elizabeth).
female(margaret).
female(diana).
female(anne).
female(sarah).
female(sophie).
female(zara).
female(beautrice).
female(eugenie).
female(louise).


% ALL MARRIAGES
marriedto(george, mum).
marriedto(mum, george).

marriedto(elizabeth, philip).
marriedto(philip, elizabeth).

marriedto(spencer, kydd).
marriedto(kydd, spencer).

marriedto(diana, charles).
marriedto(charles, diana).
marriedto(anne, mark).
marriedto(mark, anne).
marriedto(andrew, sarah).
marriedto(sarah, andrew).
marriedto(edward, sophie).
marriedto(sophie, edward).


% Great grandparents
parent(george, elizabeth).
parent(george, margaret).
parent(mum, elizabeth).
parent(mum, margaret).


% Distant family
parent(spencer, diana).
parent(kydd, diana).


% Grandparents
parent(elizabeth, charles).
parent(philip, charles).
parent(elizabeth, anne).
parent(philip, anne).
parent(elizabeth, andrew).
parent(philip, andrew).
parent(elizabeth, edward).
parent(philip, edward).


% Parents - 1
parent(diana, william).
parent(diana, harry).
parent(charles, william).
parent(charles, harry).


% Parents - 2
parent(anne, peter).
parent(anne, zara).
parent(mark, peter).
parent(mark, zara).


% Parents - 3
parent(andrew, beautrice).
parent(andrew, eugenie).
parent(sarah, beautrice).
parent(sarah, eugenie).


% Parents - 4
parent(edward, louise).
parent(edward, james).
parent(sophie, louise).
parent(sophie, james).


grandchild(A, B) :- 
	parent(X, A), 
	parent(B, X).

greatgrandparent(A, B):- 
	parent(X, B), 
	parent(Y, X), 
	parent(A, Y).

ancestor(A, B) :- 
	parent(A, B); 
	parent(A, X), 
	ancestor(X, B).

daughter(A, B) :-
	female(A),
	parent(B, A).

son(A, B) :-
	male(A),
	parent(B, A).

siblings(A, B) :- 
	parent(X, A), 
	parent(X, B), 
	A \== B.

firstcousin(A, B) :- 
	parent(X, A), 
	parent(Y, B), 
	siblings(X, Y).

brother(A, B) :- 
	male(A), 
	siblings(A, B).

sister(A, B) :- 
	female(A), 
	siblings(A, B).

brotherinlaw(A, B) :- 
	sister(X, B), 
	marriedto(X, A).

sisterinlaw(A, B) :- 
	brother(X, B), 
	marriedto(A, X).

uncle(A, B) :- 
	parent(P, B), 
	(brother(A, P); 
		brotherinlaw(A, P)).

aunt(A, B) :- 
	parent(P, B), 
	(sister(A, P); 
		sisterinlaw(A, P)).