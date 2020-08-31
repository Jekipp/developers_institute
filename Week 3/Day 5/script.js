function mage(){}  // wizard poker
function make_deck(){} //
function shuffle(){} //
function deal(){} // 7 cards per player
function player_turn(){} //
function reset(){} // resets diamond_mine to diamond_share, untap royals
function draw(){} // 1 card per turn
function diamond_share(){} //player turn only, permanent, to cast card from hand diamond >= card
function royal(){} // player turn only, play facecard to table, permanent
function diamond_daze(){} // royals may not attack the turn they are played
function declare_duel(){} // declaration of royal attack, targer player, tap royal, duels may only be initiated on player turn
function block(){} // royal defends player from royal attack, multiple royals may block attacking royal
function spade_armor(){} // +#/+# attack / defense counters on target royal, permanent
function club_damage(){} // -#/-# counters on target royal, permanent
function heart_heal(){} // prevent lethal damage to royal, heart > club, heart remainder gain heart casters life, non-permanent
function drop(){} // discard diamond add # to diamond_mine
function return_spade(){} // diamond return =< spade from discard to hand
function return(){} // spade return =< any suit from discard to hand
function burn(){} // club target player -# - life, non-permanent
function gain_life(){} // heart # + life target player
function joker(){} // destroy target royal, # = 10
function pair(){} // if a royal has a club spade # pair, discard the pair
function end_turn(){} //

let life = 27 + [] // starting life
let library = [] // deck
let hand = [] // 7 card deal, no maximun size
let table = [] // royal and permanents played here
let diamond_mine = [] // sum of diamonds in shared zone
let duel_zone = [] // duel spells resolve here before player damage resolves, spades must be played before duel unless royals are tageted by opponent when they are in duel_zone
let discard = [] // cards are places in diamond zone after they resolve or are destroyed


number = [1-10, (J=1), (Q=2), (K=3)]
suit = [royal, diamond, spade, club, heart]
royal_ability = [#/#  ((attack)/(defense)) stays on table until destroyed or defense >= 0 may duel]
diamond_ability = [# = $, currency to play cards from hand, each card has casting cost = #, drop = discard diamond for 1 time diamond counter boost for caster only]
spade_ability = [+#/+# permanent counters to royal, return => card from discard to hand]
club_ability = [-#/-# permaned counters on royal, if club > royal then club - royal damages target royal controller, -# target player damage]
heart_ability = [+# added to life, prevent lethal damage to royal, heart caster gains life = remaider heart > royal - club]
